import pandas as pd
from data import fees_schedule, order_book

# Small test
exchanges = ["ftx", "kraken", "currencycom", "coinmate"]
symbol = 'BTC/EUR'
expected_volume = 0

for exchange in exchanges:
    for i in list(data[exchange].keys())[i]:
        tmp = list(data[exchange].keys())[i]
        {
            'exchange': exchange,
            'fecha': timeStamp,
            'levels': len(data[exchange][timeStamp]),
            'volume_ask': sum(data[exchange][timeStamp].ask_size),
            'volume_bid': sum(data[exchange][timeStamp].bid_size),

        }