import datetime
import quandl


# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()

# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date

def get_stock_data(name = 'AAPL', start = datetime.datetime(2017, 1, 1), end=datetime.date.today()):
    stock = quandl.get("WIKI/" + name, start_date=start, end_date=end)
    return stock