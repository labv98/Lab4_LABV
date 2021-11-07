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
import pickle
from functions_labv import *

# Small test
exchanges = ["kraken", "ftx", "coinmate"]  #,"currencycom"
symbol_a = 'ETH/USD'
symbol_b = 'DOGE/USD'
symbol_c = 'SOL/USD'
expected_volume = 0

# Massive download of OrderBook data
data_a = order_book(symbol=symbol_a, exchanges=exchanges, output='inplace', stop=None, verbose=True)
data_b = order_book(symbol=symbol_b, exchanges=exchanges, output='inplace', stop=None, verbose=True)
data_c = order_book(symbol=symbol_c, exchanges=exchanges, output='inplace', stop=None, verbose=True)

# Diccionario a
dic_a = currency_a(data_a, exchanges)
dic_file_a = open("dic_a.pkl", "wb")
pickle.dump(dic_a, dic_file_a)
dic_file_a.close()

# Diccionario b
dic_b = currency_b(data_b, exchanges)
dic_file_b = open("dic_b.pkl", "wb")
pickle.dump(dic_b, dic_file_b)
dic_file_b.close()

# Diccionario c
dic_c = currency_c(data_c, exchanges)
dic_file_c = open("dic_c.pkl", "wb")
pickle.dump(dic_c, dic_file_c)
dic_file_c.close()

# DataFrame a
df_a = pd.DataFrame(dic_a)
print(df_a)
df_a.to_pickle("df_final_a.pkl")

# DataFrame b
df_b = pd.DataFrame(dic_b)
print(df_b)
df_b.to_pickle("df_final_b.pkl")

# DataFrame a
df_c = pd.DataFrame(dic_c)
print(df_c)
df_c.to_pickle("df_final_c.pkl")
