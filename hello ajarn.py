import numpy as np
import pandas as pd
from scipy.integrate import odeint
import tkinter as tk

root = tk.Tk()

root.geometry('500x300')
root.title('Personal Finance Calculator')


incometext = tk.Label(root, text='Income', font=16).grid(row=0, sticky=tk.W)
text1 = tk.Text(width=15, height=1, font = 16)
text1.grid(row=0, column=1, sticky=tk.E)

spendtext = tk.Label(root, text='Spending', font=16).grid(row=1, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=1, column=1, sticky=tk.E)

taxtext = tk.Label(root, text='Tax', font=16).grid(row=2, sticky=tk.W)
text2 = tk.Text(width=15, height=1, font = 16)
text2.grid(row=2, column=1, sticky=tk.E)

enterbtn = tk.Button(root, height=1, text='Enter', font=16)
enterbtn.grid(pady=10, column=1)



root.mainloop()

