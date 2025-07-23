Week-by-Week Roadmap (1 Hour/Day × 4 Days)
🟢 Week 1 – Foundation & Planning
Day 1 (Mon): Project Setup + Goal Framing
Create GitHub repo (legal-doc-analyzer)

Set up folder structure: backend/, frontend/, data/, docs/

Initialize README with:

✍️ Project summary

✅ Problem it solves

🧠 Key features

✍️ Add LICENSE, .gitignore, and requirements.txt

🚀 Learn: What makes a good open-source README?

Day 2 (Tue): FastAPI + Basic Server
Build a /health endpoint

Add /summarize dummy POST endpoint (returning dummy summary)

Test locally with curl or Postman

🚀 Learn: FastAPI vs Flask — why FastAPI is better for async, type-safe APIs

Day 3 (Thu): HuggingFace Summarizer
Use transformers (e.g., bart-large-cnn) to summarize sample legal text

Add real summarization to /summarize endpoint

🚀 Learn: What makes a good legal summarizer? Trade-offs of abstractive vs extractive summarization

Day 4 (Fri): Commit, Push + Tracker
Push changes to GitHub

Set up GitHub Projects board (or Notion kanban)

Add columns: Backlog, In Progress, Testing, Done

🚀 Learn: Branching strategy, commit message standards, changelog format

🔵 Week 2 – Clause Extraction & Risk Flagging
Day 5 (Mon): Named Entity Recognition (NER)
Integrate HuggingFace NER model (dslim/bert-base-NER)

Test NER on legal phrases (e.g., “termination after 30 days”)

🚀 Learn: NER limitations — domain generalization, misclassifications

Day 6 (Tue): Key Clause Extractor
Write rule-based extractors (e.g., regex + model-assisted)

Detect: duration, penalties, parties involved, effective dates

Return as structured JSON

🚀 Learn: Combining NER + regex for high accuracy

Day 7 (Thu): Risky Term Flagging
Maintain a list of “risky terms” (e.g., "indemnify", "arbitration", "termination without notice")

Highlight them in output with explanations

🚀 Learn: Basics of legal NLP risk scoring

Day 8 (Fri): Save to DB (SQLite/MongoDB)
Store summary, extracted clauses, and flagged risks

Design a simple schema (JSON blob or normalized table)

🚀 Learn: SQLite vs MongoDB pros/cons (lightweight storage options)

🟠 Week 3 – Frontend + Integration
Day 9 (Mon): HTML/CSS or React Frontend
Build upload form (PDF/Text), display results

Optionally use PDF.js or extract text on backend

🚀 Learn: React vs plain HTML — tradeoffs in simplicity vs interactivity

Day 10 (Tue): Connect Frontend to FastAPI
Use fetch() in frontend to POST file/text

Show summary, clauses, risks with basic styling

🚀 Learn: CORS handling + JSON handling between frontend-backend

Day 11 (Thu): Error Handling + Edge Cases
Add backend error responses (e.g., malformed input)

Validate file types, handle empty text

🚀 Learn: Defensive programming for ML APIs

Day 12 (Fri): Push Milestone + GIF Demo
Record 10s screen capture (e.g., LICEcap) of upload → analysis

Add GIF to README

🚀 Learn: How to demo AI tools effectively for GitHub & recruiters

🟣 Week 4 – Deployment + LinkedIn Launch
Day 13 (Mon): AWS Free Tier Setup
Use EC2 or Elastic Beanstalk for FastAPI backend

Optionally serve static frontend from S3

🚀 Learn: Serverless vs EC2, deploying with uvicorn + Nginx

Day 14 (Tue): Final Touches
Add /docs with FastAPI auto-generated Swagger

Add examples to README:

📄 Sample contract

📋 Example API input & output

Finalize CHANGELOG.md

Day 15 (Thu): Testing + Feedback
Test app end-to-end

Share repo with peers for 1st review

Open GitHub issues for improvement

🚀 Learn: Open-source maintenance and documentation best practices

Day 16 (Fri): Write LinkedIn Article
Title: “I Built a Legal Document Analyzer Using AI – Here’s What I Learned”

Include:

Problem: “Legal contracts are complex”

Demo GIF + GitHub link

What you learned (FastAPI, NLP, deployment)

Impact vision: democratize legal understanding

🚀 Learn: Thought-leadership writing for career building