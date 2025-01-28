from nsepy import get_history
import yfinance as yf
from datetime import date
import pandas as pd

def fetch_nse_data(symbol, start_date, end_date):
    return get_history(
        symbol=symbol,
        start=start_date,
        end=end_date,
        index=True
    )

def fetch_yfinance_data(ticker):
    return yf.download(ticker)
