##
# File: ParserErrorListner.py
# Date: 11-Feb-2022
#
# Updates:
""" Inheritance of ANTLR ErrorListener for Parser.
    @author: Masashi Yokochi
"""
from antlr4.error.ErrorListener import ErrorListener

try:
    from wwpdb.utils.nmr.mr.ParserListenerUtil import MAX_ERROR_REPORT
except ImportError:
    from nmr.mr.ParserListenerUtil import MAX_ERROR_REPORT


class ParserErrorListener(ErrorListener):

    __messageList = None
    __errorLineNumber = None

    __filePath = None

    __maxErrorReport = MAX_ERROR_REPORT

    def __init__(self, filePath, maxErrorReport=MAX_ERROR_REPORT):

        self.__messageList = []
        self.__errorLineNumber = []

        self.__filePath = filePath

        self.__maxErrorReport = maxErrorReport

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        if line not in self.__errorLineNumber:
            self.__errorLineNumber.append(line)

        if len(self.__messageList) >= self.__maxErrorReport:
            return

        _msg = msg.split("'")
        length = 1 if 'alternative' in msg or len(_msg) < 2 else len(_msg[1])

        _dict = {'file_path': self.__filePath,
                 'line_number': line,
                 'column_position': column,
                 'message': msg,
                 'marker': " " * (column) + "^" * (length)}

        _line = 1
        with open(self.__filePath, 'r', encoding='utf-8') as ifp:
            for content in ifp:
                if _line == line:
                    _dict['input'] = content.replace('\t', ' ')\
                        .replace('\r', ' ').replace('\n', ' ')\
                        .rstrip(' ')
                    break
                _line += 1

        if 'at input' in _dict['message']:  # parser error
            try:
                p = _dict['message'].index('at input')
                _dict['message'] = _dict['message'][0:p] + 'at input:'
            except ValueError:
                pass

        self.__messageList.append(_dict)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

    def getMessageList(self):
        return self.__messageList if len(self.__messageList) > 0 else None

    def getErrorLineNumber(self):
        return self.__errorLineNumber if len(self.__errorLineNumber) > 0 else None
