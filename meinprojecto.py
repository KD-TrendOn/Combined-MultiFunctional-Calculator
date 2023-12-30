import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
from math import e, pi, sqrt, cos, sin, tan, asin, acos, atan, log10
import random
from tkinter import *
import tkinter.messagebox as mb
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
from tkinter.ttk import Treeview
from tkinter import messagebox
from tkinter import scrolledtext
import math
import re
import webbrowser
import yfinance.base
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from bs4 import BeautifulSoup

matplotlib.use("TkAgg")


# The Table class for money Calc
class Table(Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=CENTER)
            table.column(head, anchor=CENTER, width=275)

        for row in rows:
            table.insert('', END, values=tuple(row))

        scrolltable = Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=RIGHT, fill=Y)
        table.pack(expand=YES, fill=BOTH)


# Global variables:
numbuk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '+', '-', '/', '*', '**', 'sin(', 'cos(',
          'tg(', 'ctg(', 'asin(', 'acos(', 'atg(', 'actg(', '.', 'sqrt(']
textrazm = 25
caramba = 12
rads = math.radians
deg = math.degrees
atg = atan
tg = tan
israd = True
bobr = ['sin(', 'cos(', 'tg(', 'ctg(']
ogr = ['asin(', 'acos(', 'atg(', 'actg(']
opaska = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
bez = ['(', '+', '-', '/', '*']
tochznach = 2
kakov = 'Вклад'
mesyaca = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
           'Декабрь']
yok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
provka = [(1, ''), (1, '.ME'), (1, '-USD'), (0, '^')]


def ctg(c132):
    return tan(1 / c132)


def actg(c123):
    return pi / 2 - atg(c123)


def radonoff():
    global israd
    israd = not israd
    if rad['text'] == 'Rad':
        rad['text'] = 'Deg'
    else:
        rad['text'] = 'Rad'


def type_char(char):
    print(char)
    global numbuk, textrazm, caramba, bobr, opaska, bez, tochznach
    if len(char) + len(calc.get()) > caramba:
        calc.configure(font=("Times New Roman", textrazm))
        textrazm = int(round(textrazm / 2, 0))
        caramba *= 2
    if char in numbuk:
        if char in bobr:
            print(char)
            if not israd:
                value = calc.get() + char + 'rads('
                calc.delete(0, END)
                calc.insert(0, value)
            else:
                value = calc.get() + char
                calc.delete(0, END)
                calc.insert(0, value)
        elif char in ogr:
            if not israd:
                value = calc.get() + 'deg(' + char
                calc.delete(0, END)
                calc.insert(0, value)
            else:
                value = calc.get() + char
                calc.delete(0, END)
                calc.insert(0, value)
        else:
            value = calc.get() + char
            calc.delete(0, END)
            calc.insert(0, value)
    elif char == '=':
        tochznach = int(spin.get())
        try:
            aboba = round(eval(calc.get() + ')' * (calc.get().count('(') - calc.get().count(')'))), tochznach)
        except BaseException:
            mb.showerror('Ошибка', 'Неверные данные')
        else:
            if aboba > 10 ** 21:
                aboba = str(aboba)[0] + '.' + str(aboba)[1:tochznach] + 'e+' + str(int(round(log10(aboba), 0)))
            elif len(str(aboba)[str(aboba).find('.'):]) > 12 and aboba < 1:
                aboba = str(aboba)[0] + '.' + str(aboba)[1:tochznach] + 'e-' + str(
                    int(round(log10(aboba), 0)))
            calc.delete(0, END)
            calc.insert(0, str(aboba).replace('..', '.'))
    elif char == '←':
        bob = calc.get()[0:len(calc.get()) - 1]
        calc.delete(0, END)
        calc.insert(0, bob)
    elif char == 'e' or char == 'pi':
        now = calc.get()
        if not len(now):
            now = '(' + char + ')'
            calc.insert(0, now)
        else:
            if now[-1] in bez:
                now = calc.get() + '(' + char + ')'
                calc.delete(0, END)
                calc.insert(0, now)
            else:
                now = calc.get() + '*(' + char + ')'
                calc.delete(0, END)
                calc.insert(0, now)


def ochist():
    global caramba
    global textrazm
    calc.delete(0, END)
    calc.configure(font=('Arial Bond', 50))
    ent11.delete(0, END)
    ent12.delete(0, END)
    ent13.delete(0, END)
    ent14.delete(0, END)
    ent151.delete(0, END)
    ent152.delete(0, END)
    ent21.delete(0, END)
    ent231.delete(0, END)
    ent232.delete(0, END)
    ent233.delete(0, END)
    ent241.delete(0, END)
    ent242.delete(0, END)
    ent243.delete(0, END)
    textrazm = 25
    caramba = 12


def podtv():
    global mesyaca
    goo = 1
    if ent14.get() == '':
        goo = 0
    try:
        ent11g = float(ent11.get())
        ent12g = float(ent12.get())
        gm12g = com12.get()
        ent13g = int(ent13.get())
        gm13g = com13.get()
        if goo:
            ent14g = float(ent14.get())
        else:
            ent14g = 0
        gm14g = com14.get()
        ent151g = int(ent151.get())
        if ent152.get()[0] == '0':
            ent152g = int(ent152.get()[1])
        else:
            ent152g = int(ent152.get())
        if ent151g <= 0 or ent152g <= 0 or ent152g >= 13 or ent11g <= 0 or ent11g <= 0 or ent13g <= 0:
            raise ValueError
    except ValueError as ve:
        print(ve)
        mb.showerror('Ошибка', 'Неверные данные')
        ent11.delete(0, END)
        ent12.delete(0, END)
        ent13.delete(0, END)
        ent14.delete(0, END)
        ent151.delete(0, END)
        ent152.delete(0, END)
        return
    ent152g -= 1
    if gm13g == 'Г':
        ent13g *= 12
    tekitog = ent11g
    pop = []
    nugno = 0
    for i in range(ent13g + 1):
        tekmes = mesyaca[(i + ent152g) % 12]
        tekgod = ent151g + (i + ent152g) // 12
        rot1 = tekmes + ' ' + str(tekgod)
        ya = tekitog
        hell = 0
        if gm14g == 'М' or (gm14g == 'Г' and (i + ent152g) % 12 == 0) and i:
            hell = ent14g
            nugno += ent14g
        pluspovk = 0
        if gm12g == 'М' or (gm12g == 'Г' and (i + ent152g) % 12 == ent152g and i):
            pluspovk = round(tekitog * (1 + ent12g / 100) - tekitog, 2)
        tekitog += hell + pluspovk
        nabor = [rot1, round(ya, 2), round(pluspovk, 2), round(hell, 2), round(tekitog, 2)]
        pop += [nabor]
    vlog = round(ent11g + nugno, 2)
    prib = str(round(tekitog - vlog, 2))
    vlog = str(vlog)
    pop += [["Итог: Сумма выросла в " + str(round(tekitog / ent11g, 2)) + " раза",
             'Начальная сумма: ' + str(round(ent11g, 2)), 'Конечная сумма:' + str(round(tekitog, 2)),
             'Вложено денег: ' + vlog,
             'Чистая прибыль: ' + prib]]
    toor = Tk()
    toor.geometry('1400x500')
    tblica = Table(toor, headings=('Дата', 'Текущая сумма', 'Плюс по проценту', 'Пополнение', 'Подитог'), rows=pop)
    tblica.place(x=0, y=0, height=500)


def polpos():
    global provka
    i = 0
    while True:
        try:
            if provka[i][0]:
                texty = ent21.get().upper() + provka[i][1]
            else:
                texty = provka[i][1] + ent21.get().upper()
            actia = yf.Ticker(texty)
            infosh = actia.info
            mops = actia.history(period='max')
            nach = mops.index[0].date()
            kon = mops.index[len(mops.index) - 1].date()
            if ent231.get() or ent232.get() or ent233.get():
                nach = ent231.get() + '-' + ent232.get() + '-' + ent233.get()
            if ent241.get() or ent242.get() or ent243.get():
                kon = ent241.get() + '-' + ent242.get() + '-' + ent243.get()
            data = yf.download(texty, nach, kon)
        except yfinance.base.MyError:
            i += 1
            continue
        except yfinance.base.EmptyCase:
            messagebox.showerror('Ошибка', 'Поле тикера пусто')
            return
        except IndexError:
            messagebox.showerror('Ошибка', 'Нет такого тикера!')
            return
        except ValueError:
            messagebox.showerror('Ошибка', 'Неверные данные')
            return
        break
    pop = []
    tags = [('Название: ', 'Не удается найти название', 'shortName', 'longName'),
            ('Сектор: ', 'Не удается распознать сектор компании', 'sector', 'industry'),
            ('Страна: ', 'Страна не найдена', 'country'),
            ('Город: ', 'Город не найден', 'city'),
            ('Адрес: ', 'Адрес не найден', 'address1'),
            ('Валюта: ', 'Не удалось определить валюту', 'financialCurrency', 'currency'),
            ('Ссылка: ', 'Не удается найти ссылку', 'website')]
    for i in tags:
        try:
            pop.append(i[0] + infosh[i[2]])
        except KeyError:
            if len(i) > 3:
                for el in i[4:]:
                    try:
                        pop.append(i[0] + infosh[el])
                    except KeyError:
                        pass
                    else:
                        break
            else:
                pop.append(i[1])
    a = ''
    for i in pop:
        a += i + '\n'
    scin25.configure(state='normal')
    scin25.delete(1.0, END)
    scin25.insert(INSERT, a)
    scin25.configure(state='disabled')
    figure = Figure(figsize=(11, 5), dpi=100, facecolor=cvfon)
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(data['Adj Close'])
    canvas = FigureCanvasTkAgg(figure, window)
    canvas.get_tk_widget().place(x=bibika * 4 + 25, y=melkash + zolotce * 6 + 80)


slov = ['Калькулятор и графики', 'Приложение для Инвестора(Pro)', 'Золотой инструмент',
        'Карамба', 'Только для крутых!', 'кто прочитал, тот сосиска', 'Не болейте']
pod = 165
sle = 5
wid = 72
c1 = 0
cvfon = '#F8F8FF'
cvcalc1 = '#6CA6CD'
cvcalc2 = '#7EC0EE'
# cvfon = '#F8F8FF'
# cvcalc1 = '#B5B5B5'
# cvcalc2 = '#E8E8E8'
cvkrevk1 = '#FFD373'
cvkrevk2 = '#FFC440'
# cvkrevk1 = '#EEEEE0'
# cvkrevk2 = '#B5B5B5'
# cvkrevk1 = '#C6E2FF'
# vkrevk2 = '#B9D3EE'
greta = 215
bibika = int(round(wid * 1.618, 0))
window = Tk()
window.title(slov[random.randint(0, 4)])
window.geometry('1920x1080')
window.config(bg=cvfon)
calc = Entry(window, justify=RIGHT, font=("Times New Roman", 50), bg=cvcalc1, bd=5)
calc.place(x=5, y=35, width=bibika * 4 + 15, height=125)
var = IntVar()
var.set(2)
inj = Label(window, font=('Comic Sans MS', 12), text='Инженерный калькулятор', bg=cvfon)
inj.place(x=5, y=5)
spin = Spinbox(window, from_=0, to=12, textvariable=var)
spin.place(x=5 + greta, y=5, width=35, height=25)
toch = Label(window, text='Точность', font=('Arial Bond', 12), bg=cvfon)
toch.place(x=45 + greta, y=5)
ochi = Button(window, font=("Times New Roman", 12), text='Очистить', command=ochist)
ochi.place(y=5, x=greta + 120, width=80, height=25)
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='1', command=lambda: type_char('1'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='2', command=lambda: type_char('2'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='3', command=lambda: type_char('3'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg='#6CA6CD', bd=3, text='←', command=lambda: type_char('←'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle = 5
pod += wid + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='4', command=lambda: type_char('4'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='5', command=lambda: type_char('5'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='6', command=lambda: type_char('6'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg='#6CA6CD', bd=3, text='=', command=lambda: type_char('='))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle = 5
pod += wid + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='7', command=lambda: type_char('7'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='8', command=lambda: type_char('8'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='9', command=lambda: type_char('9'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='+', command=lambda: type_char('+'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle = 5
pod += wid + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='.', command=lambda: type_char('.'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='0', command=lambda: type_char('0'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='÷', command=lambda: type_char('/'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='-', command=lambda: type_char('-'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle = 5
pod += wid + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='(', command=lambda: type_char('('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text=')', command=lambda: type_char(')'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='*', command=lambda: type_char('*'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='x**y', command=lambda: type_char('**'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle = 5
pod += wid + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='sin(x)',
             command=lambda: type_char('sin('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='cos(x)',
             command=lambda: type_char('cos('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='tg(x)', command=lambda: type_char('tg('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='ctg(x)',
             command=lambda: type_char('ctg('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle = 5
pod += wid + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='asin(x)',
             command=lambda: type_char('asin('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='acos(x)',
             command=lambda: type_char('acos('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='atg(x)',
             command=lambda: type_char('atg('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='actg(x)',
             command=lambda: type_char('actg('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle = 5
pod += wid + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='√(x)',
             command=lambda: type_char('sqrt('))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='e', command=lambda: type_char('e'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
but = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='pi', command=lambda: type_char('pi'))
but.place(x=sle, y=pod, width=bibika, height=wid)
sle += bibika + 5
rad = Button(window, font=("Times New Roman", 25), bg=cvcalc2, bd=3, text='Rad', command=radonoff)
rad.place(x=sle, y=pod, width=bibika, height=wid)
melkash = -5
zolotce = 40
opiskrevk = Label(window, text='Калькулятор вкладов', bg=cvfon, font=('Comic Sans MS', 12))
opiskrevk.place(x=bibika * 4 + 25, y=5)
ent11 = Entry(font=("Times New Roman", 16), bg=cvkrevk1, bd=4)
ent11.place(x=bibika * 4 + 25, y=melkash + 40, width=zolotce * 6, height=zolotce)
lab11 = Label(font=("Times New Roman", 12), text='Введите сумму вклада', bg=cvfon)
lab11.place(x=bibika * 4 + 25 + zolotce * 6 + 5, y=melkash + 45)
ent12 = Entry(font=("Times New Roman", 16), bg=cvkrevk1, bd=4)
ent12.place(x=bibika * 4 + 25, y=melkash + zolotce + 45, width=zolotce * 6, height=zolotce)
com12 = Combobox(window, state='readonly', values=('М', "Г"), font=('Arial Bond', 16))
com12.place(x=bibika * 4 + 25 + zolotce * 6 + 5, y=melkash + zolotce + 45, width=zolotce, height=zolotce)
com12.current(1)
lab12 = Label(font=("Times New Roman", 12), text='Введите процент по вкладу', bg=cvfon)
lab12.place(x=bibika * 4 + 35 + zolotce * 7, y=melkash + zolotce + 45)
ent13 = Entry(window, font=("Times New Roman", 16), bg=cvkrevk1, bd=4)
ent13.place(x=bibika * 4 + 25, y=melkash + zolotce * 2 + 50, width=zolotce * 6, height=zolotce)
com13 = Combobox(window, state='readonly', values=('М', "Г"), font=('Arial Bond', 16))
com13.place(x=bibika * 4 + 25 + zolotce * 6 + 5, y=melkash + zolotce * 2 + 50, width=zolotce, height=zolotce)
com13.current(1)
lab13 = Label(font=("Times New Roman", 12), text='Введите срок', bg=cvfon)
lab13.place(x=bibika * 4 + 35 + zolotce * 7, y=melkash + zolotce * 2 + 50)
ent14 = Entry(window, font=("Times New Roman", 16), bg=cvkrevk1, bd=4)
ent14.place(x=bibika * 4 + 25, y=melkash + zolotce * 3 + 55, width=zolotce * 6, height=zolotce)
com14 = Combobox(window, state='readonly', values=('М', "Г"), font=('Arial Bond', 16))
com14.place(x=bibika * 4 + 25 + zolotce * 6 + 5, y=melkash + zolotce * 3 + 55, width=zolotce, height=zolotce)
com14.current(1)
lab14 = Label(window, font=("Times New Roman", 12), text='Дополнительное пополнение', bg=cvfon)
lab14.place(x=bibika * 4 + 35 + zolotce * 7, y=melkash + zolotce * 3 + 55)
ent151 = Entry(window, font=("Times New Roman", 16), bg=cvkrevk1, bd=4)
ent151.place(x=bibika * 4 + 25, y=melkash + zolotce * 4 + 60, width=zolotce * 2 + 5, height=zolotce)
lab151 = Label(window, font=("Times New Roman", 25), text='Г', bg=cvfon)
lab151.place(x=bibika * 4 + 25 + zolotce * 2 + 5, y=melkash + zolotce * 4 + 60)
ent152 = Entry(window, font=("Times New Roman", 16), bg=cvkrevk1, bd=4)
ent152.place(x=bibika * 4 + 60 + zolotce * 2, y=melkash + zolotce * 4 + 60, width=zolotce + 5, height=zolotce)
lab152 = Label(window, font=("Times New Roman", 25), text='М', bg=cvfon)
lab152.place(x=bibika * 4 + 70 + zolotce * 3, y=melkash + zolotce * 4 + 60)
lab15 = Label(window, font=("Times New Roman", 12), text='Первая дата взноса', bg=cvfon)
lab15.place(x=bibika * 4 + 125 + zolotce * 3, y=melkash + zolotce * 4 + 60)
but16 = Button(window, text='Подтвердить', font=("Times New Roman", 16), bg=cvkrevk2, command=podtv)
but16.place(x=bibika * 4 + 25, y=melkash + zolotce * 5 + 75, width=zolotce * 6, height=zolotce)
kvadro1 = Button(window, state='disabled', bg='black')
kvadro1.place(x=bibika * 4 + 22, y=0, width=1, height=1200)
kvadro2 = Button(window, state='disabled', bg='black')
kvadro2.place(x=bibika * 4 + 22, y=melkash + zolotce * 6 + 77, width=1200, height=1)
kvadro3 = Button(window, state='disabled', bg='black')
kvadro3.place(x=997, y=0, width=1, height=313)
kra = 42
sil = round(kra * 4.24, 0)
dve = 50
lab2 = Label(window, font=('Comic Sans MS', 12), text='Показатели активов', bg=cvfon)
lab2.place(x=1000, y=5)
ent21 = Entry(window, font=("Times New Roman", 20))
ent21.place(x=1000, y=35, width=sil, height=kra)
ent21.insert(0, 'AAPL')
lab21 = Label(window, font=("Times New Roman", 12), text='Введите _______\nАкции|Облигации|Фонда',
              bg=cvfon)
lab21.place(x=1005 + sil, y=35)
butl21 = Button(window, bd=0, bg=cvfon, font=("Times New Roman", 12), justify=LEFT, text='тикер*',
                command=lambda: webbrowser.open_new('https://vseakcii.ru/issuers/countries'), fg='red',
                cursor='hand2')
butl21.place(x=1103 + sil, y=36, width=45, height=14)
lab22 = Label(window, font=("Times New Roman", 20), text='Введите дату:', bg=cvfon)
lab22.place(x=1000, y=35 + kra + 5)
lab231 = Label(window, font=("Times New Roman", 20), text='От', bg=cvfon)
lab231.place(x=1000, y=45 + kra * 2)
ent231 = Entry(window, font=("Times New Roman", 20))
ent231.place(x=1050, y=45 + kra * 2, width=round(sil * 0.4, 0), height=kra)
ent231.insert(0, '1980')
lab232 = Label(window, font=("Times New Roman", 20), text='Г', bg=cvfon)
lab232.place(x=1126, y=45 + kra * 2)
ent232 = Entry(window, font=("Times New Roman", 20))
ent232.place(x=1156, y=45 + kra * 2, width=36, height=kra)
ent232.insert(0, '01')
lab233 = Label(window, font=("Times New Roman", 20), text='М', bg=cvfon)
lab233.place(x=1197, y=45 + kra * 2)
ent233 = Entry(window, font=("Times New Roman", 20))
ent233.place(x=1227, y=45 + kra * 2, width=36, height=kra)
ent233.insert(0, '01')
lab234 = Label(window, font=("Times New Roman", 20), text='Д', bg=cvfon)
lab234.place(x=1268, y=45 + kra * 2)
lab241 = Label(window, font=("Times New Roman", 20), text='До', bg=cvfon)
lab241.place(x=1000, y=50 + kra * 3)
ent241 = Entry(window, font=("Times New Roman", 20))
ent241.place(x=1050, y=50 + kra * 3, width=round(sil * 0.4, 0), height=kra)
ent241.insert(0, 2021)
lab242 = Label(window, font=("Times New Roman", 20), text='Г', bg=cvfon)
lab242.place(x=1126, y=50 + kra * 3)
ent242 = Entry(window, font=("Times New Roman", 20))
ent242.place(x=1156, y=50 + kra * 3, width=36, height=kra)
ent242.insert(0, 12)
lab243 = Label(window, font=("Times New Roman", 20), text='М', bg=cvfon)
lab243.place(x=1197, y=50 + kra * 3)
ent243 = Entry(window, font=("Times New Roman", 20))
ent243.place(x=1227, y=50 + kra * 3, width=36, height=kra)
ent243.insert(0, 26)
lab244 = Label(window, font=("Times New Roman", 20), text='Д', bg=cvfon)
lab244.place(x=1268, y=50 + kra * 3)
kvadro4 = Button(window, state='disabled', bg='black')
kvadro4.place(x=997, y=47 + kra * 3, width=300, height=1)
kvadro5 = Button(window, state='disabled', bg='black')
kvadro5.place(x=1297, y=42 + kra * 2, width=1, height=kra * 2 + 10)
btn24 = Button(window, font=('Times New Roman', 24), text='Показать\nрезультаты', bd=4, command=polpos)
btn24.place(x=1300, y=45 + kra * 2, width=223, height=kra * 2 + 5)
kvadro6 = Button(window, state='disabled', bg='black')
kvadro6.place(x=998, y=52 + kra * 4, width=1000, height=1)
kvadro7 = Button(window, state='disabled', bg='black')
kvadro7.place(x=998, y=42 + kra * 2, width=1000, height=1)
scin25 = scrolledtext.ScrolledText(window, state='disabled', font=('Times New Roman', 24))
scin25.place(x=1000, y=55 + kra * 4, height=310 - (55 + kra * 4), width=530)
data = yf.download('AAPL', period='max')
figure = Figure(figsize=(11, 5), dpi=100, facecolor=cvfon)
plot = figure.add_subplot(1, 1, 1)
plot.plot(data['Adj Close'])
canvas = FigureCanvasTkAgg(figure, window)
canvas.get_tk_widget().place(x=bibika * 4 + 25, y=melkash + zolotce * 6 + 80)
window.mainloop()
