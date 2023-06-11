from antlr4 import *
from dist.ExprParser import ExprParser
from dist.ExprLexer import ExprLexer
from dist.ExprListener import ExprListener
from dist.ExprVisitor import ExprVisitor
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class HelloPrintListener(ExprListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())


def main():
    messagebox.showinfo("Title", "Choose a file to convert")
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not file_path:
        return messagebox.showinfo("Title", "Wrong file")
    messagebox.showinfo("Title", "Choose a folder for an output file")
    root = tk.Tk()
    root.withdraw()
    output_path = filedialog.askdirectory()
    if not output_path:
        return messagebox.showinfo("Title", "Wrong directory")
    input_stream = FileStream(file_path)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    visitor = ExprVisitor(output_path)
    visitor.visit(tree)
    messagebox.showinfo(f"Success", f"FIle was created in {output_path}")


if __name__ == '__main__':
    main()


