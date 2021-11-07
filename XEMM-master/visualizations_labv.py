# -- --------------------------------------------------------------------------------------------------- -- #
# -- MarketMaker-BackTest                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: visualizations_labv.py                                                                  -- #
# -- Description: Functions for plots, tables and text visualizations for the project                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: Lizbeth Alejandra Barragán Vázquez                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/labv98/Lab4_LABV.git                                   -- #
# --------------------------------------------------------------------------------------------------------- #

from functions_labv import *
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# PLOT 1

def graf_a(df_a):
    """Función que regresa la serie de gráficas correspondientes a las
    series de tiempo del PRIMER símbolo organizadas en diferentes
    subplots respecto a los exhanges utilizados."""

    # Initialize figure with subplots
    fig = make_subplots(
        rows=3, cols=2,
                        x_title='Fechas',
                        y_title='Cantidad',
                        subplot_titles=("Levels", "Volume_Bid", "Volume_Ask",
                                        "Total_Volume", "Mid_price", "VWAP")
    )

    # Add traces
    # Level
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='ftx'], y=df_a.Levels[df_a['Exchange']=='ftx'], name='ftx-ETH/USD:Level',
                             line=dict(color='slateblue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='kraken'], y=df_a.Levels[df_a['Exchange']=='kraken'], name='kraken-ETH/USD:Level',
                             line=dict(color='orange')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='currencycom'], y=df_a.Levels[df_a['Exchange']=='currencycom'], name='currencycom-ETH/USD:Level',
                             line=dict(color='green')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='coinmate'], y=df_a.Levels[df_a['Exchange']=='coinmate'], name='coinmate-ETH/USD:Level',
                             line=dict(color='salmon')), row=1, col=1)
    # Volume bid
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='ftx'], y=df_a.Volume_bid[df_a['Exchange']=='ftx'], name='ftx-ETH/USD:Volume_bid',
                             line=dict(color='slateblue')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='kraken'], y=df_a.Volume_bid[df_a['Exchange']=='kraken'], name='kraken-ETH/USD:Volume_bid',
                             line=dict(color='orange')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='currencycom'], y=df_a.Volume_bid[df_a['Exchange']=='currencycom'], name='currencycom-ETH/USD:Volume_bid',
                             line=dict(color='green')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='coinmate'], y=df_a.Volume_bid[df_a['Exchange']=='coinmate'], name='coinmate-ETH/USD:Volume_bid',
                             line=dict(color='salmon')), row=1, col=2)
    # Volume_ask
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='ftx'], y=df_a.Volume_ask[df_a['Exchange']=='ftx'], name='ftx-ETH/USD:Volume_ask',
                             line=dict(color='slateblue')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='kraken'], y=df_a.Volume_ask[df_a['Exchange']=='kraken'], name='kraken-ETH/USD:Volume_ask',
                             line=dict(color='orange')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='currencycom'], y=df_a.Volume_ask[df_a['Exchange']=='currencycom'], name='currencycom-ETH/USD:Volume_ask',
                             line=dict(color='green')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='coinmate'], y=df_a.Volume_ask[df_a['Exchange']=='coinmate'], name='coinmate-ETH/USD:Volume_ask',
                             line=dict(color='salmon')), row=2, col=1)
    # Total_vol
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='ftx'], y=df_a.Total_volume[df_a['Exchange']=='ftx'], name='ftx-ETH/USD:Total_volume',
                             line=dict(color='slateblue')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='kraken'], y=df_a.Total_volume[df_a['Exchange']=='kraken'], name='kraken-ETH/USD:Total_volume',
                             line=dict(color='orange')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='currencycom'], y=df_a.Total_volume[df_a['Exchange']=='currencycom'], name='currencycom-ETH/USD:Total_volume',
                             line=dict(color='green')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='coinmate'], y=df_a.Total_volume[df_a['Exchange']=='coinmate'], name='coinmate-ETH/USD:Total_volume',
                             line=dict(color='salmon')), row=2, col=2)
    # Mid price
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='ftx'], y=df_a.Mid_price[df_a['Exchange']=='ftx'], name='ftx-ETH/USD:Mid_price',
                             line=dict(color='slateblue')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='kraken'], y=df_a.Mid_price[df_a['Exchange']=='kraken'], name='kraken-ETH/USD:Mid_price',
                             line=dict(color='orange')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='currencycom'], y=df_a.Mid_price[df_a['Exchange']=='currencycom'], name='currencycom-ETH/USD:Mid_price',
                             line=dict(color='green')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='coinmate'], y=df_a.Mid_price[df_a['Exchange']=='coinmate'], name='coinmate-ETH/USD:Mid_price',
                             line=dict(color='salmon')), row=3, col=1)
    #VWAP
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='ftx'], y=df_a.VWAP[df_a['Exchange']=='ftx'], name='ftx-ETH/USD:VWAP',
                             line=dict(color='slateblue')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='kraken'], y=df_a.VWAP[df_a['Exchange']=='kraken'], name='kraken-ETH/USD:VWAP',
                             line=dict(color='orange')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='currencycom'], y=df_a.VWAP[df_a['Exchange']=='currencycom'], name='currencycom-ETH/USD:VWAP',
                             line=dict(color='green')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_a.Fechas[df_a['Exchange']=='coinmate'], y=df_a.VWAP[df_a['Exchange']=='coinmate'], name='coinmate-ETH/USD:VWAP',
                             line=dict(color='salmon')), row=3, col=2)

    # Update title and height
    fig.update_layout(title_text='ETH/USD', height=700)

    return fig.show()

def graf_b(df_b):
    """Función que regresa la serie de gráficas correspondientes a las
    series de tiempo del PRIMER símbolo organizadas en diferentes
    subplots respecto a los exhanges utilizados."""

    # Initialize figure with subplots
    fig = make_subplots(
        rows=3, cols=2,
                        x_title='Fechas',
                        y_title='Cantidad',
                        subplot_titles=("Levels", "Volume_Bid", "Volume_Ask",
                                        "Total_Volume", "Mid_price", "VWAP")
    )

    # Add traces
    # Level
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='ftx'], y=df_b.Levels[df_b['Exchange']=='ftx'], name='ftx-DOGE/USD:Level',
                             line=dict(color='darkblue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='kraken'], y=df_b.Levels[df_b['Exchange']=='kraken'], name='kraken-DOGE/USD:Level',
                             line=dict(color='seagreen')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='currencycom'], y=df_b.Levels[df_b['Exchange']=='currencycom'], name='currencycom-DOGE/USD:Level',
                             line=dict(color='goldenrod')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='coinmate'], y=df_b.Levels[df_b['Exchange']=='coinmate'], name='coinmate-DOGE/USD:Level',
                             line=dict(color='tomato')), row=1, col=1)
    # Volume bid
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='ftx'], y=df_b.Volume_bid[df_b['Exchange']=='ftx'], name='ftx-DOGE/USD:Volume_bid',
                             line=dict(color='darkblue')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='kraken'], y=df_b.Volume_bid[df_b['Exchange']=='kraken'], name='kraken-DOGE/USD:Volume_bid',
                             line=dict(color='seagreen')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='currencycom'], y=df_b.Volume_bid[df_b['Exchange']=='currencycom'], name='currencycom-DOGE/USD:Volume_bid',
                             line=dict(color='goldenrod')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='coinmate'], y=df_b.Volume_bid[df_b['Exchange']=='coinmate'], name='coinmate-DOGE/USD:Volume_bid',
                             line=dict(color='tomato')), row=1, col=2)
    # Volume_ask
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='ftx'], y=df_b.Volume_ask[df_b['Exchange']=='ftx'], name='ftx-DOGE/USD:Volume_ask',
                             line=dict(color='darkblue')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='kraken'], y=df_b.Volume_ask[df_b['Exchange']=='kraken'], name='kraken-DOGE/USD:Volume_ask',
                             line=dict(color='seagreen')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='currencycom'], y=df_b.Volume_ask[df_b['Exchange']=='currencycom'], name='currencycom-DOGE/USD:Volume_ask',
                             line=dict(color='goldenrod')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='coinmate'], y=df_b.Volume_ask[df_b['Exchange']=='coinmate'], name='coinmate-DOGE/USD:Volume_ask',
                             line=dict(color='tomato')), row=2, col=1)
    # Total_vol
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='ftx'], y=df_b.Total_volume[df_b['Exchange']=='ftx'], name='ftx-DOGE/USD:Total_volume',
                             line=dict(color='darkblue')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='kraken'], y=df_b.Total_volume[df_b['Exchange']=='kraken'], name='kraken-DOGE/USD:Total_volume',
                             line=dict(color='seagreen')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='currencycom'], y=df_b.Total_volume[df_b['Exchange']=='currencycom'], name='currencycom-DOGE/USD:Total_volume',
                             line=dict(color='goldenrod')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='coinmate'], y=df_b.Total_volume[df_b['Exchange']=='coinmate'], name='coinmate-DOGE/USD:Total_volume',
                             line=dict(color='tomato')), row=2, col=2)
    # Mid price
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='ftx'], y=df_b.Mid_price[df_b['Exchange']=='ftx'], name='ftx-DOGE/USD:Mid_price',
                             line=dict(color='darkblue')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='kraken'], y=df_b.Mid_price[df_b['Exchange']=='kraken'], name='kraken-DOGE/USD:Mid_price',
                             line=dict(color='seagreen')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='currencycom'], y=df_b.Mid_price[df_b['Exchange']=='currencycom'], name='currencycom-DOGE/USD:Mid_price',
                             line=dict(color='goldenrod')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='coinmate'], y=df_b.Mid_price[df_b['Exchange']=='coinmate'], name='coinmate-DOGE/USD:Mid_price',
                             line=dict(color='tomato')), row=3, col=1)
    #VWAP
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='ftx'], y=df_b.VWAP[df_b['Exchange']=='ftx'], name='ftx-DOGE/USD:VWAP',
                             line=dict(color='darkblue')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='kraken'], y=df_b.VWAP[df_b['Exchange']=='kraken'], name='kraken-DOGE/USD:VWAP',
                             line=dict(color='seagreen')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='currencycom'], y=df_b.VWAP[df_b['Exchange']=='currencycom'], name='currencycom-DOGE/USD:VWAP',
                             line=dict(color='goldenrod')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_b.Fechas[df_b['Exchange']=='coinmate'], y=df_b.VWAP[df_b['Exchange']=='coinmate'], name='coinmate-DOGE/USD:VWAP',
                             line=dict(color='tomato')), row=3, col=2)

    # Update title and height
    fig.update_layout(title_text='DOGE/USD', height=700)

    return fig.show()

def graf_c(df_c):
    """Función que regresa la serie de gráficas correspondientes a las
    series de tiempo del PRIMER símbolo organizadas en diferentes
    subplots respecto a los exhanges utilizados."""

    # Initialize figure with subplots
    fig = make_subplots(
        rows=3, cols=2,
                        x_title='Fechas',
                        y_title='Cantidad',
                        subplot_titles=("Levels", "Volume_Bid", "Volume_Ask",
                                        "Total_Volume", "Mid_price", "VWAP")
    )

    # Add traces
    # Level
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='ftx'], y=df_c.Levels[df_c['Exchange']=='ftx'], name='ftx-SOL/USD:Level',
                             line=dict(color='indigo')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='kraken'], y=df_c.Levels[df_c['Exchange']=='kraken'], name='kraken-SOL/USD:Level',
                             line=dict(color='violet')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='currencycom'], y=df_c.Levels[df_c['Exchange']=='currencycom'], name='currencycom-SOL/USD:Level',
                             line=dict(color='gold')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='coinmate'], y=df_c.Levels[df_c['Exchange']=='coinmate'], name='coinmate-SOL/USD:Level',
                             line=dict(color='sienna')), row=1, col=1)
    # Volume bid
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='ftx'], y=df_c.Volume_bid[df_c['Exchange']=='ftx'], name='ftx-SOL/USD:Volume_bid',
                             line=dict(color='indigo')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='kraken'], y=df_c.Volume_bid[df_c['Exchange']=='kraken'], name='kraken-SOL/USD:Volume_bid',
                             line=dict(color='violet')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='currencycom'], y=df_c.Volume_bid[df_c['Exchange']=='currencycom'], name='currencycom-SOL/USD:Volume_bid',
                             line=dict(color='gold')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='coinmate'], y=df_c.Volume_bid[df_c['Exchange']=='coinmate'], name='coinmate-SOL/USD:Volume_bid',
                             line=dict(color='sienna')), row=1, col=2)
    # Volume_ask
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='ftx'], y=df_c.Volume_ask[df_c['Exchange']=='ftx'], name='ftx-SOL/USD:Volume_ask',
                             line=dict(color='indigo')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='kraken'], y=df_c.Volume_ask[df_c['Exchange']=='kraken'], name='kraken-SOL/USD:Volume_ask',
                             line=dict(color='violet')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='currencycom'], y=df_c.Volume_ask[df_c['Exchange']=='currencycom'], name='currencycom-SOL/USD:Volume_ask',
                             line=dict(color='gold')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='coinmate'], y=df_c.Volume_ask[df_c['Exchange']=='coinmate'], name='coinmate-SOL/USD:Volume_ask',
                             line=dict(color='sienna')), row=2, col=1)
    # Total_vol
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='ftx'], y=df_c.Total_volume[df_c['Exchange']=='ftx'], name='ftx-SOL/USD:Total_volume',
                             line=dict(color='indigo')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='kraken'], y=df_c.Total_volume[df_c['Exchange']=='kraken'], name='kraken-SOL/USD:Total_volume',
                             line=dict(color='violet')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='currencycom'], y=df_c.Total_volume[df_c['Exchange']=='currencycom'], name='currencycom-SOL/USD:Total_volume',
                             line=dict(color='gold')), row=2, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='coinmate'], y=df_c.Total_volume[df_c['Exchange']=='coinmate'], name='coinmate-SOL/USD:Total_volume',
                             line=dict(color='sienna')), row=2, col=2)
    # Mid price
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='ftx'], y=df_c.Mid_price[df_c['Exchange']=='ftx'], name='ftx-SOL/USD:Mid_price',
                             line=dict(color='indigo')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='kraken'], y=df_c.Mid_price[df_c['Exchange']=='kraken'], name='kraken-SOL/USD:Mid_price',
                             line=dict(color='violet')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='currencycom'], y=df_c.Mid_price[df_c['Exchange']=='currencycom'], name='currencycom-SOL/USD:Mid_price',
                             line=dict(color='gold')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='coinmate'], y=df_c.Mid_price[df_c['Exchange']=='coinmate'], name='coinmate-SOL/USD:Mid_price',
                             line=dict(color='sienna')), row=3, col=1)
    #VWAP
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='ftx'], y=df_c.VWAP[df_c['Exchange']=='ftx'], name='ftx-SOL/USD:VWAP',
                             line=dict(color='indigo')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='kraken'], y=df_c.VWAP[df_c['Exchange']=='kraken'], name='kraken-SOL/USD:VWAP',
                             line=dict(color='violet')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='currencycom'], y=df_c.VWAP[df_c['Exchange']=='currencycom'], name='currencycom-SOL/USD:VWAP',
                             line=dict(color='gold')), row=3, col=2)
    fig.add_trace(go.Scatter(x=df_c.Fechas[df_c['Exchange']=='coinmate'], y=df_c.VWAP[df_c['Exchange']=='coinmate'], name='coinmate-SOL/USD:VWAP',
                             line=dict(color='sienna')), row=3, col=2)

    # Update title and height
    fig.update_layout(title_text='SOL/USD', height=700)

    return fig.show()