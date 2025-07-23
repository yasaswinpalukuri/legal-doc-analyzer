# summarize.py
import json
from transformers import pipeline
from pathlib import Path
import argparse

def load_data(path, num_samples=None):
    with open(path, 'r') as f:
        data = json.load(f)
    return data[:num_samples] if num_samples else data

def summarize_documents(data, model_name="google/pegasus-xsum"):
    summarizer = pipeline("summarization", model=model_name)
    summaries = []
    for doc in data:
        summary = summarizer(doc["text"], truncation=True)[0]["summary_text"]
        summaries.append({
            "title": doc["title"],
            "summary": summary,
            "reference": doc["summary"],
        })
    return summaries

def save_summaries(summaries, out_path):
    with open(out_path, 'w') as f:
        json.dump(summaries, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="google/pegasus-xsum")
    parser.add_argument("--input", default="data/raw/billsum_sample.json")
    parser.add_argument("--output", default="data/processed/summaries.json")
    parser.add_argument("--samples", type=int, default=10)
    args = parser.parse_args()

    data = load_data(args.input, args.samples)
    summaries = summarize_documents(data, model_name=args.model)
    save_summaries(summaries, args.output)
    print(f"✅ Saved {len(summaries)} summaries to {args.output}")
