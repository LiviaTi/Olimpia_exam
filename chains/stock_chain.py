# chains/stock_chain.py

from tools.yahoo_finance import get_stock_price

COMPANY_TICKERS = {
    "Petrobras": "PETR4.SA",
    "Vale": "VALE3.SA",
    "Itau": "ITUB4.SA",
    "Ambev": "ABEV3.SA",
    "Minerva": "BEEF3.SA"
}


def get_company_stock_price(company_name: str) -> dict:
    """
    Resolve company name to ticker and return stock price.
    """
    ticker = COMPANY_TICKERS.get(company_name)

    if not ticker:
        return {
            "ticker": "UNKNOWN",
            "currency": "BRL",
            "price": 0.0,
            "last_update": None
        }

    return get_stock_price(ticker)
