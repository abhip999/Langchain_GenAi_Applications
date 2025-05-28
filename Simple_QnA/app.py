import os
from dotenv import load_dotenv
#from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

## Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an AI Assistnat, please respond to the question asked"),
        ("user","Question:{question}")
    ]
)
## Streamlit framework
st.title("Simple Langchain demo with LLAMA3.2")
input_text = st.text_input("What is in your mind?")

##Ollama LLAMMA3.2 Model
llm = OllamaLLM(model="llama3.2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))