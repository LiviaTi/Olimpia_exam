# chains/stock_chain.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate  # <--- Corrigido aqui
from langchain_core.output_parsers import StrOutputParser

# Tente importar da pasta APIs ou tools
try:
    from APIs.yahoo_finance import get_stock_price
except ImportError:
    from tools.yahoo_finance import get_stock_price

def get_ticker_from_name(company_name: str) -> str:
    """
    Usa o Gemini para descobrir o ticker da empresa na B3.
    """
    if not os.getenv("GOOGLE_API_KEY"):
        return "UNKNOWN"

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.0,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    template = """
    Você é um especialista em mercado financeiro brasileiro.
    Retorne APENAS o código de negociação (ticker) da empresa "{company_name}" na B3 (Yahoo Finance), com o sufixo .SA.
    
    Regras:
    1. Retorne APENAS o código (ex: PETR4.SA). Nada de texto extra.
    2. Se a empresa não for listada ou não encontrar, retorne exatamente: UNKNOWN
    
    Exemplos:
    - Petrobras -> PETR4.SA
    - Vale -> VALE3.SA
    - Nubank -> ROXO34.SA
    
    Ticker:
    """
    
    prompt = PromptTemplate(template=template, input_variables=["company_name"])
    chain = prompt | llm | StrOutputParser()
    
    try:
        ticker = chain.invoke({"company_name": company_name})
        return ticker.strip()
    except Exception:
        return "UNKNOWN"


def get_company_stock_price(company_name: str) -> dict:
    """
    Fluxo: Descobre ticker -> Busca Preço
    """
    ticker = get_ticker_from_name(company_name)
    
    if ticker == "UNKNOWN":
        return {
            "ticker": "UNKNOWN",
            "currency": "BRL",
            "price": 0.0,
            "last_update": None,
            "error": "Ticker not found by AI"
        }

    try:
        return get_stock_price(ticker)
    except Exception as e:
        return {
            "ticker": ticker,
            "currency": "BRL",
            "price": 0.0,
            "last_update": None,
            "error": str(e)
        }