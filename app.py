import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACKING_V2"]="true"

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

promt=ChatPromptTemplate.from_messages(
    [
       ( "system","Hello, I am Ollama, a language model trained by Langchain. I can help you with your language learning journey. What would you like to learn today?"),
       ( "user","Question:{question}")
    ]
)

st.title("Ollama_Language_Learning")
input_text=st.text_input("Enter your question here")

llm=Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain=promt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
