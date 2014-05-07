import pandas as pd
import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt

import utils.simpleCals as sc


ts = pd.Series(randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

ts.plot(style='b--')


MA10 = sc.movingAverage(ts, 10)
MA20 = sc.movingAverage(ts, 20)

MA10.plot(style='k')
MA20.plot(style='r')

plt.show()

MA10 = MA10[20:999]
MA20 = MA20[20:999]

