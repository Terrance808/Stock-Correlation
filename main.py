import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import numpy as np


start = dt.datetime(2022, 1, 1)
end = dt.datetime(2022, 12, 31)

FIRST_TICK = 'QQQ'
SECOND_TICK = 'BITO'


stock_1 = web.DataReader(FIRST_TICK, 'yahoo', start, end)

stock_2 = web.DataReader(SECOND_TICK, 'yahoo', start, end)

corrcoef_matrix = np.corrcoef(stock_1['Close'], stock_2['Close'])
r = corrcoef_matrix[0, 1]
r_sq = r ** 2
print("R = ", r)
print("R2 = ", r_sq)


fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(stock_1.index, stock_1["Adj Close"])
ax2.plot(stock_2.index, stock_2["Adj Close"], color="orange")


ax1.set_ylabel("Stock 1", color="blue")
ax2.set_ylabel("Stock 2", color="orange")




plt.show()
