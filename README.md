# 🤖 AI-powered Legal Document Analyzer

This tool uses AI to simplify legal documents. Upload a contract and receive a clean summary, extracted clauses (like penalties or durations), and flagged risky terms.

---

## 🔍 Features
- 📄 Upload legal documents (PDF/text)
- 🧠 Summarize content with HuggingFace Transformers
- 🔍 Extract clauses like:
  - Duration
  - Obligations
  - Penalties
- 🚩 Flag risky language (e.g., “indemnify”, “auto-renewal”)

---

## 🧠 Tech Stack
| Layer     | Tool                    |
|-----------|-------------------------|
| Backend   | FastAPI (Python)        |
| NLP       | HuggingFace Transformers (BART) |
| Frontend  | HTML/CSS or React       |
| Database  | SQLite or MongoDB       |
| Hosting   | AWS Free Tier (EC2/S3)  |

---

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/AI-powered-Legal-Document-Analyzer.git
cd backend
pip install -r ../requirements.txt
uvicorn main:app --reload
```

- Swagger: http://127.0.0.1:8000/docs  
- Health check: http://127.0.0.1:8000/health

---

## 📍 Roadmap
- [x] Project setup
- [x] FastAPI backend with dummy endpoints
- [ ] Summarization with HuggingFace
- [ ] Clause extraction (NER + regex)
- [ ] Risk flagging
- [ ] Frontend UI
- [ ] AWS deployment
- [ ] Open-source launch

---

## 📄 License
MIT

## 👤 Author
Yasaswin Palukuri