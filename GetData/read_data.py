import datetime
import quandl

def get_stock_data(name = 'AAPL', start = datetime.datetime(2017, 1, 1), end=datetime.date.today()):
    stock = quandl.get("WIKI/" + name, start_date=start, end_date=end)
    return stock