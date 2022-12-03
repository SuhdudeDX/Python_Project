import numpy as np
import pandas as pd
from scipy.integrate import odeint
import tkinter as tk

root = tk.Tk()
root.geometry('360x380')
root.title('Personal Finance Calculator')


class Life: #main class
    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.grid()
        
        self.incometext = tk.Label(master, text='Income', font=16).grid(row=0, sticky=tk.W)
        self.text1 = tk.Entry(width=15, font = 16)
        self.text1.grid(row=0, column=1, sticky=tk.E)

        self.coststext = tk.Label(master, text='Spending', font=16).grid(row=1, sticky=tk.W)
        self.text2 = tk.Entry(width=15, font = 16)
        self.text2.grid(row=1, column=1, sticky=tk.E)

        self.taxtext = tk.Label(master, text='Tax', font=16).grid(row=2, sticky=tk.W)
        self.text3 = tk.Entry(width=15, font = 16)
        self.text3.grid(row=2, column=1, sticky=tk.E)

        self.startage = tk.Label(master, text='Starting Age', font=16).grid(row=3, sticky=tk.W)
        self.text4 = tk.Entry(width=15, font = 16)
        self.text4.grid(row=3, column=1, sticky=tk.E)

        self.retireage = tk.Label(master, text='Retiring Age', font=16).grid(row=4, sticky=tk.W)
        self.text5 = tk.Entry(width=15, font = 16)
        self.text5.grid(row=4, column=1, sticky=tk.E)

        self.pensiontext = tk.Label(master, text='Pension', font=16).grid(row=5, sticky=tk.W)
        self.text6 = tk.Entry(width=15, font = 16)
        self.text6.grid(row=5, column=1, sticky=tk.E)

        self.Investfractext = tk.Label(master, text='Investment Fraction', font=16).grid(row=6, sticky=tk.W)
        self.text7 = tk.Entry(width=15, font = 16)
        self.text7.grid(row=6, column=1, sticky=tk.E)

        self.lifeinflationtext = tk.Label(master, text='Life Inflation', font=16).grid(row=7, sticky=tk.W)
        self.text8 = tk.Entry(width=15, font = 16)
        self.text8.grid(row=7, column=1, sticky=tk.E)

        self.IRproctext = tk.Label(master, text='Interest Rate', font=16).grid(row=8, sticky=tk.W)
        self.text9 = tk.Entry(width=15, font = 16)
        self.text9.grid(row=8, column=1, sticky=tk.E)

        self.IFproctext = tk.Label(master, text='Inflation Proc', font=16).grid(row=9, sticky=tk.W)
        self.text10 = tk.Entry(width=15, font = 16)
        self.text10.grid(row=9, column=1, sticky=tk.E)

        self.Pay_risetext = tk.Label(master, text='Pay rise', font=16).grid(row=10, sticky=tk.W)
        self.text11 = tk.Entry(width=15, font = 16)
        self.text11.grid(row=10, column=1, sticky=tk.E)

        enterbtn = tk.Button(master, height=1, text='Enter', font=16, command=self.enter) #button
        enterbtn.grid(pady=11, column=1)

    def enter(self):
        self.starting_age = self.text1.get()
        self.retirement_age = self.text2.get()
        self.income = self.text3.get()
        self.tax_rate = self.text4.get()
        self.costs = self.text5.get()
        self.pension = self.text6.get()
        self.life_inflation = self.text7.get()
        self.investment_fraction = self.text8.get()
        self.interest_rate_proc = self.text9.get()
        self.inflation_proc = self.text10.get()
        self.pay_rise = self.text11.get()

        def earn(self, t):
            if t < self.starting_age:
                return 0
            elif self.starting_age <= t < self.retirement_age:
                return 12 * (self.income + self.pay_rise * (t - self.starting_age))
            else:
                return 12 * self.pension


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

def live_without_investing(x, t, you):#no invest
    balance = you.earn(t) - you.spend(t) - you.pay_taxes(t)
    return balance - np.log(1 + 0.01*you.inflation_proc) * x

def live_with_investing(x, t, you):#invest
    balance = you.earn(t) - you.spend(t) - you.pay_taxes(t)
    if t < you.retirement_age:
        x0 = balance * (1 - you.investment_fraction)
        x1 = np.log(1 + 0.01*you.interest_rate_proc) * x[1] + you.investment_fraction * balance
        
        x0 = x0 - np.log(1 + 0.01*you.inflation_proc) * x[0]
        x1 = x1 - np.log(1 + 0.01*you.inflation_proc) * x[1]
    else:
        x0 = balance
        x0 = x0 - np.log(1 + 0.01*you.inflation_proc) * x[0]
        x1 = 0
    return [x0, x1]


def simulate(you): #graphs
    t0 = np.linespace(0, you.starting_age - 1, num=you.starting_age)
    t1 = np.linespace(you.starting_age, you.retirement_age - 1, num=(you.retirement_age - you.starting_age))
    t2 = np.linespace(you.retirement_age, 100, num=(100 - you.retirement_age))

    x0 = np.zeros((t0.shape[0], 1))
    x1 = odeint(live_without_investing, 0, t1, args=(you,))
    x2 = odeint(live_without_investing, x1[-1], t2, args=(you,))

    df0 = pd.DataFrame({'time': t0, 'wallet (non-investor)': x0})
    df1 = pd.DataFrame({'time': t1, 'wallet (non-investor)': x1})
    df2 = pd.DataFrame({'time': t2, 'wallet (non-investor)': x2})
    return pd.concat([df0, df1, df2]) #connect 3 dataframes

you = Life(root)


root.mainloop()




