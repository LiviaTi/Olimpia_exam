# tools/yahoo_finance.py

import yfinance as yf
from typing import Dict


def get_stock_price(ticker: str) -> Dict:
    """
    Retrieve latest stock price using Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    info = stock.fast_info

    return {
        "ticker": ticker,
        "currency": info.get("currency", "BRL"),
        "price": float(info.get("last_price")),
        "last_update": None
    }
