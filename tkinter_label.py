# -*- coding: utf-8 -*-
#http://www.cyberforum.ru/python-graphics/thread1952009.html#post10294052

from tkinter import *
from tkinter.filedialog import *


class create_label:
    def __init__(self, text, f, txtVar):
        self.lbl = Label(root, textvariable=txtVar)
        self.lbl["text"] = text
        self.lbl["bg"] = f
        self.lbl["font"] = "Arial 12"
        self.lbl.pack()


def calc(event):
    a = "a"
    b = "b"
    lblVar.set(a)

if __name__ == "__main__":
    root = Tk()
    root.geometry('640x480+400+90')
    but = Button(root, text='Рассчитать', width=10, height=3, font='arial 14')
    but.bind("<Button-1>", calc)
    but.pack()
    lblVar = StringVar()
    lbl = create_label('Text:', None, lblVar)

    root.mainloop()