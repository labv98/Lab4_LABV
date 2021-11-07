# -- --------------------------------------------------------------------------------------------------- -- #
# -- Función para leer datos y trabajar en ellos                                                        -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: functions_labv.py                                                                              -- #
# -- Description: Function execution logic for the project                                          -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: Lizbeth Aljandra Barragán Vázquez                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/labv98/Lab4_LABV.git                                 -- #
# --------------------------------------------------------------------------------------------------------- #


import pandas as pd

def currency_a(data_a, exchanges):
    """Esta función regresa el diccionario con la información
     extraída de ccxt para el PRIMER símbolo.
     De este modo, podremos ver y analizar los cambios
     que presentan las serie de tiempo correspondientes."""

    # Ciclo de diccionario
    dictionary_a = {'Exchange': [],
                  'Fechas': [],
                  'Levels': [],
                  'Volume_ask': [],
                  'Volume_bid': [],
                  'Total_volume': [],
                  'Mid_price': [],
                  'VWAP': []
                  }

    for exchange in exchanges:
        for i in list(data_a[exchange].keys()):
            # Exchange
            ex = exchange
            dictionary_a['Exchange'].append(ex)
            # Timestamp
            fecha = i
            keys = pd.DataFrame(data_a[exchange][i])
            dictionary_a['Fechas'].append(fecha)
            # Levels
            level = len(keys)
            dictionary_a['Levels'].append(level)
            # Asks y Bids volumes
            volume_bid = keys['bid_size'].sum()
            volume_ask = keys['ask_size'].sum()
            dictionary_a['Volume_bid'].append(volume_bid)
            dictionary_a['Volume_ask'].append(volume_ask)
            # Total volume
            volume = volume_bid + volume_ask
            dictionary_a['Total_volume'].append(volume)
            # Midprice
            midprice = (keys['ask'][0] + keys['bid'][0]) / 2
            dictionary_a['Mid_price'].append(midprice)
            # VWAP
            vwap_ask = (keys['ask'] * keys['ask_size']).sum() / keys['ask_size'].sum()
            vwap_bid = (keys['bid'] * keys['bid_size']).sum() / keys['bid_size'].sum()
            vwap = (vwap_ask + vwap_bid) / 2
            dictionary_a['VWAP'].append(vwap)

    return dictionary_a

def currency_b(data_b, exchanges):
    """Esta función regresa el diccionario con la información
     extraída de ccxt para el SEGUNDO símbolo.
     De este modo, podremos ver y analizar los cambios
     que presentan las serie de tiempo correspondientes."""

    # Ciclo de diccionario
    dictionary_b = {'Exchange': [],
                  'Fechas': [],
                  'Levels': [],
                  'Volume_ask': [],
                  'Volume_bid': [],
                  'Total_volume': [],
                  'Mid_price': [],
                  'VWAP': []
                  }

    for exchange in exchanges:
        for i in list(data_b[exchange].keys()):
            # Exchange
            ex = exchange
            dictionary_b['Exchange'].append(ex)
            # Timestamp
            fecha = i
            keys = pd.DataFrame(data_b[exchange][i])
            dictionary_b['Fechas'].append(fecha)
            # Levels
            level = len(keys)
            dictionary_b['Levels'].append(level)
            # Asks y Bids volumes
            volume_bid = keys['bid_size'].sum()
            volume_ask = keys['ask_size'].sum()
            dictionary_b['Volume_bid'].append(volume_bid)
            dictionary_b['Volume_ask'].append(volume_ask)
            # Total volume
            volume = volume_bid + volume_ask
            dictionary_b['Total_volume'].append(volume)
            # Midprice
            midprice = (keys['ask'][0] + keys['bid'][0]) / 2
            dictionary_b['Mid_price'].append(midprice)
            # VWAP
            vwap_ask = (keys['ask'] * keys['ask_size']).sum() / keys['ask_size'].sum()
            vwap_bid = (keys['bid'] * keys['bid_size']).sum() / keys['bid_size'].sum()
            vwap = (vwap_ask + vwap_bid) / 2
            dictionary_b['VWAP'].append(vwap)

    return dictionary_b

def currency_c(data_c, exchanges):
    """Esta función regresa el diccionario con la información
     extraída de ccxt para el TERCER símbolo.
     De este modo, podremos ver y analizar los cambios
     que presentan las serie de tiempo correspondientes."""

    # Ciclo de diccionario
    dictionary_c = {'Exchange': [],
                  'Fechas': [],
                  'Levels': [],
                  'Volume_ask': [],
                  'Volume_bid': [],
                  'Total_volume': [],
                  'Mid_price': [],
                  'VWAP': []
                  }

    for exchange in exchanges:
        for i in list(data_c[exchange].keys()):
            # Exchange
            ex = exchange
            dictionary_c['Exchange'].append(ex)
            # Timestamp
            fecha = i
            keys = pd.DataFrame(data_c[exchange][i])
            dictionary_c['Fechas'].append(fecha)
            # Levels
            level = len(keys)
            dictionary_c['Levels'].append(level)
            # Asks y Bids volumes
            volume_bid = keys['bid_size'].sum()
            volume_ask = keys['ask_size'].sum()
            dictionary_c['Volume_bid'].append(volume_bid)
            dictionary_c['Volume_ask'].append(volume_ask)
            # Total volume
            volume = volume_bid + volume_ask
            dictionary_c['Total_volume'].append(volume)
            # Midprice
            midprice = (keys['ask'][0] + keys['bid'][0]) / 2
            dictionary_c['Mid_price'].append(midprice)
            # VWAP
            vwap_ask = (keys['ask'] * keys['ask_size']).sum() / keys['ask_size'].sum()
            vwap_bid = (keys['bid'] * keys['bid_size']).sum() / keys['bid_size'].sum()
            vwap = (vwap_ask + vwap_bid) / 2
            dictionary_c['VWAP'].append(vwap)

    return dictionary_c
