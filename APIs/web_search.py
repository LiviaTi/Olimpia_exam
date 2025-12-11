# APIs/web_search.py
from duckduckgo_search import DDGS
from typing import List, Dict

def search_news(query: str, count: int = 3) -> List[Dict]:
    """
    Busca notícias recentes usando DuckDuckGo (Gratuito).
    """
    results = []
    try:
        with DDGS() as ddgs:
            ddg_results = ddgs.news(
                keywords=query, 
                region="br-pt", 
                safesearch="off", 
                timelimit="w", 
                max_results=count
            )
            for item in ddg_results:
                results.append({
                    "title": item.get("title"),
                    "source": item.get("source"),
                    "url": item.get("url")
                })
    except Exception as e:
        print(f"Erro na busca: {e}")
        return []
    return results