from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


llm = GoogleGenerativeAI(model="gemini-pro")
prompt=PromptTemplate.from_template("qual é o maior {input} do mundo?")
model=prompt|llm


st.set_page_config(page_title='Gemini chat')
st.header('Gemini Chat')

entrada = st.chat_input("Say something")
user = st.chat_message("user")
user.write(f"qual é o maior {entrada} do mundo?")

if entrada:
    answer = model.invoke({'input':entrada})
    gemini = st.chat_message("assistant")
    gemini.write(answer)