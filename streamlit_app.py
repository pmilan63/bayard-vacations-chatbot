import streamlit as st
import requests

FLASK_API_URL = "http://127.0.0.1:5000/chat"

st.set_page_config(page_title="Bayard Vacations Chatbot", page_icon="✈️")

st.title("✈️ Bayard Vacations Chatbot")
st.write("Ask me about travel packages, destinations, pricing, or booking process.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            FLASK_API_URL,
            json={"message": user_input},
            timeout=5
        )
        bot_reply = response.json().get("response", "Sorry, I couldn't understand that.")
    except Exception as e:
        bot_reply = "Backend server is not running."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
