/*
 * File: latin1_input_stream.h
 * Date: 01-Oct-2026  M. Yokochi
 *
 * A read-only antlr4::CharStream over a Python str stored one byte per character
 * (PyUnicode_1BYTE_KIND: every code point is U+00FF or lower, e.g. any ASCII
 * file). The do_parse() of each speedy-antlr accelerator lexes such a str in
 * place instead of handing ANTLRInputStream a UTF-8 copy that it decodes into a
 * UTF-32 copy of its own (4 bytes per character); any other str still goes
 * through ANTLRInputStream (DAOTHER-7829, 9785).
 *
 * The code points, indices, LA() and seek() semantics are those of
 * ANTLRInputStream for the same str, so tokens, their positions and the lexer's
 * error messages do not change. getText() and toString() return UTF-8, as
 * ANTLRInputStream does, because the Python side decodes them as UTF-8.
 *
 * Hand-written, not generated: tools/gen_speedy_antlr.py patches the generated
 * do_parse() to use it and leaves this file alone.
 */

#pragma once

#include <algorithm>
#include <cassert>
#include <string>

#include "antlr4-runtime.h"

namespace wwpdb {

class Latin1InputStream : public antlr4::CharStream {
  public:
    // 'data' must outlive the stream; do_parse() holds the str for the whole parse.
    Latin1InputStream(const unsigned char *data, size_t length) : _data(data), _size(length), p(0) {}

    void consume() override {
        if (p >= _size) {
            assert(LA(1) == antlr4::IntStream::EOF);
            throw antlr4::IllegalStateException("cannot consume EOF");
        }
        p++;
    }

    size_t LA(ssize_t i) override {
        if (i == 0) {
            return 0;  // undefined
        }
        ssize_t position = static_cast<ssize_t>(p);
        if (i < 0) {
            i++;  // e.g., translate LA(-1) to use offset i=0; then _data[p+0-1]
            if ((position + i - 1) < 0) {
                return antlr4::IntStream::EOF;  // invalid; no char before first char
            }
        }
        if ((position + i - 1) >= static_cast<ssize_t>(_size)) {
            return antlr4::IntStream::EOF;
        }
        return _data[static_cast<size_t>(position + i - 1)];
    }

    size_t index() override { return p; }

    size_t size() override { return _size; }

    ssize_t mark() override { return -1; }

    void release(ssize_t /* marker */) override {}

    void seek(size_t index) override {
        if (index <= p) {
            p = index;  // just jump; don't update stream state (line, ...)
            return;
        }
        index = std::min(index, _size);
        while (p < index) {
            consume();
        }
    }

    std::string getText(const antlr4::misc::Interval &interval) override {
        if (interval.a < 0 || interval.b < 0) {
            return "";
        }
        size_t start = static_cast<size_t>(interval.a);
        size_t stop = static_cast<size_t>(interval.b);
        if (stop >= _size) {
            stop = _size - 1;
        }
        size_t count = stop - start + 1;  // wraps around when start > stop + 1, as in ANTLRInputStream
        if (start >= _size) {
            return "";
        }
        // ANTLRInputStream takes u32string_view::substr(start, count), which clamps count to the end
        return toUtf8(_data + start, std::min(count, _size - start));
    }

    std::string getSourceName() const override { return antlr4::IntStream::UNKNOWN_SOURCE_NAME; }

    std::string toString() const override { return toUtf8(_data, _size); }

  private:
    const unsigned char *_data;
    size_t _size;
    size_t p;

    // Latin-1 code points to UTF-8: U+0000-U+007F as one byte, U+0080-U+00FF as two.
    static std::string toUtf8(const unsigned char *s, size_t n) {
        std::string out;
        out.reserve(n);
        for (size_t k = 0; k < n; k++) {
            unsigned char c = s[k];
            if (c < 0x80) {
                out.push_back(static_cast<char>(c));
            } else {
                out.push_back(static_cast<char>(0xC0 | (c >> 6)));
                out.push_back(static_cast<char>(0x80 | (c & 0x3F)));
            }
        }
        return out;
    }
};

}  // namespace wwpdb
