# Faith
> An experimental chatbot built to get hands-on with the **RAG** (Retrieval-Augmented Generation) concept and compare different implementations, using the **llama3.1:8b** and **llama3.2:latest** LLMs via Ollama

## Description
**Faith** is an educational project designed to explore the world of **RAG** (Retrieval-Augmented Generation) from the ground up. The goal is to build a chatbot capable of answering questions based on a user-provided document set, using two different LLMs (llama3.1:8b and llama3.2:latest) and experimenting with various retrieval strategies (e.g., sentence-transformers embeddings, FAISS or ChromaDB vector indexing, re-ranking, etc.).

This project is not intended for production use, but rather to:
- Understand the complete RAG pipeline (indexing → retrieval → generation).
- Compare the two models in terms of response quality, speed, and memory usage.
- Experiment with parameters such as chunk size, top-k, and embedding types.