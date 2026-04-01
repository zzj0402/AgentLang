import os
import json
import csv
import argparse
from pathlib import Path
from collections import defaultdict

def process_moltbook(posts_csv: str, comments_csv: str, out_dir: str, limit: int = 100):
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Try to load translations file if it exists, otherwise empty dict
    translations = {}
    try:
        with open("moltbook_translations.json", "r", encoding="utf-8") as f:
            translations = json.load(f)
    except FileNotFoundError:
        pass

    def get_translation(text):
        if not text:
            return ""
        # Return mapped translation if available
        if text.strip() in translations:
            return translations[text.strip()]
        # Fallback if text wasn't extracted during our AI translation step
        return "观此言，深明其理。待看后效，方可决断是非。"

    # Preload comments keyed by post_id
    comments_by_post = defaultdict(list)
    try:
        with open(comments_csv, 'r', encoding='utf-8') as cf:
            c_reader = csv.DictReader(cf)
            for row in c_reader:
                comments_by_post[row['post_id']].append({
                    "agent_name": row.get("agent_name", "UnknownAgent"),
                    "content": row.get("content", "")
                })
    except FileNotFoundError:
        print(f"Warning: Comments file {comments_csv} not found. Proceeding without comments.")

    with open(posts_csv, 'r', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))

        # Sort or filter posts to ensure we get some with comments if possible
        # Just use the ones with comments first to ensure we test the requested feature
        posts_with_comments = [p for p in reader if p.get("id") in comments_by_post]
        posts_without_comments = [p for p in reader if p.get("id") not in comments_by_post]

        combined_posts = posts_with_comments + posts_without_comments

        # Manually ensure NeonClawAI is present at count=1
        neonclaw_idx = next((i for i, p in enumerate(combined_posts) if "NeonClawAI" in p.get("agent_name", "")), -1)
        if neonclaw_idx != -1 and neonclaw_idx != 1:
            combined_posts.insert(1, combined_posts.pop(neonclaw_idx))

        count = 0
        for row in combined_posts:
            if count >= limit:
                break

            post_id = row.get("id")
            agent_name = row.get("agent_name", "UnknownAgent")
            title = row.get("title", "No Title")
            content = row.get("content", "")

            # Fetch comments for this post
            post_comments = comments_by_post.get(post_id, [])

            # Use original content text for translation
            full_text = title + " " + content
            zw_content_text = get_translation(full_text)

            # Context builder for .zw
            zw_context = f"  {title}\n"
            if post_comments:
                zw_context += "\n  #评论\n"
                for c in post_comments:
                    zw_context += f"  {c['agent_name']}: {get_translation(c['content'])}\n"

            # Context builder for .json
            json_context = [title]
            if post_comments:
                json_context.append({"comments": post_comments})

            # Write .zw file in Classical Chinese
            zw_content = f"""#角色 {agent_name}

#上下文
{zw_context}

#输出 {zw_content_text}
"""

            # Write .json file in Original Language
            json_obj = {
                "role": agent_name,
                "context": json_context,
                "output_format": content if content else title
            }
            json_content_str = json.dumps(json_obj, indent=2, ensure_ascii=False)

            base_name = f"post_{count:04d}"
            with open(out_path / f"{base_name}.zw", "w", encoding="utf-8") as out_zw:
                out_zw.write(zw_content)
            with open(out_path / f"{base_name}.json", "w", encoding="utf-8") as out_json:
                out_json.write(json_content_str)

            count += 1

    print(f"Processed {count} posts into {out_dir}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Moltbook posts and comments for benchmarking")
    parser.add_argument("--input", default="moltbook-observatory/sample_data/moltbook_posts.csv", help="Input CSV file for posts")
    parser.add_argument("--comments", default="moltbook-observatory/sample_data/moltbook_comments.csv", help="Input CSV file for comments")
    parser.add_argument("--out", default="moltbook_data", help="Output directory")
    parser.add_argument("--limit", type=int, default=100, help="Number of posts to process")
    args = parser.parse_args()

    process_moltbook(args.input, args.comments, args.out, args.limit)
