import os
import streamlit as st
from dotenv import load_dotenv

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI


# ------------------------------------------------------
# Load API Key (streamlit secrets or .env)
# ------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found in .env or Streamlit secrets.")
    st.stop()


# ------------------------------------------------------
# Initialize ChatBot
# ------------------------------------------------------
@st.cache_resource
def load_chatbot():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=api_key
    )
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory, verbose=False)
    return conversation

conversation_chain = load_chatbot()


# ------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------
st.set_page_config(page_title="LangChain Chatbot", layout="centered")
st.title("💬 LangChain ChatBot using OpenAI")


# Conversation Log
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# User Input Box
user_msg = st.text_input("Enter your message:", key="input_text")

if st.button("Send"):
    if user_msg.strip():
        with st.spinner("Generating response..."):
            reply = conversation_chain.predict(input=user_msg)

        # Save conversation
        st.session_state.chat_history.append(("You", user_msg))
        st.session_state.chat_history.append(("Bot", reply))

        st.rerun()


# Display Chat History
st.subheader("Conversation History")
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")


# Reset button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
