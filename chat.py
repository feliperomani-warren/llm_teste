import streamlit as st
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory


# Carrega a API Key
api_key = st.secrets["GEMINI"]["api_key"]
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro-exp-03-25", google_api_key=api_key)


if "memory" not in st.session_state:   # Inicializa a memória e a conversação no session_state
    st.session_state.memory = ConversationBufferMemory()

if "conversation" not in st.session_state:
    st.session_state.conversation = ConversationChain(llm=llm, memory=st.session_state.memory)


st.set_page_config(page_title="Chatbot Gemini", page_icon="🤖", layout="wide")# Configuração da Página
st.logo("assets/LogoWarrenRena.png", icon_image="assets/LogoWRena.png")
st.title("🤖 Chatbot Gemini com LangChain")


if "messages" not in st.session_state:# Inicializa o histórico no session_state se ainda não existir
    st.session_state["messages"] = []

for message in st.session_state["messages"]:# Exibe o histórico de mensagens no chat
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("Digite sua pergunta...")# Campo de input do usuário

if user_input:
    
    st.session_state["messages"].append({"role": "user", "content": user_input})# Adiciona a mensagem do usuário ao histórico

    
    response = st.session_state.conversation.run(user_input)# Obtém resposta do Gemini via LangChain

    
    st.session_state["messages"].append({"role": "assistant", "content": response})# Adiciona a resposta ao histórico

    
    with st.chat_message("assistant"):# Exibe a resposta no chat
        st.markdown(response)
        
