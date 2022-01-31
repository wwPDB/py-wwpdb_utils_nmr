##
# File: MRErrorListner.py
# Date: 26-Jan-2022
#
# Updates:
""" Inheritance of ANTLR ErrorListener for MR Parser.
    @author: Masashi Yokochi
"""
import os
import os.path

from antlr4.error.ErrorListener import ErrorListener


class MRErrorListener(ErrorListener):

    __messageList = None

    __filePath = None
    __fileName = None

    def __init__(self, filePath, fileName=None):

        self.__filePath = filePath

        self.__fileName = fileName\
            if fileName is not None and len(fileName) > 0\
            else os.path.basename(filePath)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        if self.__messageList is None:
            self.__messageList = []

        dict = {'file_path': self.__filePath,
                'file_name': self.__fileName,
                'line_number': line,
                'column_position': column,
                'message': msg}

        _line = 1
        with open(self.__filePath, 'r', encoding='UTF-8') as ifp:
            for content in ifp:
                if _line == line:
                    dict['input'] = content.replace('\t', ' ')\
                        .replace('\r', ' ').replace('\n', ' ')\
                        .rstrip(' ')
                    break
                _line += 1

        if 'input' in dict:
            dict['marker'] = " " * (column - 1) + "^"

        self.__messageList.append(dict)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

    def getMessageList(self):
        return self.__messageList
