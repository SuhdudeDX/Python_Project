import numpy as np
import pandas as pd
from scipy.integrate import odeint

class Life:
    def __init__(self, income, tax_rate, spending, pension, starting_age, retirement_age):
        self.income = income
        self.tax_rate = tax_rate
        self.spending = spending
        self.pension = pension
        self.starting_age = starting_age
        self.retirement_age = retirement_age

    def earn(self, t):
        if t < self.starting_age:
            return 0
        elif self.starting_age <= t < self.retirement_age:
            return 12 * self.income
        else:
            return 12 * self.pension

    def spend(self, t):
        return 12 * self.spending

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

