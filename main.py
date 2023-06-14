from antlr4 import *
from dist.ExprParser import ExprParser
from dist.ExprLexer import ExprLexer
from dist.ExprListener import ExprListener
from dist.ExprVisitor import ExprVisitor
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            text1.delete("1.0", tk.END)
            text1.insert(tk.END, file.read())

def save_file1():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text1.get("1.0", tk.END))

def save_file2():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text2.get("1.0", tk.END))

def convert():
    text2.delete("1.0", tk.END)
    input_stream = InputStream(text1.get("1.0", tk.END))
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    visitor = ExprVisitor(text2)
    visitor.visit(tree)




def clear_text():
    text1.delete("1.0", tk.END)
    text2.delete("1.0", tk.END)

root = tk.Tk()
root.title("Notepad")

# Create a frame to hold the text widgets and scrollbars
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Create the first text widget
text1 = tk.Text(frame, height=30, width=40)
text1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the first text widget
scrollbar1 = tk.Scrollbar(frame, command=text1.yview)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
text1.config(yscrollcommand=scrollbar1.set)

# Create the second text widget
text2 = tk.Text(frame, height=30, width=40)
text2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the second text widget
scrollbar2 = tk.Scrollbar(frame, command=text2.yview)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
text2.config(yscrollcommand=scrollbar2.set)

# Create buttons for saving text1 and text2
save_button1 = tk.Button(root, text="Save Left Text", command=save_file1)
save_button1.pack(side=tk.LEFT, padx=5, pady=5)

save_button2 = tk.Button(root, text="Save Right Text", command=save_file2)
save_button2.pack(side=tk.LEFT, padx=5, pady=5)
save_button3 = tk.Button(root, text="Convert Left Text", command=convert)
save_button3.pack(side=tk.LEFT, padx=5, pady=5)

# Create a menu bar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Clear", command=clear_text)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Configure the root window to use the menu bar
root.config(menu=menubar)

# Run the application
root.mainloop()