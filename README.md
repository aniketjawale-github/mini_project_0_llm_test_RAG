# 🧠 LLM Reality Check — Understanding the Need for RAG

## 📌 Overview

This project is a beginner-friendly Python experiment that demonstrates the **limitations of Large Language Models (LLMs) when used without Retrieval-Augmented Generation (RAG)**.

The goal is to **intentionally expose hallucinations and overconfidence** in LLM responses when:
- No external data is provided
- No embeddings are used
- No vector database is involved
- No document retrieval is performed

This project builds **strong fundamentals** before moving into full RAG systems.

---

## 🎯 Learning Objectives

By completing this project, you will learn:

- Why LLMs hallucinate without external knowledge
- Why prompt engineering alone cannot ensure correctness
- How LLM confidence does NOT equal factual accuracy
- Why Retrieval-Augmented Generation (RAG) is required

---

## 🧩 Project Structure

```text
mini-project-llm-without-rag/
├── main.py                  # Main experiment script
├── private_data.txt         # Ground truth (never sent to LLM)
├── observations.md          # Manual learning notes
└── llm_test_results.txt     # Auto-generated model outputs
