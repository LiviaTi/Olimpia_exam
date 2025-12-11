# app.py
import streamlit as st
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Importa o orquestrador (certifique-se que a pasta core existe)
try:
    from core.orchestrator import run_company_research
except ImportError:
    st.error("Erro: Não foi possível importar o sistema central. Verifique se a pasta 'core' está correta.")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS AVANÇADO (UI/UX) ---
st.markdown("""
<style>
    /* 1. FUNDO BRANCO CLEAN */
    .stApp {
        background-color: #ffffff;
        background-image: radial-gradient(#e5e7eb 1px, transparent 1px);
        background-size: 20px 20px;
        font-family: 'Inter', sans-serif;
    }

    /* 2. CARTÕES (Aumentei o padding para ficar mais espaçoso) */
    .data-card {
        background-color: rgba(255, 255, 255, 0.95);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 30px; /* Mais espaço interno */
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s;
    }
    .data-card:hover {
        border-color: #0ea5e9;
        box-shadow: 0 8px 16px rgba(14, 165, 233, 0.1);
    }

    /* 3. TIPOGRAFIA AUMENTADA (FÁCIL LEITURA) */
    h1 {
        font-size: 3rem !important; /* Título bem grande */
        color: #0f172a !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }
    h2 {
        font-size: 2rem !important;
        color: #0f172a !important;
        font-weight: 700 !important;
    }
    h3 {
        font-size: 1.5rem !important;
        color: #1e293b !important;
        font-weight: 700 !important;
    }
    
    /* Texto geral maior */
    p, label, li, span, div.stMarkdown {
        font-size: 1.15rem !important; /* Aumentado para ~18px */
        color: #334155 !important;
        line-height: 1.7;
    }
    
    strong {
        color: #000000 !important;
    }

    /* 4. INPUT DE PESQUISA (Maior e mais visível) */
    .stTextInput > div > div > input {
        background-color: #f8fafc;
        color: #0f172a;
        border: 2px solid #cbd5e1; /* Borda um pouco mais grossa */
        border-radius: 12px;
        padding: 15px; /* Mais gordinho */
        font-size: 1.2rem; /* Letra maior ao digitar */
    }
    .stTextInput > div > div > input:focus {
        border-color: #0ea5e9;
        background-color: #ffffff;
        box-shadow: 0 0 0 4px rgba(14, 165, 233, 0.1);
    }

    /* 5. BOTÃO AZUL VIBRANTE (O destaque!) */
   .stTextInput > div > div > input {
        background-color: #f8fafc;
        color: #0f172a; /* Texto escuro */
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 12px;
        font-size: 16px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #0ea5e9;
        background-color: #ffffff;
        box-shadow: 0 0 0 2px rgba(14, 165, 233, 0.2);
    }
    /* 6. MÉTRICAS (PREÇO GIGANTE) */
    [data-testid="stMetricValue"] {
        font-size: 48px !important; /* Preço bem grande */
        color: #0284c7 !important; /* Azul forte */
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
    }
    [data-testid="stMetricLabel"] {
        font-size: 1.1rem !important;
        color: #64748b !important;
    }
    .stButton > button {
        background: #499dff; /* Botão preto/azul escuro */
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: #0084ff;
        transform: translateY(-2px);
    }
    /* 7. LINKS DE NOTÍCIAS (CONFORTÁVEIS) */
    a.news-link {
        text-decoration: none;
        color: #1e293b;
        display: block;
        padding: 18px; /* Mais área de clique */
        border-radius: 10px;
        background: #f1f5f9;
        margin-bottom: 15px;
        border-left: 6px solid #0ea5e9; /* Borda lateral mais grossa */
        transition: transform 0.2s, background 0.2s;
    }
    a.news-link:hover {
        background: #e2e8f0;
        transform: translateX(5px); /* Move levemente para a direita */
    }
    .news-title {
        font-size: 1.2rem; /* Título da notícia maior */
        font-weight: 600;
        margin-bottom: 5px;
    }
    .news-source {
        font-size: 0.9rem;
        color: #64748b;
        text-transform: uppercase;
        font-weight: 600;
    }

    /* Esconder elementos padrão */
    header {visibility: hidden;}
    footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# --- LAYOUT PRINCIPAL ---

st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>📊 Market Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-bottom: 40px; color: #64748b;'>Tome decisões melhores com dados e notícias em tempo real IA</p>", unsafe_allow_html=True)

# Área de Busca
col_search_1, col_search_2, col_search_3 = st.columns([1, 6, 1])
with col_search_2:
    company = st.text_input("Investigar Ativo", placeholder="Ex: Petrobras, Vale, Apple...")
    btn_search = st.button("Executar Análise")

# Lógica de Exibição
if btn_search and company:
    st.markdown("---")
    
    with st.spinner("🔄 Conectando aos mercados e processando dados..."):
        try:
            result = run_company_research(company)
            
            # Extraindo dados
            summary = result.get("summary", {})
            stock = result.get("stock_price", {})
            news_list = result.get("news", [])

            # --- LINHA 1: DESTAQUES (Preço e Setor) ---
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Cartão de Cotação
                st.markdown('<div class="data-card">', unsafe_allow_html=True)
                st.caption("Cotação Atual")
                
                ticker = stock.get("ticker", "N/A")
                price = stock.get("price", 0.0)
                currency = stock.get("currency", "BRL")
                
                # Exibindo métrica nativa dentro do cartão HTML
                st.metric(label=ticker, value=f"{currency} {price:.2f}")
                
                if stock.get("last_update"):
                    st.caption(f"Atualizado em: {stock.get('last_update')}")
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                # Cartão de Perfil
                st.markdown('<div class="data-card" style="height: 100%;">', unsafe_allow_html=True)
                st.subheader(f"🏢 {summary.get('company_name', company)}")
                st.markdown(f"**Setor:** <span style='padding: 2px 8px; border-radius: 4px; font-size: 0.9em;'>{summary.get('sector', 'N/A')}</span>", unsafe_allow_html=True)
                st.markdown(f"<div style='margin-top: 15px;'>{summary.get('description', 'Sem descrição.')}</div>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # --- LINHA 2: NOTÍCIAS (Feed) ---
            st.subheader("📰 Radar de Notícias")
            st.markdown('<div class="data-card">', unsafe_allow_html=True)
            
            if news_list:
                for item in news_list:
                    # Layout customizado para notícia
                    st.markdown(f"""
                    <a href="{item['url']}" target="_blank" class="news-link">
                        <div>{item['title']}</div>
                        <div class="news-source">FONTE: {item['source']}</div>
                    </a>
                    """, unsafe_allow_html=True)
            else:
                st.info("Nenhuma notícia recente relevante encontrada para este ativo.")
            
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Falha na análise: {str(e)}")

# Rodapé minimalista
st.markdown("<br><br><p style='text-align: center; font-size: 0.8em; opacity: 0.5;'>Powered by Gemini AI & DuckDuckGo</p>", unsafe_allow_html=True)