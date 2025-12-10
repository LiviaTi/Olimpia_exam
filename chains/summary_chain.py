# chains/summary_chain.py
"""
Company summary chain.
This module exposes `get_company_summary(company_name: str) -> dict`
which returns a structured summary matching interfaces/schemas.CompanySummarySchema.

Requirements:
- LANGCHAIN (pip install langchain)
- OpenAI Python client (if using ChatOpenAI) and environment variable OPENAI_API_KEY set
- Optionally a prompt file at prompts/company_summary.txt

Behavior:
- Use a PromptTemplate to instruct the LLM to return strict JSON.
- Parse the JSON and return a dict with keys: company_name, sector, description.
- On failure, return a minimal fallback summary.
"""

from typing import Dict
import json
import os

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Default model settings (deterministic for demo)
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))  # deterministic by default


def _load_prompt_template() -> str:
    """
    Load the prompt template from prompts/company_summary.txt if present,
    otherwise return a built-in fallback prompt.
    """
    prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts", "company_summary.txt")
    if os.path.isfile(prompt_path):
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            # if file exist but reading fails, fall back to builtin
            pass

    # Built-in prompt (kept concise and explicit about JSON output)
    return (
        "You are an investment banking research assistant.\n\n"
        "Given the company name: {company_name}, produce a concise, professional company summary.\n\n"
        "Return a JSON object **only** (no additional text) with the following fields:\n"
        " - company_name: full canonical company name (string)\n"
        " - sector: main sector or industry (string)\n"
        " - description: short paragraph (2-4 sentences) describing the company's activities, brief history and main products/services (string)\n\n"
        "Example:\n"
        '{\"company_name\": \"Petrobras\", \"sector\": \"Energy / Oil & Gas\", \"description\": \"Petróleo Brasileiro S.A. (Petrobras) is a state-controlled energy company...\"}\n\n'
        "If you are not sure about a specific field, provide the best succinct answer you can."
    )


def _build_prompt(company_name: str) -> PromptTemplate:
    """
    Return a PromptTemplate instance for the given company_name.
    """
    template_text = _load_prompt_template()
    # Use {company_name} as input variable
    return PromptTemplate(template=template_text, input_variables=["company_name"])


def get_company_summary(company_name: str) -> Dict[str, str]:
    """
    Generate a structured company summary for the given company_name.

    Returns a dict matching:
    {
      "company_name": str,
      "sector": str,
      "description": str
    }

    On parsing or LLM failure, returns a minimal fallback with the company_name and short description.
    """
    if not company_name or not company_name.strip():
        raise ValueError("company_name must be a non-empty string")

    # Initialize LLM
    llm = ChatOpenAI(model=LLM_MODEL, temperature=LLM_TEMPERATURE)

    prompt = _build_prompt(company_name)
    chain = LLMChain(llm=llm, prompt=prompt)

    try:
        # Run chain - the prompt instructs the model to return JSON only
        response_text = chain.run(company_name=company_name)

        # Attempt to parse JSON from model output robustly
        # Model may include surrounding whitespace/newlines; extract first JSON object occurrence.
        response_text = response_text.strip()

        # If the model accidentally includes text before/after JSON, try to find the JSON block
        # Simple heuristic: find first '{' and last '}' and parse substring
        if not response_text.startswith("{"):
            first_brace = response_text.find("{")
            last_brace = response_text.rfind("}")
            if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
                json_text = response_text[first_brace:last_brace + 1]
            else:
                json_text = response_text  # give it a try
        else:
            json_text = response_text

        parsed = json.loads(json_text)

        # Basic validation and normalization of keys
        company = parsed.get("company_name") or parsed.get("company") or company_name
        sector = parsed.get("sector") or parsed.get("industry") or "N/A"
        description = parsed.get("description") or parsed.get("summary") or ""

        # Final dict matching CompanySummarySchema
        result = {
            "company_name": str(company).strip(),
            "sector": str(sector).strip(),
            "description": str(description).strip()
        }

        return result

    except Exception as exc:
        # Fallback: return a minimal, safe summary
        fallback = {
            "company_name": company_name,
            "sector": "Unknown",
            "description": f"Automated summary not available due to an error: {str(exc)}"
        }
        return fallback


# Simple demo / test when running module directly
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Quick test for summary_chain")
    parser.add_argument("company", help="Company name to summarize")
    args = parser.parse_args()

    summary = get_company_summary(args.company)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
