import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Study & Career Assistant")

user_input = st.text_input("Ask anything")

if st.button("Send"):
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
        