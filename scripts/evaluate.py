# evaluate.py
import json
from rouge_score import rouge_scorer
import matplotlib.pyplot as plt
import seaborn as sns

def load_summaries(path):
    with open(path, 'r') as f:
        return json.load(f)

def compute_rouge(summaries):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = {'rouge1': [], 'rouge2': [], 'rougeL': []}
    
    for entry in summaries:
        score = scorer.score(entry['reference'], entry['summary'])
        for k in scores:
            scores[k].append(score[k].fmeasure)

    return {k: sum(v)/len(v) for k, v in scores.items()}

def plot_scores(score_dict):
    sns.barplot(x=list(score_dict.keys()), y=list(score_dict.values()))
    plt.title("Average ROUGE Scores")
    plt.ylabel("F1 Score")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig("reports/rouge_scores.png")
    plt.show()

if __name__ == "__main__":
    summaries = load_summaries("data/processed/summaries.json")
    avg_scores = compute_rouge(summaries)
    print("📊 ROUGE Scores:", avg_scores)
    plot_scores(avg_scores)
