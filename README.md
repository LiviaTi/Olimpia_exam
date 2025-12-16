<h1>Olimpia Partners</h1>

<h2>Automação de Pesquisa de Empresas (LangChain)</h2>

<p><strong>Versão:</strong> 1.1<br>
<strong>Autora:</strong> Lívia Ferreira Santos<br>


<hr>

<h2>Índice</h2>
<ol>
  <li>Visão Geral do Projeto</li>
  <li>Arquitetura &amp; Fluxograma</li>
  <li>Estrutura do Repositório</li>
  <li>Requisitos &amp; Dependências</li>
  <li>Instalação</li>
  <li>Variáveis de Ambiente</li>
  <li>Uso (CLI / Streamlit)</li>
  <li>Formato de Saída</li>
  <li>Melhorias Futuras</li>
</ol>

<hr>

<h2>1. Visão Geral do Projeto</h2>
<p>
Este projeto implementa um <strong>workflow automatizado de pesquisa corporativa</strong>, utilizando <strong>LangChain</strong> para orquestração de agentes e integração com ferramentas de busca e APIs públicas.
</p>

<p>
A solução recebe como entrada o <strong>nome de uma empresa brasileira de capital aberto</strong> e retorna informações estruturadas, incluindo:
</p>

<ul>
  <li>Resumo institucional da empresa</li>
  <li>Notícias recentes (2 a 3 itens relevantes)</li>
  <li>Preço atual da ação</li>
</ul>

<p>
A aplicação foi desenvolvida em <strong>Python</strong>, com suporte para <strong>CLI</strong> e <strong>interface gráfica via Streamlit</strong>, oferecendo uma experiência interativa, clara e profissional.
</p>

<hr>

<h2>2. Arquitetura &amp; Fluxograma</h2>

<h3>Arquitetura de Alto Nível</h3>
<ul>
  <li><strong>Entrada</strong>
    <ul>
      <li>Interface Streamlit (<code>app.py</code>)</li>
      <li>CLI (<code>main.py</code>)</li>
    </ul>
  </li>
  <li><strong>Orquestrador</strong>
    <ul>
      <li>Pipeline principal implementado com <strong>LangChain</strong></li>
    </ul>
  </li>
  <li><strong>Agents / Workers</strong>
    <ul>
      <li>Resumo da empresa: Sites institucionais + LLM</li>
      <li>Notícias: DuckDuckGo</li>
      <li>Preço da ação: Yahoo Finance (<code>yfinance</code>)</li>
    </ul>
  </li>
  <li><strong>Agregador</strong>
    <ul>
      <li>Consolidação, validação e formatação dos dados</li>
    </ul>
  </li>
  <li><strong>Saída</strong>
    <ul>
      <li>Terminal (output formatado)</li>
      <li>Interface Streamlit</li>
    </ul>
  </li>
</ul>

<h3>Fluxo de Execução</h3>
<ol>
  <li>Usuário informa o nome da empresa</li>
  <li>O orquestrador aciona os agentes especializados</li>
  <li>Cada agente coleta e processa seus dados</li>
  <li>O agregador organiza o resultado final</li>
  <li>Os dados são exibidos na UI ou no terminal</li>
</ol>

<hr>

<h2>3. Estrutura do Repositório</h2>

<pre><code>Olimpia_exam/
│
├── app.py                 # Interface Streamlit
├── main.py                # Entrypoint via CLI (ex.: python main.py "Petrobras")
├── requirements.txt
│
├── chains/
│   ├── summary_chain.py   # Cadeia de resumo institucional
│   ├── news_chain.py      # Cadeia de notícias
│   └── stock_chain.py     # Cadeia de preço da ação
│
├── APIs/
│   ├── web_search.py      # Busca web/notícias
│   └── yahoo_finance.py   # Integração com Yahoo Finance
│
├── core/
│   └── orchestrator.py    # Orquestrador principal (LangChain)
│
└── docs/
    └── documentation.pdf
</code></pre>

<hr>

<h2>4. Requisitos &amp; Dependências</h2>
<ul>
  <li>Python 3.11</li>
  <li>langchain 1.1.3</li>
  <li>google-genai 1.55.0</li>
  <li>requests 2.32.5</li>
  <li>yfinance 0.2.66</li>
  <li>streamlit 1.52.1</li>
  <li>duckduckgo_search 8.1.1</li>
  <li>python-dotenv 1.2.1</li>
</ul>

<hr>

<h2>5. Instalação</h2>

<pre><code>git clone https://github.com/LiviaTi/Olimpia_exam.git
cd Olimpia_exam

python -m venv .venv

# Linux / Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
</code></pre>

<hr>

<h2>6. Variáveis de Ambiente</h2>

<p>Crie um arquivo <code>.env</code> na raiz do projeto:</p>

<pre><code>GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY</code></pre>

<p><strong>Importante:</strong> nunca versionar chaves de API em repositórios públicos.</p>

<hr>

<h2>7. Uso</h2>

<h3>Streamlit (UI)</h3>
<pre><code>streamlit run app.py</code></pre>

<p>Acesse no navegador: <code>http://localhost:8501</code></p>

<h3>CLI</h3>
<pre><code>python main.py "Petrobras"</code></pre>

<hr>

<h2>8. Formato de Saída</h2>
<p>A saída apresenta, de forma estruturada:</p>
<ul>
  <li>Nome da empresa</li>
  <li>Resumo institucional objetivo</li>
  <li>Notícias recentes com título e fonte</li>
  <li>Preço atual da ação</li>
</ul>

<p>Na interface Streamlit, os dados são exibidos de maneira visual e organizada.</p>

<hr>

<h2>9. Melhorias Futuras</h2>
<ul>
  <li>Integração com Webhooks (Slack, e-mail, etc.)</li>
  <li>Uso da Bing Search API para maior precisão</li>
  <li>Integração com n8n para automação no-code</li>
  <li>Persistência dos dados para histórico e auditoria</li>
  <li>Dashboard no Streamlit com gráficos e comparações</li>
</ul>

<hr>

<p><strong>Olimpia Partners</strong> — Automação inteligente de pesquisa corporativa com LangChain.</p>
