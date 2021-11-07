# -- --------------------------------------------------------------------------------------------------- -- #
# -- MarketMaker-BackTest                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: main_labv.py                                                                              -- #
# -- Description: Main execution logic for the project                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: Lizbeth Aljandra Barragán Vázquez                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/labv98/Lab4_LABV.git                                 -- #
# --------------------------------------------------------------------------------------------------------- #

# Librerías
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
df = currency(data, exchanges)
print(df)


#Figures

fig = go.Figure()

time = df[df["Fechas"].to_list()]

# ftx
ftx = df[df['Exchanges']=='ftx']




values = currency(data, exchanges)["Levels"].to_list()

# Create and style traces
fig.add_trace(go.Scatter(x=time, y=values, name='Levels',
                         line=dict(color='firebrick', width=4)))
