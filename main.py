import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

""")

# Defining Ticker Symbol
tickerSymbol = 'GOOGL'

# Get Data Down on This Ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)