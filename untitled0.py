# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:41:22 2024

@author: mk
"""
import tkinter as Tk
pencere = Tk.Tk()
from tkinter import Entry, Button
pencere.geometry("250x300")

def yaz(x):
    s = len(giris.get())
    giris.insert(s, str(x))

hesap = 5
s1 = 0

def islemler(x):
    global hesap
    hesap = x 
    global s1 
    s1 = float(giris.get())
    giris.delete(0, 'end')

s2 = 0
def hesapla():
    global s2
    s2 = float(giris.get())
    global hesap
    sonuc = 0
    if hesap == 0: 
        sonuc = s1 + s2
    elif hesap == 1: 
        sonuc = s1 - s2
    elif hesap == 2: 
        sonuc = s1 * s2
    elif hesap == 3: 
        if s2 != 0:
            sonuc = s1 / s2
        else:
            sonuc = "Error"
    giris.delete(0, 'end')
    giris.insert(0, str(sonuc))

giris = Entry(font="Verdana 14 bold", width=15, justify="right")
giris.place(x=20, y=20)

b = []
for i in range(1, 10): 
    b.append(Button(text=str(i), font="Verdana 14 bold", command=lambda x=i: yaz(x)))

sayac = 0
for i in range(0, 3):
    for j in range(0, 3):
        b[sayac].place(x=20+j*50, y=50+i*50)
        sayac += 1

islem = []
for i in range(0, 4):
    islem.append(Button(font="Verdana 14 bold", width=2, command=lambda x=i: islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(0, 4):
    islem[i].place(x=170, y=50+50*i)

sb = Button(text="0", font="Verdana 14 bold", command=lambda x=0: yaz(x))
sb.place(x=20, y=200)

nb = Button(text=".", font="Verdana 14 bold", width=2, command=lambda x=".": yaz(x))
nb.place(x=70, y=200)

eb = Button(text="=", fg="red", font="Verdana 14 bold", command=hesapla)
eb.place(x=120, y=200)


pencere.mainloop()