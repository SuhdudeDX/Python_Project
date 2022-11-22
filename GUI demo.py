import numpy as np
import pandas as pd
from scipy.integrate import odeint
import tkinter as tk

root = tk.Tk()

e = ""

def enter():
    a = text1.get()
    print(a)
    b = text2.get()
    print(b)
    c = text3.get()
    print(c)
    d = text4.get()
    print(d)
    e = text5.get()
    print(e)
    f = text6.get()
    print(f)
    g = text7.get()
    print(g)
    h = text8.get()
    print(h)
    

root.geometry('300x300')
root.title('Personal Finance Calculator')


incometext = tk.Label(root, text='Income', font=16).grid(row=0, sticky=tk.W)
text1 = tk.Entry(width=15, font = 16)
text1.grid(row=0, column=1, sticky=tk.E)

coststext = tk.Label(root, text='Spending', font=16).grid(row=1, sticky=tk.W)
text2 = tk.Entry(width=15, font = 16)
text2.grid(row=1, column=1, sticky=tk.E)

taxtext = tk.Label(root, text='Tax', font=16).grid(row=2, sticky=tk.W)
text3 = tk.Entry(width=15, font = 16)
text3.grid(row=2, column=1, sticky=tk.E)

pensiontext = tk.Label(root, text='Pension', font=16).grid(row=3, sticky=tk.W)
text4 = tk.Entry(width=15, font = 16)
text4.grid(row=3, column=1, sticky=tk.E)

Investfractext = tk.Label(root, text='Investment Fraction', font=16).grid(row=4, sticky=tk.W)
text5 = tk.Entry(width=15, font = 16)
text5.grid(row=4, column=1, sticky=tk.E)

lifeinflationtext = tk.Label(root, text='Life Inflation', font=16).grid(row=5, sticky=tk.W)
text6 = tk.Entry(width=15, font = 16)
text6.grid(row=5, column=1, sticky=tk.E)

IRproctext = tk.Label(root, text='Interest Rate', font=16).grid(row=6, sticky=tk.W)
text7 = tk.Entry(width=15, font = 16)
text7.grid(row=6, column=1, sticky=tk.E)

IFproctext = tk.Label(root, text='Inflation Proc', font=16).grid(row=7, sticky=tk.W)
text8 = tk.Entry(width=15, font = 16)
text8.grid(row=7, column=1, sticky=tk.E)

enterbtn = tk.Button(root, height=1, text='Enter', font=16, command=enter)
enterbtn.grid(pady=10, column=1)


root.mainloop()




