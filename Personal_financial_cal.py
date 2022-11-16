import numpy as np
import pandas as pd
from scipy.integrate import odeint

class Life:
    def __init__(self):
        self.income = 1000
        self.tax_rate = 0.19
        self.spending = 650

    def earn(self, t):
        return 12 * self.income

    def spend(self, t):
        return 12 * self.spending

    def pay_taxes(self, t):
        return self.earn(t) * self.tax_rate
    
def live_without_investing(x, t, you):
    return you.earn(t) - you.spend(t) - you.pay_taxes(t)

def simulate(you):
    t = np.linspace(0, 100, num=101)
    x = odeint(live_without_investing, 0, t, args=(you,))
    return pd.DataFrame({'time': t, 'wallet (non-investor)': x})


you = Life()
df = simulate(you)