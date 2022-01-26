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

        description = f"SyntaxError: {msg}\n"
        description += f"  File \"{self.__fileName}\", line {line}\n"

        _line = 1
        with open(self.__filePath, 'r', encoding='UTF-8') as ifp:
            for content in ifp:
                if _line == line:
                    description += content
                    break
                _line += 1

        description += " " * (column - 1) + "^"

        self.__messageList.append(description)

    def getMessageList(self):
        return self.__messageList
