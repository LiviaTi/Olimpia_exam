# app.py

import streamlit as st
from core.orchestrator import run_company_research

st.set_page_config(page_title="Company Research", layout="centered")

st.title("Company Research Tool")

company = st.text_input("Enter a Brazilian public company name:")

if st.button("Run Research") and company:
    with st.spinner("Collecting data..."):
        result = run_company_research(company)
        st.json(result)
