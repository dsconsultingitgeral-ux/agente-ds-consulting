import streamlit as st
from groq import Groq
from PIL import Image # Adicione esta linha no topo
# 1. Configuração da Identidade Visual
st.set_page_config(page_title="Digital Solutions & Consulting IT", page_icon="🚀")

# --- NOVO CÓDIGO PARA O LOGO ---
try:
    img = Image.open("logo.png") # Garanta que o nome aqui é igual ao do ficheiro que subiu
    st.image(img, width=200)     # Ajuste o tamanho (200) como preferir
except:
    st.warning("Logo não encontrado no repositório.")
# ------------------------------

# Estilo para parecer um chat profissional
st.markdown("""
    <style>
    .stApp { background-color: #f5f7f9; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Consultor Digital DS")
st.caption("Especialistas em Automação, IA e Eficiência Operacional")

# 2. Configuração da IA (Groq)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 3. O "Cérebro" do Agente - Contexto da Empresa
SYSTEM_PROMPT = """
Tu és o Consultor Proativo da 'Digital Solutions & Consulting IT'. 
O teu objetivo é ajudar o utilizador a entender como a transformação digital pode alavancar o negócio dele.
Baseia as tuas respostas nestes pilares da empresa:
- Automação Inteligente: eliminar erros humanos e tarefas repetitivas.
- IA & Formação: ensinar equipas a usar Prompt Engineering e LLMs.
- Decisões de Milhões: dashboards inteligentes e análise de dados (Python).
- Autoridade Digital: Websites e LinkedIn profissional.
- Produtividade Office/IT: infraestrutura sem falhas.

Tom de voz: Profissional, inovador, focado em lucro e eficiência. 
Se o utilizador parecer interessado, sugere contactar: ds.consulting.it@outlook.com
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Exibir histórico (escondendo o prompt de sistema)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Como posso escalar o meu negócio?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages,
            temperature=0.7
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
