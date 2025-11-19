# 🤖 Multi-Model AI Chatbot (LangChain + LlamaIndex)

This project is a **Streamlit-based conversational AI chatbot** that allows users to **switch dynamically between two powerful frameworks**:

- **LangChain** (with OpenAI Chat Models)
- **LlamaIndex** (SimpleChatEngine with memory)

The chatbot includes **conversation memory**, **model switching**, and a clean chat UI — all powered from a single `app.py`.

---

## 🚀 Features

### 🔄 **Model Switching (Unique Feature)**
Easily switch between:
- **LangChain**
- **LlamaIndex**

Each model maintains **its own memory buffer**, and switching automatically resets conversation state.

### 💬 **Full Chat Interface**
- Chat UI in Streamlit  
- Conversation history  
- Dynamic responses  
- Clean UI  

### 🧠 **Memory Support**
- LangChain → `ConversationBufferMemory`
- LlamaIndex → `ChatMemoryBuffer`

### 🔐 **Secure API Key Handling**
Supports:
- `.env` (local development)
- `st.secrets` (Streamlit Cloud)

---

## 🏗️ Project Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4d2b645b-9e50-48db-84df-2dde3edef3e3" />

🏁 Live Demo
🌍 Deployed Endpoint:
https://ic-langchain-stremlit-fyhznguu85zbbvsjxs88nk.streamlit.app/

🧠 Try both LangChain and LlamaIndex models from the dropdown in the UI.

📚 Example Output
🔹 LangChain Chat
<img width="1231" height="569" alt="image" src="https://github.com/user-attachments/assets/76663c08-e5d9-449b-9ddb-cc15a170f767" />

🔹 LlamaIndex Chat
<img width="1110" height="635" alt="image" src="https://github.com/user-attachments/assets/d4b270fc-12b4-4905-94a0-a5dee5f48cf3" />
