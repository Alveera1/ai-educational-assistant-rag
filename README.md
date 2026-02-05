~AI-Powered Educational Assistant using Offline RAG
An intelligent academic assistant that answers student questions directly from textbooks using Retrieval-Augmented Generation (RAG).  
Built to run fully offline — no paid APIs required.
Designed to provide fact-grounded academic answers by preventing LLM hallucinations through retrieval-based generation.

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
✔ Optimized for local execution on standard laptops
 
✔ Easy to customize with your own PDFs  


~Tech Stack

- **Streamlit** — Interactive web interface  
- **Ollama (Phi-3)** — Local Large Language Model  
- **LangChain** — RAG pipeline orchestration  
- **ChromaDB** — Vector database for semantic retrieval  
- **Sentence Transformers** — Text embeddings  

~How It Works

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

Simple architecture.

~Installation

1)Clone the Repository

```bash
git clone https://github.com/your-username/ai-educational-assistant-rag.git
cd ai-educational-assistant-rag
```

2)Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

(Mac/Linux: `source venv/bin/activate`)


3)Install Requirements

```bash
pip install -r requirements.txt
```

---

4)Install Ollama

Download from:

👉 https://ollama.com

Pull the Phi-3 model:

```bash
ollama pull phi3
```

5)Add Your PDFs

Place your textbooks inside the:

```
data/
```

folder.

6)Create the Vector Database

Run:

```bash
python rag.py
```

(This converts your PDFs into searchable embeddings.)

---

6)Start the App

```bash
streamlit run app.py
```

Open the local URL shown in the terminal — your AI assistant is ready 🎉

<img width="1365" height="719" alt="Screenshot 2026-02-05 232347" src="https://github.com/user-attachments/assets/312e39e6-e8cc-4a79-a880-751eddca58e0" />
<img width="1366" height="706" alt="Screenshot 2026-02-05 232409" src="https://github.com/user-attachments/assets/7a141b8f-800c-415f-9ff8-6437c37424c3" />
<img width="1365" height="721" alt="Screenshot 2026-02-05 232243" src="https://github.com/user-attachments/assets/fabda0c4-1bf1-40df-b333-c8501ab829ab" />
<img width="1365" height="722" alt="Screenshot 2026-02-05 232314" src="https://github.com/user-attachments/assets/fb56bb3e-a2a7-486c-bed3-d95592fcf51b" />




~Use Cases

- College exam preparation  
- Concept revision  
- Doubt solving from textbooks  
- Offline academic environments  
- Privacy-focused learning
- Retrieval-based answer grounding


~Future Improvements

- Chat memory  
- Multi-PDF querying  
- Voice input  
- Mobile-friendly UI  
- Advanced citation support  

~ Contributing

Contributions are welcome!  
Feel free to fork this repository and submit a pull request.


~License

This project is open-source and available under the MIT License.

