import datetime as dt
import pandas_datareader.data as pdr
import yfinance as yf
import numpy as np
from plot.plot_stocks import plot_stocks


def get_date(date_type):
    while True:
        try:
            # Set the prompt based on the value of date_type
            if date_type == "start":
                prompt = "Enter the start date (YYYY/MM/DD): "
            elif date_type == "end":
                prompt = "Enter the end date (YYYY/MM/DD): "
            else:
                raise ValueError("Invalid date type. Please specify 'start' or 'end'.")

            year, month, day = map(int, input(prompt).split('/'))

            # Use the datetime function from the datetime module to create a date object
            date = dt.datetime(year, month, day)
            print(f"The {date_type} date is: {date}")
            return date
        except ValueError:
            print("Invalid date. Please try again.")


def get_stock(stock_number, start, end):
    while True:
        yf.pdr_override()  # Work-around while pdr.DataReader() has a bug
        try:
            # Set the prompt based on the value of stock_number
            if stock_number == "first":
                prompt = "Please enter the first stock: "
            elif stock_number == "second":
                prompt = "Please enter the second stock: "
            else:
                raise ValueError("Invalid stock order. Please specify 'first' or 'second'.")

            stock_ticker = str(input(prompt)).upper()

            stock_data = pdr.DataReader(stock_ticker, start, end)
            print(f"The {stock_number} stock ticker is: {stock_ticker}")
            return stock_data
        except ValueError:
            # If a ValueError is raised (e.g. invalid month or day), print an error message and continue the loop
            print(f"Invalid stock ticker. Please try again.")


start_date = get_date("start")
end_date = get_date("end")
print()


stock_1 = get_stock("first", start_date, end_date)
stock_2 = get_stock("second", start_date, end_date)
print()

corrcoef_matrix = np.corrcoef(stock_1['Close'], stock_2['Close'])
r = corrcoef_matrix[0, 1]
r_sq = r ** 2
print("R =", r)
print("R2 =", r_sq)
print()

plot_stocks(stock_1, stock_2)
