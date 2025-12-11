# chains/news_chain.py
from typing import List

# Agora importamos do novo arquivo 'web_search', não mais do 'bing_search'
try:
    from APIs.web_search import search_news
except ImportError:
    # Fallback caso a pasta se chame tools
    from tools.web_search import search_news

def get_company_news(company_name: str) -> List[dict]:
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