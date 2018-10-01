# -*- coding: utf-8 -*-
#http://www.cyberforum.ru/python-graphics/thread1999838.html

from tkinter import *
 
#Функция открытия нового окна
def openNewWindow(event):
    door = var.get()
    print(door)
    y = var1.get()
    print(y)
    x = var2.get()
    print(x)
    if (x == 0) & (y != 2):
        str = 'Не может быть шума без группы'
    else:
        if door == 1:
            error = Toplevel()
            Label(error, text = 'Дверь закрыта, попробуйте открыть').grid(row = 0, column = 0)
            buton = Button(error, text='Далее')
            buton.grid(row=1, column=0, columnspan=2)
            buton.bind("<Button-1>", error.withdraw())
 
        else:
            fw.withdraw()
 
 
#Создание объекта окна
fw = Tk()
fw.title(u'Виртуальный тренажер')
#Объект кнопка
but = Button(fw)
#Верхний текст
tv = StringVar()
Label(fw, width=50,textvariable=tv,relief="groove",
      borderwidth=3,font=("Times New Romans", 10, "bold"))\
    .grid(row = 1, column = 0,columnspan = 2)
tv.set("Дверь открыта?")
#Верхние Радиокнопки
var=IntVar()
rad0 = Radiobutton(fw,text="Да",
variable=var,value=0)
rad0.grid(row = 2, column = 1)
rad1 = Radiobutton(fw,text="Нет",
variable=var,value=1)
rad1.grid(row = 2, column = 0)
#Текст перед кнопкой
tq = StringVar()
tq.set("Шум из аудитории")
Label(fw, width=50,textvariable=tq,relief="groove",
      borderwidth=3,font=("Times New Romans", 10, "bold"))\
    .grid(row = 3, column = 0, columnspan = 2)
#Кнопка воспроизвести
but["text"]='Воспроизвести'
but.grid(row = 4, column = 0, columnspan = 2)
#Средний текст
tw=StringVar()
tw.set("Причина шума")
Label(fw, width=50,textvariable=tw,relief="groove",
      borderwidth=3,font=("Times New Romans", 10, "bold"))\
    .grid(row = 5, column = 0, columnspan = 2)
#Средние Радиокнопки
var1=IntVar()
rad2 = Radiobutton(fw,text="Гул",
variable=var1,value=0)
rad2.grid(row = 6, column = 0)
rad3 = Radiobutton(fw,text="Обсуждение",
variable=var1,value=1)
rad3.grid(row = 6, column = 1)
rad4 = Radiobutton(fw,text="Тишина",
variable=var1,value=2)
rad4.grid(row = 7, column = 0, columnspan = 2)
#Текст перед рисунком
te = StringVar()
te.set("Состояние группы")
Label(fw, width=50,textvariable=te,relief="groove",
      borderwidth=3,font=("Times New Romans", 10, "bold"))\
    .grid(row = 8, column = 0, columnspan = 2)
#Рисунок
canvas = Canvas(fw,width=500,height=400)
canvas.grid(row = 9, column = 0, columnspan = 3)

#Нижние Радиокнопки
var2=IntVar()
rad2 = Radiobutton(fw,text="Никого нет", variable=var2,value=0)
rad2.place(x= 0, y = 495)
rad3 = Radiobutton(fw,text="Группа присутствует", variable=var2,value=1)
rad3.place(x=150 , y = 495)
#Переменные передачи
door = var.get()
classroom = var1.get()
classcount = var2.get()
#Кнопка Далее
buton1=Button(fw,text = 'Далее')
buton1.place(x=300 , y = 500)
buton1.bind("<Button-1>",openNewWindow)
#Вывод окна
fw.mainloop()

