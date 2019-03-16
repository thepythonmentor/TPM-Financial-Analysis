from GetData.read_data import get_stock_data

Amazon = get_stock_data('AMZN')

print(type(Amazon))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(Amazon.head())

Amazon.Open.describe()


fit = np.polyfit(pd.to_numeric(Amazon.index),Amazon.Open, deg=1)

y = np.polyval(fit, pd.to_numeric(Amazon.index))

plt.plot(Amazon.index, y)
plt.plot(Amazon.index, Amazon.Open)

