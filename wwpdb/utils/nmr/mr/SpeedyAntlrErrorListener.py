##
# File: SpeedyAntlrErrorListener.py
# Date: 7-Aug-2026
#
# Updates:
""" Adapter that routes speedy-antlr-tool syntax errors back into the ANTLR
    LexerErrorListener/ParserErrorListener pair used throughout this package.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import re

# speedy-antlr-tool cannot bridge an ANTLR ErrorListener across the C++ boundary.
# Each generated sa_<grammar>.py shim instead declares its own SA_ErrorListener
# class, and the shim's _cpp_parse() asserts isinstance() against *that* class -
# so the adapter has to be derived per shim module. The derived classes are
# cached here, keyed by shim module, because generating one per parse would be
# wasteful on the hot path.
__adapterCache = {}

# The ANTLR lexer only ever reports "token recognition error at: '...'"; every
# other message shape ("mismatched input ... expecting ...", "missing X at ...",
# "extraneous input ... expecting ...", "no viable alternative at input ...")
# comes from the parser. This mirrors the discrimination the two listeners
# already perform internally (LexerErrorListener tests "error at" in the
# message, ParserErrorListener tests "at input").
LEXER_ERROR_PREFIX = 'token recognition error'

# ANTLR's C++ target escapes '?' as '?' in its literal-token table, to keep
# the generated C++ clear of trigraphs. That escape leaks verbatim into the
# "expecting {...}" part of a parser error message, so an SLL parse of an XPLOR
# restraint file reports "'?'" where the Python runtime reports "'?'".
# Undo any such escape so both paths produce byte-identical reports.
unicode_escape_pattern = re.compile(r'\\u([0-9A-Fa-f]{4})')


def isLexerErrorMessage(msg: str) -> bool:
    """ Return whether an ANTLR syntax error message originates from the lexer.
    """

    return msg is not None and msg.startswith(LEXER_ERROR_PREFIX)


def normalizeErrorMessage(msg: str) -> str:
    """ Rewrite a C++ ANTLR syntax error message to match the Python runtime's.
    """

    if msg is None or '\\u' not in msg:
        return msg

    return unicode_escape_pattern.sub(lambda m: chr(int(m.group(1), 16)), msg)


def createSpeedyAntlrErrorListener(saModule, lexerErrorListener, parserErrorListener):
    """ Create an SA_ErrorListener for the given sa_<grammar> shim module that
        delegates to the supplied LexerErrorListener/ParserErrorListener.
        @return: an instance of a subclass of saModule.SA_ErrorListener
    """

    adapterClass = __adapterCache.get(saModule)

    if adapterClass is None:

        class _SpeedyAntlrErrorListener(saModule.SA_ErrorListener):
            """ Route C++ lexer/parser syntax errors to the ANTLR error listeners.
            """

            def __init__(self, lexerErrorListener, parserErrorListener):
                self.lexerErrorListener = lexerErrorListener
                self.parserErrorListener = parserErrorListener

            # 'input_stream' and 'char_index' are part of the SA_ErrorListener
            # signature that the C++ side calls positionally; the two ANTLR
            # listeners work from (line, column) alone.
            def syntaxError(self, input_stream, offendingSymbol, char_index,  # pylint: disable=unused-argument
                            line, column, msg):
                msg = normalizeErrorMessage(msg)
                # The ANTLR listeners ignore both 'recognizer' and the exception,
                # so passing None for each preserves their behavior exactly.
                if isLexerErrorMessage(msg):
                    self.lexerErrorListener.syntaxError(None, offendingSymbol, line, column, msg, None)
                else:
                    self.parserErrorListener.syntaxError(None, offendingSymbol, line, column, msg, None)

        adapterClass = __adapterCache[saModule] = _SpeedyAntlrErrorListener

    return adapterClass(lexerErrorListener, parserErrorListener)
