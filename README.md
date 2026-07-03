# 🎬 Semantic Movie Recommendation System

A content-based movie recommendation engine built with **sentence-transformer embeddings** and **Elasticsearch vector search**, combining dense vector similarity with traditional filtering for hybrid retrieval. Built as a hands-on learning project to explore embeddings, vector databases, and semantic search — a companion track to a broader LLM/RAG/agentic AI learning sprint.

---

## 📌 Overview

Traditional recommendation systems rely on collaborative filtering or exact keyword matches, which often miss movies that are *thematically* similar but described differently. This project instead encodes movie metadata (overview, genres, keywords) into dense vector embeddings using `sentence-transformers`, indexes them in Elasticsearch using `dense_vector` fields, and performs **k-NN semantic search** to surface movies that are conceptually similar — not just textually similar.

**Datasets used:**
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)

---

## ✨ Features

- 🔍 **Semantic search** — find movies by meaning/theme, not just keyword overlap
- 🧠 **Dense vector embeddings** generated via `sentence-transformers`
- ⚡ **Elasticsearch k-NN search** for fast approximate nearest-neighbor retrieval
- 🎯 **Hybrid retrieval** — combines vector similarity with structured filters (genre, language, release year, etc.)
- 📊 Clean, reproducible data pipeline from raw CSV → cleaned DataFrame → indexed documents

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────────┐     ┌────────────────────┐
│  TMDB / ML CSV   │ --> │  Data Cleaning &      │ --> │  Sentence-         │
│  Raw Datasets    │     │  Preprocessing        │     │  Transformer Model │
└─────────────────┘     │  (pandas)             │     │  (embeddings)      │
                         └──────────────────────┘     └──────────┬─────────┘
                                                                    │
                                                                    ▼
                         ┌──────────────────────┐     ┌────────────────────┐
                         │  Elasticsearch Index   │ <-- │  Bulk Indexing     │
                         │  (dense_vector field)  │     │  (es.index / bulk) │
                         └──────────┬─────────────┘     └────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  k-NN Query Layer      │
                         │  (semantic search API) │
                         └──────────────────────┘
```

---

## 🛠️ Tech Stack

| Component        | Technology                          |
|-------------------|--------------------------------------|
| Language           | Python                              |
| Embeddings         | `sentence-transformers`             |
| Vector Search       | Elasticsearch 9.4.3 (dense_vector, k-NN) |
| Data Handling       | pandas                              |
| Dev Environment     | Jupyter Notebook / VS Code          |
| Visualization (opt.)| Kibana                              |

---

## 📂 Project Structure

```
movie-recommendation-system/
├── tmdb_5000_movies.csv     # Raw TMDB dataset
├── abc.ipynb                # Data exploration / development notebook
├── index.py                 # Elasticsearch index creation & mapping definition
├── sample_index.py          # Sample/test indexing script
├── application.py           # Main application — embedding + search logic
├── requirements.txt
└── README.md
```
> `tempCodeRunnerFile.py` is an auto-generated VS Code temp file — add it to `.gitignore` rather than committing it (see note below).

---

## 🧠 Key Learnings

- Handling `dense_vector` mapping configuration correctly (e.g. `similarity` vs `similarities`)
- Avoiding nested-array pitfalls when batch-encoding text with `sentence-transformers`
- Designing a mapping schema that supports both vector search and structured filtering
- Debugging Elasticsearch client/server version mismatches and Windows-specific path/auth issues

---

## 🚀 Future Improvements

- [ ] Add a simple Streamlit/FastAPI front-end for interactive search
- [ ] Incorporate MovieLens collaborative filtering signals alongside content-based vectors
- [ ] Experiment with re-ranking using cross-encoders
- [ ] Add evaluation metrics (precision@k, recall@k) against a labeled test set

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 🙋 About

Built as part of a self-directed learning sprint into LLMs, RAG, and agentic AI — this project focuses specifically on embeddings and vector search fundamentals as building blocks toward more advanced retrieval-augmented systems.
