import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf



DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self):
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.to_datetime(data.index)
        self.calc_returns(data)
        return data


    def calc_returns(self, data):
        data['change'] = data['Close'].diff()
        data['instant_return'] = np.log(data['Close']).diff().round(4)
        pass

    
    def plot_return_dist(self):
        plt.figure(figsize=(10, 6))
        self.data['instant_return'].hist(bins=20, color='orange', edgecolor='black', alpha=0.7)
        plt.title('Instantaneous Returns Distribution')
        plt.xlabel('Instantaneous Returns')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()


    def plot_performance(self):
        plt.figure(figsize=(10, 6))
        self.data['Close'].plot(color='purple', alpha=0.7)
        plt.title('Stock Performance')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.grid(True)
        plt.show()
                  

def main():
    try:
        stksym = "DIS"
        test = Stock(symbol=[stksym])
        print(test.data)
        test.plot_performance()
        test.plot_return_dist()
    except Exception as e:
        print("Error occurred:", e)

if __name__ == '__main__':
    main()