import numpy as np
import pandas as pd
from scipy.integrate import odeint

class Life:
    def __init__(self):
        self.income = 1000
        self.tax_rate = 0.19
        self.spending = 650