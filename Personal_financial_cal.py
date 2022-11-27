import numpy as np
import pandas as pd
from scipy.integrate import odeint
import tkinter as tk

class Life: #main class for the project
    def __init__(self, income, costs, tax_rate, pension, starting_age, retirement_age, life_inflation, investment_fraction, interest_rate_proc, inflation_proc):
        self.starting_age = starting_age
        self.retirement_age = retirement_age
        self.income = income
        self.tax_rate = tax_rate
        self.costs = costs
        self.pension = pension
        self.life_inflation = life_inflation
        self.investment_fraction = investment_fraction
        self.interest_rate_proc = interest_rate_proc
        self.inflation_proc = inflation_proc


    def earn(self, t):
        if t < self.starting_age:
            return 0
        elif self.starting_age <= t < self.retirement_age:
            return 12 * (self.income + self.pay_rise * (t - self.starting_age))
        else:
            return 12 * self.pension

    def spend(self, t):
        if (t < self.starting_age):
            return 0
        return 12 * (self.costs + self.life_inflation * (t - self.starting_age))

    def pay_taxes(self, t):
        return self.earn(t) * self.tax_rate

    
def live_without_investing(x, t, you):
    return you.earn(t) - you.spend(t) - you.pay_taxes(t)

def simulate(you):
    t0 = np.linespace(0, you.starting_age - 1, num=you.starting_age)
    t1 = np.linespace(you.starting_age, you.retirement_age - 1, num=(you.retirement_age - you.starting_age))
    t2 = np.linespace(you.retirement_age, 100, num=(100 - you.retirement_age))

    x0 = np.zeros((t0.shape[0], 1))
    x1 = odeint(live_without_investing, 0, t1, args=(you,))
    x2 = odeint(live_without_investing, x1[-1], t2, args=(you,))

    df0 = pd.DataFrame({'time': t0, 'wallet (non-investor)': x0})
    df1 = pd.DataFrame({'time': t1, 'wallet (non-investor)': x1})
    df2 = pd.DataFrame({'time': t2, 'wallet (non-investor)': x2})
    return pd.concat([df0, df1, df2])


root = tk.Tk()

def enter(): #get the inputs from GUI and return it
    a = text1.get()
    b = text2.get()
    c = text3.get()
    d = text4.get()
    e = text5.get()
    f = text6.get()
    g = text7.get()
    h = text8.get()
    i = text9.get()
    j = text10.get()
    you = Life(a, b, c, d, e, f, g, h, i, j)
    return you

root.geometry('350x350')
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

startage = tk.Label(root, text='Starting Age', font=16).grid(row=3, sticky=tk.W)
text4 = tk.Entry(width=15, font = 16)
text4.grid(row=3, column=1, sticky=tk.E)

retireage = tk.Label(root, text='Retiring Age', font=16).grid(row=4, sticky=tk.W)
text5 = tk.Entry(width=15, font = 16)
text5.grid(row=4, column=1, sticky=tk.E)

pensiontext = tk.Label(root, text='Pension', font=16).grid(row=5, sticky=tk.W)
text6 = tk.Entry(width=15, font = 16)
text6.grid(row=5, column=1, sticky=tk.E)

Investfractext = tk.Label(root, text='Investment Fraction', font=16).grid(row=6, sticky=tk.W)
text7 = tk.Entry(width=15, font = 16)
text7.grid(row=6, column=1, sticky=tk.E)

lifeinflationtext = tk.Label(root, text='Life Inflation', font=16).grid(row=7, sticky=tk.W)
text8 = tk.Entry(width=15, font = 16)
text8.grid(row=7, column=1, sticky=tk.E)

IRproctext = tk.Label(root, text='Interest Rate', font=16).grid(row=8, sticky=tk.W)
text9 = tk.Entry(width=15, font = 16)
text9.grid(row=8, column=1, sticky=tk.E)

IFproctext = tk.Label(root, text='Inflation Proc', font=16).grid(row=9, sticky=tk.W)
text10 = tk.Entry(width=15, font = 16)
text10.grid(row=9, column=1, sticky=tk.E)

enterbtn = tk.Button(root, height=1, text='Enter', font=16, command=enter)
enterbtn.grid(pady=10, column=1)


root.mainloop()

you = Life()
df = simulate(you)

