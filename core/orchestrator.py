# core/orchestrator.py

from chains.summary_chain import get_company_summary
from chains.news_chain import get_company_news
from chains.stock_chain import get_company_stock_price


def run_company_research(company_name: str) -> dict:
    """
    Orchestrates all research chains.
    """
    return {
        "company": company_name,
        "summary": get_company_summary(company_name),
        "news": get_company_news(company_name),
        "stock_price": get_company_stock_price(company_name)
    }
