import os
import json
import csv
import argparse
from pathlib import Path

def process_moltbook(input_csv: str, out_dir: str, limit: int = 100):
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            if count >= limit:
                break

            agent_name = row.get("agent_name", "UnknownAgent")
            title = row.get("title", "No Title")
            content = row.get("content", "")

            # Write .zw file
            zw_content = f"""#角色 {agent_name}

#上下文
  {title}

#输出 {content}
"""

            # Write .json file
            json_obj = {
                "role": agent_name,
                "context": title,
                "output_format": content
            }
            json_content = json.dumps(json_obj, indent=2, ensure_ascii=False)

            base_name = f"post_{count:04d}"
            with open(out_path / f"{base_name}.zw", "w", encoding="utf-8") as out_zw:
                out_zw.write(zw_content)
            with open(out_path / f"{base_name}.json", "w", encoding="utf-8") as out_json:
                out_json.write(json_content)

            count += 1

    print(f"Processed {count} posts into {out_dir}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Moltbook posts for benchmarking")
    parser.add_argument("--input", default="moltbook-observatory/sample_data/moltbook_posts.csv", help="Input CSV file")
    parser.add_argument("--out", default="moltbook_data", help="Output directory")
    parser.add_argument("--limit", type=int, default=100, help="Number of posts to process")
    args = parser.parse_args()

    process_moltbook(args.input, args.out, args.limit)
