# interfaces/schemas.py
from typing import List, TypedDict, Optional


class CompanySummarySchema(TypedDict):
    company_name: str
    sector: str
    description: str


class NewsItemSchema(TypedDict):
    title: str
    source: Optional[str]
    url: Optional[str]


class StockPriceSchema(TypedDict):
    ticker: str
    currency: str
    price: float
    last_update: Optional[str]


class CompanyResearchResultSchema(TypedDict):
    company: str
    summary: CompanySummarySchema
    news: List[NewsItemSchema]
    stock_price: StockPriceSchema
