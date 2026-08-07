##
# File: AntlrParseUtil.py
# Date: 7-Aug-2026
#
# Updates:
""" A single ANTLR parse driver shared by every *Reader class in this package.

    Historically each *Reader.py repeated the same
    InputStream -> Lexer -> CommonTokenStream -> Parser -> parser.<rule>()
    sequence inline, together with the LexerErrorListener/ParserErrorListener
    wiring. That block is centralized here so that the speedy-antlr-tool C++
    accelerator can be substituted for the pure-Python ANTLR runtime in one
    place.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

from typing import Optional, Tuple

from antlr4 import CommonTokenStream, InputStream, PredictionMode
from antlr4.tree.Tree import ParseTree

try:
    from wwpdb.utils.nmr.NmrDpConstant import MAX_ERROR_REPORT
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.mr.SpeedyAntlrErrorListener import createSpeedyAntlrErrorListener
except ImportError:
    from nmr.NmrDpConstant import MAX_ERROR_REPORT
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.mr.SpeedyAntlrErrorListener import createSpeedyAntlrErrorListener


def usingCppParser(saModule) -> bool:
    """ Return whether the given sa_<grammar> shim module will use its compiled
        C++ accelerator. False when the extension was not built for this
        platform, in which case parseAntlr() runs the pure-Python ANTLR runtime.
    """

    return saModule is not None and getattr(saModule, 'USE_CPP_IMPLEMENTATION', False)


def parseAntlr(lexerClass, parserClass, entryRuleName: str, inputString: str,
               filePath: Optional[str] = None, saModule=None,
               maxLexerErrorReport: int = MAX_ERROR_REPORT,
               maxParserErrorReport: int = MAX_ERROR_REPORT,
               ignoreCodicError: bool = False,
               predictionModeSll: bool = False,
               reportInputString: Optional[str] = None
               ) -> Tuple[ParseTree, ParserErrorListener, LexerErrorListener]:
    """ Lex and parse the given input, using the compiled C++ parser when it is
        available and the pure-Python ANTLR runtime otherwise.
        @param lexerClass: generated ANTLR lexer class (Python fallback path)
        @param parserClass: generated ANTLR parser class (Python fallback path)
        @param entryRuleName: name of the grammar's top-level rule, e.g. 'nmrpipe_cs'
        @param inputString: the whole input to parse
        @param filePath: source file path, or None when parsing a string
        @param saModule: the generated sa_<grammar> shim module, or None to force
                         the pure-Python path
        @param predictionModeSll: use the simpler/faster SLL prediction mode.
                                  Honored on both the C++ and the Python path, so
                                  Readers that decide it per call (XplorMR, CnsMR,
                                  CyanaMR, CharmmMR, SchrodingerMR, CyanaNOA) keep
                                  working against a single compiled accelerator.
        @param reportInputString: input echoed in error reports when filePath is
                                  None (the error listeners' 'inputString' argument)
        @return: the parse tree, ParserErrorListener, LexerErrorListener
    """

    lexerErrorListener = LexerErrorListener(filePath, inputString=reportInputString,
                                            maxErrorReport=maxLexerErrorReport,
                                            ignoreCodicError=ignoreCodicError)
    parserErrorListener = ParserErrorListener(filePath, inputString=reportInputString,
                                              maxErrorReport=maxParserErrorReport,
                                              ignoreCodicError=ignoreCodicError)

    stream = InputStream(inputString)

    if usingCppParser(saModule):

        # The C++ lexer and parser both run inside saModule.parse(); their
        # syntax errors are funnelled through a single SA_ErrorListener, which
        # the adapter splits back into the two listeners above.
        errorListener = createSpeedyAntlrErrorListener(saModule, lexerErrorListener, parserErrorListener)

        tree = saModule.parse(stream, entryRuleName, errorListener, predictionModeSll)

        return tree, parserErrorListener, lexerErrorListener

    # Pure-Python fallback. Deliberately not saModule._py_parse(), which neither
    # honors the SLL prediction mode nor reports through the ANTLR listeners.
    lexer = lexerClass(stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexerErrorListener)

    parser = parserClass(CommonTokenStream(lexer))
    if predictionModeSll:
        # try with simpler/faster SLL prediction mode
        parser._interp.predictionMode = PredictionMode.SLL  # pylint: disable=protected-access
    parser.removeErrorListeners()
    parser.addErrorListener(parserErrorListener)

    entryRule = getattr(parser, entryRuleName, None)
    if entryRule is None:
        raise ValueError(f"Invalid entry_rule_name '{entryRuleName}' for {parserClass.__name__}.")

    return entryRule(), parserErrorListener, lexerErrorListener
