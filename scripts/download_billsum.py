from datasets import load_dataset

# Load the dataset
dataset = load_dataset("billsum", split="train")

# Save 10 sample docs
sample_data = dataset.select(range(10))
sample_data.to_json("data/raw/billsum_sample.json")