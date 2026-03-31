import argparse
import os
import tiktoken
from tabulate import tabulate
from pathlib import Path

def count_tokens(text: str, model: str = "cl100k_base") -> int:
    """Counts tokens in a string using tiktoken."""
    enc = tiktoken.get_encoding(model)
    return len(enc.encode(text))

def analyze_directory(directory_path: str):
    """Analyzes .zw files and compares with their JSON/YAML equivalents."""
    base_dir = Path(directory_path)
    if not base_dir.is_dir():
        print(f"Error: Directory '{directory_path}' not found.")
        return

    results = []

    # Find all .zw files
    for zw_file in base_dir.rglob("*.zw"):
        # Check for equivalents (.json, .yaml, .yml)
        equivalents = []
        for ext in [".json", ".yaml", ".yml"]:
            potential_file = zw_file.with_suffix(ext)
            if potential_file.exists():
                equivalents.append(potential_file)

        if not equivalents:
            print(f"Warning: No equivalent JSON/YAML file found for {zw_file}")
            continue

        # If multiple exist, just pick the first one
        eq_file = equivalents[0]

        try:
            with open(zw_file, 'r', encoding='utf-8') as f:
                zw_content = f.read()
            with open(eq_file, 'r', encoding='utf-8') as f:
                eq_content = f.read()
        except Exception as e:
            print(f"Error reading files for {zw_file.name}: {e}")
            continue

        zw_tokens = count_tokens(zw_content)
        eq_tokens = count_tokens(eq_content)

        if eq_tokens == 0:
            compression = 0.0
        else:
            compression = (1 - (zw_tokens / eq_tokens)) * 100

        results.append([
            zw_file.name,
            eq_file.name,
            zw_tokens,
            eq_tokens,
            f"{compression:.2f}%"
        ])

    if not results:
        print("No paired files found to analyze.")
        return

    headers = ["ZhiWen File", "Equivalent File", "ZhiWen Tokens", "Equivalent Tokens", "Reduction"]
    print("\nToken Cruncher Benchmark Results:\n")
    print(tabulate(results, headers=headers, tablefmt="github"))

    # Calculate averages
    total_zw_tokens = sum(row[2] for row in results)
    total_eq_tokens = sum(row[3] for row in results)
    if total_eq_tokens > 0:
        overall_reduction = (1 - (total_zw_tokens / total_eq_tokens)) * 100
        print(f"\nOverall Tokens (ZhiWen): {total_zw_tokens}")
        print(f"Overall Tokens (Equivalent): {total_eq_tokens}")
        print(f"Overall Reduction: {overall_reduction:.2f}%")
    print()

def main():
    parser = argparse.ArgumentParser(description="ZhiWen Token Cruncher Benchmark Tool")
    parser.add_argument("directory", help="Directory containing ZhiWen samples and JSON/YAML equivalents")
    args = parser.parse_args()

    analyze_directory(args.directory)

if __name__ == "__main__":
    main()
