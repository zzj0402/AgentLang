import argparse
import os
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
import numpy as np

def calculate_similarity(text1: str, text2: str, model) -> float:
    """Calculates cosine similarity between two texts using a sentence transformer model."""
    if not text1.strip() or not text2.strip():
        return 0.0

    # Compute embeddings
    embeddings = model.encode([text1, text2])

    # Calculate cosine similarity between the two embeddings
    # Reshape for sklearn: (1, n_features)
    sim = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return float(sim)

def analyze_directory(directory_path: str, models: list):
    """Analyzes .zw files and compares semantic similarity with JSON/YAML equivalents using multiple models."""
    base_dir = Path(directory_path)
    if not base_dir.is_dir():
        print(f"Error: Directory '{directory_path}' not found.")
        return

    # Find all .zw files and their equivalents first to avoid repeated disk reads
    file_pairs = []
    for zw_file in base_dir.rglob("*.zw"):
        equivalents = []
        for ext in [".json", ".yaml", ".yml"]:
            potential_file = zw_file.with_suffix(ext)
            if potential_file.exists():
                equivalents.append(potential_file)

        if not equivalents:
            print(f"Warning: No equivalent JSON/YAML file found for {zw_file}")
            continue

        eq_file = equivalents[0]

        try:
            with open(zw_file, 'r', encoding='utf-8') as f:
                zw_content = f.read()
            with open(eq_file, 'r', encoding='utf-8') as f:
                eq_content = f.read()

            file_pairs.append({
                'zw_name': zw_file.name,
                'eq_name': eq_file.name,
                'zw_content': zw_content,
                'eq_content': eq_content
            })
        except Exception as e:
            print(f"Error reading files for {zw_file.name}: {e}")
            continue

    if not file_pairs:
        print("No paired files found to analyze.")
        return

    # Evaluate each model
    for model_name in models:
        print(f"\n{'='*50}")
        print(f"Loading embedding model: {model_name}...")
        try:
            model = SentenceTransformer(model_name)
        except Exception as e:
            print(f"Error loading model {model_name}: {e}")
            continue

        results = []
        for pair in file_pairs:
            similarity = calculate_similarity(pair['zw_content'], pair['eq_content'], model)

            results.append([
                pair['zw_name'],
                pair['eq_name'],
                f"{similarity:.4f}"
            ])

        headers = ["ZhiWen File", "Equivalent File", "Cosine Similarity"]
        print(f"\nEmbedding Similarity Benchmark Results (Model: {model_name}):\n")
        print(tabulate(results, headers=headers, tablefmt="github"))

        # Calculate average
        similarities = [float(row[2]) for row in results]
        if similarities:
            avg_sim = sum(similarities) / len(similarities)
            print(f"\nAverage Cosine Similarity ({model_name}): {avg_sim:.4f}")
        print()

def main():
    parser = argparse.ArgumentParser(description="ZhiWen Embedding Similarity Benchmark Tool")
    parser.add_argument("directory", help="Directory containing ZhiWen samples and JSON/YAML equivalents")
    parser.add_argument("--models", nargs='+', default=[
        "paraphrase-multilingual-MiniLM-L12-v2", # Good for bilingual (Chinese/English)
        "all-MiniLM-L6-v2", # Fast and lightweight, proxy for universal sentence encoder speed
        "sentence-transformers/use-cmlm-multilingual" # Universal Sentence Encoder Multilingual HuggingFace port
    ], help="List of SentenceTransformer models to use")

    args = parser.parse_args()

    analyze_directory(args.directory, args.models)

if __name__ == "__main__":
    main()
