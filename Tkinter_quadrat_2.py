# -*- coding: utf-8 -*-
#http://www.cyberforum.ru/python-graphics/thread1955553.html

from Tkinter import *
import time
from random import choice


def draw(row, col, color, count, last_row):

        x1 = col * sizeX
        y1 = row * sizeY
        x2 = x1 + sizeX
        y2 = y1 + sizeY
        rectId = canvas.create_rectangle(x1,y1,x2,y2, fill=color, outline=color)

        last_row.append(rectId)
        if count == number_total:
            print last_row
            #for _id in last_row:
                #canvas.move(_id, -)
            canvas.delete("all")
            print "Done!"
            return

        count += 1
        col += 1
        if (col > cols - 1):
            col = 0
            row += 1
            last_row = []

        
        canvas.after(refresh_rate, lambda: draw(row, col, choice(colors), count, last_row))

 
if __name__ == "__main__":
    width = 800
    height = 600

    print 'Enter the number of quadrats in row:'
    cols=input()
    print 'Enter the total number of quadrats:'
    number_total=input()
    print 'Enter refresh rate (in msec):'
    refresh_rate=input()
    print 'The number of elements in row:', cols
    print 'The number of elements:', number_total
    print 'Refresh rate:', refresh_rate

    rows=number_total//cols
    print "rows: ", rows

    sizeX = width//cols
    sizeY = height//cols
    print 'sizeX: %d; sizeY: %d' % (sizeX, sizeY)
 
    tk = Tk()
    tk.title("laboratory_number_5")
    tk.wm_geometry("%dx%d+20+40" % (width, height))
    canvas = Canvas(tk, width=width, height=height)
    colors = ["Red","Orange","Yellow","Green","LightBlue","Blue","Violet"]
    draw(0, 0, choice(colors), 1, [])
    canvas.pack()
    tk.mainloop()
