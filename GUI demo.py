import numpy as np
import pandas as pd
from scipy.integrate import odeint
import tkinter as tk

root = tk.Tk()

root.geometry('300x300')
root.title('Personal Finance Calculator')


incometext = tk.Label(root, text='Income', font=16).grid(row=0, sticky=tk.W)
text1 = tk.Text(width=15, height=1, font = 16)
text1.grid(row=0, column=1, sticky=tk.E)

coststext = tk.Label(root, text='Spending', font=16).grid(row=1, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=1, column=1, sticky=tk.E)

taxtext = tk.Label(root, text='Tax', font=16).grid(row=2, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=2, column=1, sticky=tk.E)

pensiontext = tk.Label(root, text='Pension', font=16).grid(row=3, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=3, column=1, sticky=tk.E)

Investfractext = tk.Label(root, text='Investment Fraction', font=16).grid(row=4, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=4, column=1, sticky=tk.E)

lifeinflationtext = tk.Label(root, text='Life Inflation', font=16).grid(row=5, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=5, column=1, sticky=tk.E)

IRproctext = tk.Label(root, text='Interest Rate', font=16).grid(row=6, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=6, column=1, sticky=tk.E)

IFproctext = tk.Label(root, text='Inflation Proc', font=16).grid(row=7, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=7, column=1, sticky=tk.E)

enterbtn = tk.Button(root, height=1, text='Enter', font=16)
enterbtn.grid(pady=10, column=1)



root.mainloop()

