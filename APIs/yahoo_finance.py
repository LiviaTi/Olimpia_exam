# APIs/yahoo_finance.py

import yfinance as yf
from datetime import datetime, timezone, timedelta
from typing import Dict

def get_stock_price(ticker: str) -> Dict:
    """
    Recupera preço, horário da última negociação e estado do mercado.
    Garante que o horário seja convertido corretamente para BRT se for ação brasileira.
    """
    stock = yf.Ticker(ticker)
    
    # 1. Tenta obter dados rápidos de preço (FastInfo)
    # fast_info é um objeto, acessamos via atributos.
    try:
        fast_info = stock.fast_info
        price = fast_info.last_price
        currency = fast_info.currency
    except AttributeError:
        price = None
        currency = "BRL"

    # 2. Busca metadados detalhados em .info para Horário e Estado
    # O .info contém 'regularMarketTime' (Unix timestamp da última troca)
    # e 'marketState' (REGULAR, CLOSED, PRE, POST).
    try:
        info = stock.info
        
        # Fallback de preço se fast_info falhou
        if price is None:
            price = info.get('currentPrice') or info.get('regularMarketPrice')
            currency = info.get('currency', 'BRL')

        # Timestamp exato da última transação registrada
        market_time_ts = info.get('regularMarketTime')
        
        # Estado do mercado: 'REGULAR' (Aberto), 'CLOSED', 'PRE', 'POST'
        market_state = info.get('marketState', 'UNKNOWN')
        
    except Exception:
        market_time_ts = None
        market_state = "UNKNOWN"

    # 3. Formatação de Data/Hora e Status
    last_update_str = "N/A"
    is_market_open = False
    
    if market_time_ts:
        # Cria objeto datetime em UTC
        dt_utc = datetime.fromtimestamp(market_time_ts, tz=timezone.utc)
        
        # Se for ticker brasileiro (.SA), converte para BRT (UTC-3)
        if ".SA" in ticker.upper() or currency == "BRL":
            # Ajuste simples para UTC-3 (Horário de Brasília)
            dt_brt = dt_utc - timedelta(hours=3)
            last_update_str = dt_brt.strftime('%d/%m/%Y %H:%M:%S (BRT)')
        else:
            last_update_str = dt_utc.strftime('%Y-%m-%d %H:%M:%S (UTC)')

    # Traduz e define o status para exibição
    status_map = {
        "REGULAR": "Aberto",
        "CLOSED": "Fechado",
        "PRE": "Pré-Market",
        "POST": "After-Market",
        "PREPRE": "Fechado",
        "POSTPOST": "Fechado"
    }
    status_label = status_map.get(market_state, market_state)

    return {
        "ticker": ticker,
        "currency": currency,
        "price": float(price) if price else 0.0,
        "last_update": last_update_str,
        "market_status": status_label,   # Ex: "Aberto", "Fechado"
        "raw_state": market_state        # Debug se precisar
    }