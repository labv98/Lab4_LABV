import pandas as pd
from data import order_book

def currency(data, exchanges):

    # Ciclo de diccionario
    dictionary = {'Exchange': [],
                  'Fechas': [],
                  'Levels': [],
                  'Volume_ask': [],
                  'Volume_bid': [],
                  'Total_volume': [],
                  'Mid_price': [],
                  'VWAP': []
                  }

    for exchange in exchanges:
        for i in list(data[exchange].keys()):
            # Exchange
            ex = exchange
            dictionary['Exchange'].append(ex)
            # Timestamp
            fecha = i
            keys = pd.DataFrame(data[exchange][i])
            dictionary['Fechas'].append(fecha)
            # Levels
            level = len(keys)
            dictionary['Levels'].append(level)
            # Asks y Bids volumes
            volume_bid = keys['bid_size'].sum()
            volume_ask = keys['ask_size'].sum()
            dictionary['Volume_bid'].append(volume_bid)
            dictionary['Volume_ask'].append(volume_ask)
            # Total volume
            volume = volume_bid + volume_ask
            dictionary['Total_volume'].append(volume)
            # Midprice
            midprice = (keys['ask'][0] + keys['bid'][0]) / 2
            dictionary['Mid_price'].append(midprice)
            # VWAP
            vwap_ask = (keys['ask'] * keys['ask_size']).sum() / keys['ask_size'].sum()
            vwap_bid = (keys['bid'] * keys['bid_size']).sum() / keys['bid_size'].sum()
            vwap = (vwap_ask + vwap_bid) / 2
            dictionary['VWAP'].append(vwap)

    df = pd.DataFrame(dictionary)
    return df
