# main.py

import sys
import json
from core.orchestrator import run_company_research


def main():
    if len(sys.argv) < 2:
        raise ValueError("Company name not provided")

    company_name = sys.argv[1]
    result = run_company_research(company_name)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
