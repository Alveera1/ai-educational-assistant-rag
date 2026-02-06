from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings
import ollama

# Custom embedding wrapper
class LocalEmbedding(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-en")

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode([text])[0].tolist()


# Load PDF
loader = PyPDFLoader("data/coa.pdf")
documents = loader.load()

# Chunk text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Create vector DB
embedding = LocalEmbedding()

db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="chroma_db"
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# Ask question
query = input("Ask your textbook: ")

relevant_docs = retriever.invoke(query)

context = "\n".join([doc.page_content for doc in relevant_docs])

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

response = ollama.chat(
    model='mistral',
    messages=[{"role": "user", "content": prompt}]
)

print("\nAI Answer:\n")
print(response['message']['content'])
