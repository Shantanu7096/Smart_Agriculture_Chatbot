import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="Smart Agriculture Assistant",
    page_icon="🌱"
)

st.title("🌱 Smart Agriculture Assistant")

st.write("Ask me anything about agriculture, crops, irrigation, weather, soil, fertilizers, greenhouse farming, etc.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    prompt = f"""
You are an Agriculture Assistant chatbot.

Rules:
- Answer only agriculture related questions.
- If the question is not related to agriculture, politely reply:
'I am designed to answer agriculture-related questions only.'

User Question:
{question}
"""

    response = model.generate_content(prompt)

    answer = response.text

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)