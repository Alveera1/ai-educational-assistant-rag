#AI Educational Assistant using Offline RAG#

An intelligent academic assistant that answers student questions directly from textbooks using Retrieval-Augmented Generation (RAG).  
Built to run fully offline — no paid APIs required.


~Problem

Students often rely on AI tools that can generate incorrect or hallucinated answers.  
This creates risk in academic environments where accuracy is critical.


~Solution

This project uses **Retrieval-Augmented Generation (RAG)** to fetch information directly from trusted academic documents before generating responses.

Instead of guessing, the assistant searches your textbook data and then answers — ensuring:

- Higher accuracy  
- Academic reliability  
- Context-based responses  

~Features

✔ Works without paid APIs  
✔ Runs completely offline  
✔ Reduces AI hallucinations  
✔ Fast semantic search  
✔ Simple and clean user interface  
✔ Lightweight — runs on normal laptops  
✔ Easy to customize with your own PDFs  

~Tech Stack

- **Streamlit** — Interactive web interface  
- **Ollama (Phi-3)** — Local Large Language Model  
- **LangChain** — RAG pipeline orchestration  
- **ChromaDB** — Vector database for semantic retrieval  
- **Sentence Transformers** — Text embeddings  

How It Works

```
User Question
     ↓
Text Embedding
     ↓
Vector Database (ChromaDB)
     ↓
Retriever
     ↓
Phi-3 LLM via Ollama
     ↓
Accurate Answer
```

Simple architecture. Professional results.

---
~~ Installation

~Clone the Repository

```bash
git clone https://github.com/your-username/ai-educational-assistant-rag.git
cd ai-educational-assistant-rag
```

~Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

(Mac/Linux: `source venv/bin/activate`)

~Install Requirements

```bash
pip install -r requirements.txt
```

~Install Ollama

Download from:

👉 https://ollama.com

~Pull the Phi-3 model:

```bash
ollama pull phi3
```
---

Add Your PDFs
~Place your textbooks inside the:

```
data/
```

folder.

~Create the Vector Database

Run:

```bash
python app.py
```

(This converts your PDFs into searchable embeddings.)

---
~Start the App

```bash
streamlit run app.py
```

Open the local URL shown in the terminal — your AI assistant is ready 🎉

~Use Cases

- College exam preparation  
- Concept revision  
- Doubt solving from textbooks  
- Offline academic environments  
- Privacy-focused learning  


~Future Improvements

- Chat memory  
- Multi-PDF querying  
- Voice input  
- Mobile-friendly UI  
- Advanced citation support  


~Contributing

Contributions are welcome!  
Feel free to fork this repository and submit a pull request.


