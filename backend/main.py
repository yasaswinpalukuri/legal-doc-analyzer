from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI-powered Legal Document Analyzer",
    description="Summarizes legal text, extracts clauses, and flags risky terms.",
    version="0.1.0"
)

class SummaryRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API is up and running."}

@app.post("/summarize")
def dummy_summarize(request: SummaryRequest):
    # This is a placeholder - real model integration coming next!
    return {
        "summary": "This is a placeholder summary.",
        "input_length": len(request.text)
    }