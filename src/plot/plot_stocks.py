import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt



def plot_stocks(stock_one, stock_two):
    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.plot(stock_one.index, stock_one["Adj Close"])
    ax2.plot(stock_two.index, stock_two["Adj Close"], color="orange")

    ax1.set_ylabel("Stock 1", color="blue")
    ax2.set_ylabel("Stock 2", color="orange")
    print("Saving historical stock price chart to stocks-correlation.png in the current folder...")
    plt.savefig("stock-correlation.png")
