import streamlit as st
import openai
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    llm=ChatGroq(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Enhanced Q&A Chatbot With Groq")


## Sidebar for settings
st.sidebar.title("Settings")

## Select the Groq model
engine=st.sidebar.selectbox("Select AI model",["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "deepseek-r1-distill-llama-70b","gemma2-9b-it"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## MAin interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)

elif user_input:
    st.warning("Please enter the Groq API Key in the sider bar")
else:
    st.write("Please provide the user input")


