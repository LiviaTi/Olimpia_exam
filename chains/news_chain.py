# chains/news_chain.py

from typing import List
from tools.bing_search import search_news


def get_company_news(company_name: str) -> List[dict]:
    """
    Retrieve and normalize recent news for a given company.
    """
    query = f"{company_name} stock market news"
    news_items = search_news(query)

    return [
        {
            "title": item["title"],
            "source": item.get("source"),
            "url": item.get("url")
        }
        for item in news_items
    ]
