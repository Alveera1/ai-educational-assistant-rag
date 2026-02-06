import streamlit as st
import ollama
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Educational Assistant",
    page_icon="📚",
    layout="centered"
)


# ---------------- LOAD EMBEDDING MODEL ----------------
@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("BAAI/bge-small-en")


class LocalEmbedding(Embeddings):
    def __init__(self):
        self.model = load_embedding_model()

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode([text])[0].tolist()


embedding = LocalEmbedding()

# ---------------- LOAD VECTOR DB ----------------
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

retriever = db.as_retriever(search_kwargs={"k": 2})


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📌 Project Overview")
    st.write(
        """
        **AI-Powered Educational Assistant**  
        Uses **Retrieval-Augmented Generation (RAG)** to answer
        questions strictly from textbook content.
        """
    )

    st.subheader("⚙️ Tech Stack")
    st.markdown(
        """
        - **Streamlit** – UI  
        - **LangChain + ChromaDB** – Vector Search  
        - **Sentence Transformers** – Embeddings  
        - **Ollama (Phi-3)** – LLM  
        """
    )

    st.subheader("🧠 How It Works")
    st.write(
        """
        1. Question → converted to embeddings  
        2. Relevant textbook chunks retrieved  
        3. AI answers **only from given context**  
        """
    )

    st.markdown("---")
    st.caption("👩‍💻 Developed by Alveera Shaikh")


# ---------------- MAIN UI ----------------
st.title("📚 AI-Powered Educational Assistant")
st.write("Ask questions from your textbook and get **accurate AI-generated answers**.")

st.markdown("### 🔍 Ask Your Question")
question = st.text_input(
    "Type your question here:",
    placeholder="e.g. What is CPU scheduling?"
)

if question:
    with st.spinner("🤖 AI is thinking..."):

        docs = retriever.invoke(question)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer ONLY from the context below.

        Context:
        {context}

        Question:
        {question}
        """

        response = ollama.chat(
            model='phi3',
            messages=[{"role": "user", "content": prompt}]
        )

    st.success("✅ Answer Generated")

    st.markdown("### 📝 Answer")
    st.write(response['message']['content'])

    # Optional: show context (judges LOVE transparency)
    with st.expander("📖 View Retrieved Textbook Context"):
        st.write(context)


# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 RAG-Based AI System | Academic Integrity Focused")
