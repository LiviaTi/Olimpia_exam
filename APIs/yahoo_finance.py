# APIs/yahoo_finance.py

import yfinance as yf
from typing import Dict

def get_stock_price(ticker: str) -> Dict:
    """
    Retrieve latest stock price using Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    
    # fast_info é um objeto, não um dicionário.
    # O acesso deve ser feito via atributos (ex: .last_price).
    info = stock.fast_info

    try:
        # Tenta pegar o preço atualizado via fast_info (mais rápido)
        price = info.last_price
        currency = info.currency
    except AttributeError:
        # Fallback caso fast_info falhe ou mude de estrutura
        # (stock.info é mais lento, mas é um dicionário tradicional)
        price = stock.info.get('currentPrice') or stock.info.get('regularMarketPrice')
        currency = stock.info.get('currency', 'BRL')

    return {
        "ticker": ticker,
        "currency": currency,
        "price": float(price) if price else 0.0,
        "last_update": None
    }