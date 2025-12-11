# core/orchestrator.py

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from chains.summary_chain import get_company_summary
from chains.news_chain import get_company_news
from chains.stock_chain import get_company_stock_price

def run_company_research(company_name: str) -> dict:
    """
    Orquestra a pesquisa usando LangChain RunnableParallel (LCEL).
    Executa resumo, notícias e ações em paralelo.
    """
    
    # Define o fluxo paralelo
    # O input (company_name) é passado para todas as 'branches' automaticamente.
    research_chain = RunnableParallel({
        "company": RunnablePassthrough(),  # Mantém o nome original
        "summary": RunnableLambda(get_company_summary),
        "news": RunnableLambda(get_company_news),
        "stock_price": RunnableLambda(get_company_stock_price)
    })
    
    # Executa o fluxo
    return research_chain.invoke(company_name)