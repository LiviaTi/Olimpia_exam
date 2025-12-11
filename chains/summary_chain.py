# chains/summary_chain.py
import json
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_company_summary(company_name: str) -> dict:
    """
    Gera resumo estruturado usando Google Gemini.
    """
    if not company_name:
        return {"error": "No company name provided"}

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    template = """
    Atue como um analista de Investment Banking.
    Escreva um resumo sobre a empresa: {company_name}.
    
    A saída DEVE ser um JSON válido com as seguintes chaves:
    - "company_name": Nome oficial da empresa.
    - "sector": Setor de atuação.
    - "description": Um parágrafo conciso (2-3 frases) descrevendo o que a empresa faz.

    Responda APENAS o JSON, sem markdown (```json).
    """
    
    prompt = PromptTemplate(template=template, input_variables=["company_name"])
    chain = prompt | llm | StrOutputParser()

    try:
        response = chain.invoke({"company_name": company_name})
        # Limpeza de segurança para remover crase de markdown se houver
        clean_json = response.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        return {
            "company_name": company_name,
            "sector": "N/A",
            "description": f"Erro ao gerar resumo: {str(e)}"
        }