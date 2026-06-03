import streamlit as st

# 1. Configuração Inicial da Página
st.set_page_config(
    page_title="Portfólio de Automações", 
    page_icon="🤖", 
    layout="wide"
)

# --- SOLUÇÃO INFALÍVEL: INJEÇÃO DE CSS PARA O TEMA PRETO E ROXO ---
st.markdown("""
    <style>
        /* 1. Mudar o fundo principal para preto */
        .stApp {
            background-color: #000000 !important;
        }
        
        /* 2. Mudar o fundo da barra lateral para cinza bem escuro */
        [data-testid="stSidebar"] {
            background-color: #121212 !important;
        }
        
        /* 3. Mudar a cor de todos os links para Roxo */
        a {
            color: #9D4EDD !important;
            text-decoration: none;
        }
        
        /* 4. Mudar a cor do link quando passas o rato por cima */
        a:hover {
            color: #B47AEA !important;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)
# ------------------------------------------------------------------

# 2. BARRA LATERAL - Perfil e Contactos
with st.sidebar:
    st.title("👤 Sobre Mim")
    st.write("""
    Olá! O meu nome é Ana Clara Nishiki. 
    
    Sou desenvolvedora e estudante de **Engenharia de Software** (1.º período). Movida pela curiosidade e pelo desejo de resolver problemas reais, procuro constantemente ir além da faculdade através de cursos especializados por fora.
    
    O meu foco principal é a criação de **automações inteligentes** que eliminam tarefas repetitivas e otimizam processos.
    """)
    
    st.markdown("---")
    st.write("**🧠 Principais Competências:**")
    st.markdown("- 🐍 Python & Lógica de Programação")
    st.markdown("- 🤖 Automação de Processos (Scripts)")
    st.markdown("- 🌐 HTML5 & CSS3 (Estruturação e Estilo Web)")
    st.markdown("- 📚 Aprendizagem Contínua & Resolução de Problemas")
    
    st.markdown("---")
    st.write("**📬 Vamos conversar?**")
    st.write("📧 Dev.Nishiki@gmail.com")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/authwall?trk=gf&trkInfo=AQFqKNTm2Q36GAAAAZ6K7Or4-3qhqWMziFSkPJTQCNjvSdut_-QAQvQYIM2M41wLOdOr5Y-Tt2CuHdanYLSDlzjTJU-ZpqnKrw_jOPov1SwENqOAn6LSEsaR7y1z0JxAxwVh8OE=&original_referer=https://www.google.com/&sessionRedirect=https%3A%2F%2Fbr.linkedin.com%2Fin%2Fana-clara-nishiki-a9bb04248)")
    st.markdown("[💻 GitHub](https://github.com/Dev-Nishiki)")

# 3. ÁREA PRINCIPAL - Apresentação
st.title("🤖 Meu Portfólio de Automações")
st.subheader("Bem-vindo aqui você verá os robôs e scripts que desenvolvi para otimizar processos.")
st.markdown("---")

# 4. GALERIA DE PROJETOS (Organizada em Colunas)
st.header("📂 Projetos em Destaque")

# --- LINHA 1: AUTOMAÇÕES CONTABILIZEI ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("💼 Robô de Cadastro - Contabilizei (CPF)")
    st.write("""
    **Problema:** Necessidade de inserir dados em lote (e-mails/CNPJs) numa plataforma com seletores dinâmicos em React, gerando trabalho manual demorado.  
    **Solução:** Bot em Playwright que lê dados do Excel, manipula os campos React limpando e simulando digitação humana sequencial, interage com dropdowns complexos com sistemas de fallback (teclado) e grava o status de envio em tempo real na folha Excel.
    """)
    st.caption("🛠️ Tecnologias: Python, Playwright, Openpyxl, Manipulação de DOM/React")
    st.markdown("[Código no GitHub](https://github.com)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("🖥️ App Desktop: Interface para Procurações")
    st.write("""
    **Problema:** Scripts em terminal podem ser difíceis de operar por utilizadores finais ou equipas de operações.  
    **Solução:** Transformação do motor de automação numa aplicação de ambiente de trabalho (Desktop) moderna e intuitiva. Implementação de Multi-threading (para a interface não congelar enquanto o robô roda), logs em tempo real na tela e caixas de diálogo integradas.
    """)
    st.caption("🛠️ Tecnologias: Python, CustomTkinter (GUI), Threading, Playwright")
    st.markdown("[Código no GitHub](https://github.com)")
    st.markdown('</div>', unsafe_allow_html=True)

# --- LINHA 2: PORTAIS MUNICIPAIS & QUEBRA DE CAPTCHAS ---
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("👁️ Inteligência Antidefesa: Robô Nota Carioca (RJ)")
    st.write("""
    **Problema:** Bloqueios por Captchas visuais que impedem o login e a automação de declarações fiscais municipais.  
    **Solução:** Um robô ultra avançado que tira prints do elemento do Captcha em tempo real, usa processamento digital de imagens (Filtro de Desfoque Gaussiano e Limiarização Fixo Agressivo/Otsu com OpenCV) e quebra a proteção usando Redes Neuronais locais (ddddocr) para declarar ausência de movimento e extrair recibos.
    """)
    st.caption("🛠️ Tecnologias: Python, Playwright, OpenCV (cv2), ddddocr (Neural Networks), Pandas")
    st.markdown("https://github.com/Dev-Nishiki/Automa-o-Rio-de-janeiro-")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("🌐 Extensões e Engenharia de Shadow DOM: Barueri")
    st.write("""
    **Problema:** Portais seguros com Google ReCAPTCHA Enterprise e elementos escondidos dentro de componentes complexos isolados (Shadow DOM / visualizadores internos de PDF do Chrome).  
    **Solução:** Script que inicia contextos persistentes do Chromium injetando uma extensão externa de resolução de captchas. O código faz engenharia reversa via JavaScript injetado para manipular e clicar em elementos ocultos do navegador e extrair relatórios fiscais diretamente da sessão autenticada.
    """)
    st.caption("🛠️ Tecnologias: Python, Playwright Async/Sync, Anti-Captcha API, Chrome Shadow DOM Injection")
    st.markdown("https://github.com/Dev-Nishiki/Automa-o-Barueri-)")
    st.markdown('</div>', unsafe_allow_html=True)

# --- LINHA 3: FISCAL FEDERAL ---
col5, _ = st.columns([1, 1]) # O segundo parâmetro vazio mantém o card do mesmo tamanho dos outros

with col5:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("📊 Mapeador Dinâmico PGDAS - Receita Federal")
    st.write("""
    **Problema:** Declaração manual massiva de informações de exportação do Simples Nacional que exige cruzar e preencher dados de mais de 30 colunas diferentes ao longo de 12 meses (Janeiro a Dezembro).  
    **Solução:** Um orquestrador de dados estruturados que lê esquemas dinâmicos do Excel, abre painéis em formato de sanfona (accordions) para cada mês de forma programática, insere os valores simulando tempos de digitação humana para evitar deteção de firewalls e faz o download automático dos arquivos federais .txt oficiais.
    """)
    st.caption("🛠️ Tecnologias: Python, Playwright, Openpyxl (Excel Data Mapping), OS-automation")
    st.markdown("[https://github.com/Dev-Nishiki/Automa-o-PGDAS)")
    st.markdown('</div>', unsafe_allow_html=True)