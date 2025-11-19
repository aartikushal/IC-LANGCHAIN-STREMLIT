import streamlit as st
import os
from dotenv import load_dotenv

# LangChain Imports
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# LlamaIndex Imports
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import SimpleChatEngine


# ---------------------------------------------------------
# Load Environment / Secrets
# ---------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OpenAI API key not found in .env or Streamlit Secrets.")
    st.stop()

# ---------------------------------------------------------
# Streamlit Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Multi-Model Chatbot", layout="centered")
st.title("🤖 Multi-Model Chatbot (LangChain + LlamaIndex)")


# ---------------------------------------------------------
# Initialize Session State
# ---------------------------------------------------------
if "model" not in st.session_state:
    st.session_state.model = "LangChain"

if "langchain_chain" not in st.session_state:
    st.session_state.langchain_chain = None

if "llama_engine" not in st.session_state:
    st.session_state.llama_engine = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------------------------------------------------
# LangChain Chatbot
# ---------------------------------------------------------
def get_langchain_bot():
    if st.session_state.langchain_chain is None:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=api_key
        )
        memory = ConversationBufferMemory()
        st.session_state.langchain_chain = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=True
        )
    return st.session_state.langchain_chain


# ---------------------------------------------------------
# LlamaIndex Chatbot
# ---------------------------------------------------------
def get_llama_bot():
    if st.session_state.llama_engine is None:
        Settings.llm = OpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=api_key
        )
        memory = ChatMemoryBuffer.from_defaults(token_limit=3000)
        st.session_state.llama_engine = SimpleChatEngine.from_defaults(
            llm=Settings.llm,
            memory=memory
        )
    return st.session_state.llama_engine


# ---------------------------------------------------------
# Sidebar Model Selection
# ---------------------------------------------------------
model_choice = st.sidebar.selectbox(
    "Choose Chat Model",
    ["LangChain", "LlamaIndex"],
)

# Reset bot when model changes
if model_choice != st.session_state.model:
    st.session_state.model = model_choice
    st.session_state.chat_history = []
    st.session_state.langchain_chain = None
    st.session_state.llama_engine = None


st.write(f"### Active Model: `{st.session_state.model}`")


# ---------------------------------------------------------
# Chat Interface
# ---------------------------------------------------------
user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Select Chat Engine
        if st.session_state.model == "LangChain":
            bot = get_langchain_bot()
            response = bot.predict(input=user_input)

        elif st.session_state.model == "LlamaIndex":
            bot = get_llama_bot()
            response = bot.chat(user_input)

        # Store chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", str(response)))


# ---------------------------------------------------------
# Display Chat History
# ---------------------------------------------------------
st.write("### Chat History")
if len(st.session_state.chat_history) == 0:
    st.info("Start chatting...")
else:
    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 Bot:** {msg}")
