from antlr4 import *
from dist.ExprParser import ExprParser
from dist.ExprLexer import ExprLexer
from dist.ExprListener import ExprListener
from dist.ExprVisitor import ExprVisitor


class HelloPrintListener(ExprListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())


def main():

    input_stream = FileStream("data.txt")
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    visitor = ExprVisitor()

    visitor.visit(tree)


if __name__ == '__main__':
    main()


