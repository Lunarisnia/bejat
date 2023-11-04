import sys
import antlr4
from grammar.BejatLexer import BejatLexer
from grammar.BejatParser import BejatParser

from src.ast.bejat_custom_visitor import BejatCustomVisitor

def main(argv):
    input_stream = antlr4.FileStream(argv[1])
    lexer = BejatLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = BejatParser(tokens)

    start_context = parser.start()
    if parser.getNumberOfSyntaxErrors() > 0:
        # TODO: add custom syntax handler
        print("syntax errors")
        exit(0)
    else:
        bejat_visitor = BejatCustomVisitor()
        bejat_visitor.visit(start_context)

if __name__ == "__main__":
    main(sys.argv)