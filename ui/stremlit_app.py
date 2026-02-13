import streamlit as st
import requests

st.set_page_config(page_title="Personal Finance Chatbot", page_icon="💸")

st.title("💸 Personal Finance Chatbot")
st.write("Ask me about your spending and budget")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You")

if user_input:
    st.session_state.chat.append(("You", user_input))

    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"message": user_input}
    )

    data = response.json()
    bot_re = data[0]["text"] if data else "Sorry, I didn't get that"

    st.session_state.chat.append(("Bot", bot_re))

for se, msg in st.session_state.chat:
    st.markdown(f"**{se}:** {msg}")

st.divider()


