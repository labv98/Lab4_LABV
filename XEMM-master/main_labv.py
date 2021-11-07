import pandas as pd
from data import order_book
from functions_labv import *

# Small test
exchanges = ["ftx", "kraken", "currencycom", "coinmate"]
symbol = 'BTC/EUR'
expected_volume = 0

# Massive download of OrderBook data
data = order_book(symbol=symbol, exchanges=exchanges, output='inplace', stop=None, verbose=True)

# Data
print(currency(data, exchanges))
