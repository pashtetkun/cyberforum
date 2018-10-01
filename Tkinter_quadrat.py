# -*- coding: utf-8 -*-
#http://www.cyberforum.ru/python-graphics/thread1954222.html

from Tkinter import *
import time
from random import choice


def draw(i, color):
    size = 50
    x = 0 + i * size
    y = 0
    canvas.create_rectangle(x,0, x+size, 0+size, fill=color, outline=color)
    canvas.after(1000, lambda: draw(i+1, choice(colors)))

if __name__ == "__main__":
    tk = Tk()
    tk.title("laboratory_number_5")
    tk.wm_geometry("800x600+20+40")
    canvas = Canvas(tk, width=800, height=600)
    colors = "Red Orange Yellow Green LightBlue Blue Violet".split()
    draw(0, choice(colors))
    canvas.pack()
    tk.mainloop()
