import streamlit as st

# --- PAGE SETUP ---
pagina_inicial = st.Page(
    "pages/Receitas_por_Mesa_e_Ativo.py",
    title="Receitas por Mesa e Ativo",
    icon=":material/attach_money:",
    default=True,
)

pagina_resultados = st.Page(
    "pages/Acompanhamento_Metas.py",
    title="Acompanhamento Metas",
    icon=":material/target:",
)

pagina_chat = st.Page(
    "pages/chat.py",
    title="Chat",
    icon=":material/smart_toy:",
)

pagina_chat2 = st.Page(
    "pages/chat copy.py",
    title="Chat2",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation({
    "Institucional": [pagina_inicial, pagina_resultados],
    "Perguntas": [pagina_chat, pagina_chat2]
})


# --- RUN NAVIGATION ---
pg.run()