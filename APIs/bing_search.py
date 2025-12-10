# tools/bing_search.py

import os
import requests
from typing import List, Dict

BING_API_KEY = os.getenv("BING_API_KEY")
BING_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"


def search_news(query: str, count: int = 3) -> List[Dict]:
    """
    Search recent news using Bing Web Search API.
    """
    if not BING_API_KEY:
        raise EnvironmentError("BING_API_KEY environment variable not set")

    headers = {
        "Ocp-Apim-Subscription-Key": BING_API_KEY
    }

    params = {
        "q": query,
        "mkt": "pt-BR",
        "freshness": "7",
        "responseFilter": "News",
        "count": count
    }

    response = requests.get(BING_ENDPOINT, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    results = []

    for item in data.get("news", {}).get("value", []):
        results.append({
            "title": item.get("name"),
            "source": item.get("provider", [{}])[0].get("name"),
            "url": item.get("url")
        })

    return results
