import json
import tiktoken
from tabulate import tabulate

def count_tokens(text: str, model: str = "cl100k_base") -> int:
    enc = tiktoken.get_encoding(model)
    return len(enc.encode(text))

def generate_large_prompt(round_idx, lang="zh"):
    if lang == "zh":
        return f"这是第{round_idx}轮的深度分析报告。我们观察到系统在处理大规模并发请求时出现了明显的延迟峰值。根据架构师的初步诊断，这可能与数据库连接池的耗尽有关。我们需要立即审查当前微服务之间的依赖拓扑图，并考虑引入一种更有效的熔断机制以防止级联故障。此外，考虑到内存泄漏的历史记录，建议在测试环境中运行全面的静态分析工具以确保没有任何未释放的资源。"
    else:
        return f"This is the in-depth analysis report for round {round_idx}. We have observed significant latency spikes when the system processes large-scale concurrent requests. According to the architect's preliminary diagnosis, this may be related to the exhaustion of the database connection pool. We need to immediately review the dependency topology graph among the current microservices and consider introducing a more effective circuit breaker mechanism to prevent cascading failures. In addition, considering the history of memory leaks, it is recommended to run comprehensive static analysis tools in the test environment to ensure there are no unreleased resources."

def generate_999_rounds():
    """Generates 999 rounds of large prompts in 3 formats."""

    zw_content = "#上下文\n"
    json_zh_arr = []
    json_en_arr = []

    for i in range(1, 1000):
        agent = "分析师A" if i % 2 != 0 else "架构师B"
        agent_en = "AnalystA" if i % 2 != 0 else "ArchitectB"

        zh_text = generate_large_prompt(i, "zh")
        en_text = generate_large_prompt(i, "en")

        # 1. ZhiWen Format (Dense, Chinese text)
        zw_content += f"  {agent}: {zh_text}\n"

        # 2. JSON Format (Simplified Chinese text)
        json_zh_arr.append({
            "sender": agent,
            "message": zh_text
        })

        # 3. JSON Format (English text)
        json_en_arr.append({
            "sender": agent_en,
            "message": en_text
        })

    # Wrap ZhiWen
    zw_full = f"""#角色 系统架构监控平台

{zw_content}

#输出 生成最终的系统架构优化报告并提出明确的实施计划
"""

    # Wrap JSONs
    json_zh_full = json.dumps({
        "role": "系统架构监控平台",
        "context": json_zh_arr,
        "output_format": "生成最终的系统架构优化报告并提出明确的实施计划"
    }, indent=2, ensure_ascii=False)

    json_en_full = json.dumps({
        "role": "System Architecture Monitoring Platform",
        "context": json_en_arr,
        "output_format": "Generate the final system architecture optimization report and propose a clear implementation plan"
    }, indent=2, ensure_ascii=False)

    return zw_full, json_zh_full, json_en_full

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Generate 999 rounds of inter-agent communication")
    parser.add_argument("--save", type=str, help="Directory to save the generated files")
    args = parser.parse_args()

    print("Generating 999 rounds of large-prompt inter-agent communication...")
    zw_text, json_zh_text, json_en_text = generate_999_rounds()

    if args.save:
        os.makedirs(args.save, exist_ok=True)
        with open(os.path.join(args.save, "999_rounds.zw"), "w", encoding="utf-8") as f:
            f.write(zw_text)
        with open(os.path.join(args.save, "999_rounds_zh.json"), "w", encoding="utf-8") as f:
            f.write(json_zh_text)
        with open(os.path.join(args.save, "999_rounds_en.json"), "w", encoding="utf-8") as f:
            f.write(json_en_text)
        print(f"Files saved to {args.save}/")

    zw_tokens = count_tokens(zw_text)
    json_zh_tokens = count_tokens(json_zh_text)
    json_en_tokens = count_tokens(json_en_text)

    print("\nBenchmark Results (999 Rounds, Large Prompts):")

    results = [
        ["ZhiWen (.zw) [Simplified Chinese]", zw_tokens],
        ["JSON (.json) [Simplified Chinese]", json_zh_tokens],
        ["JSON (.json) [English]", json_en_tokens]
    ]

    headers = ["Format", "Tokens (cl100k_base)"]
    print(tabulate(results, headers=headers, tablefmt="github"))

    # Structural Reduction (Chinese JSON vs Chinese ZhiWen)
    struct_red = (1 - (zw_tokens / json_zh_tokens)) * 100

    # Absolute Reduction (English JSON vs Chinese ZhiWen)
    abs_red = (1 - (zw_tokens / json_en_tokens)) * 100

    print(f"\nStructural Overhead Reduction (Chinese JSON -> ZhiWen): {struct_red:.2f}%")
    print(f"Absolute Token Reduction (English JSON -> ZhiWen): {abs_red:.2f}%")
    print(f"Linguistic Bias Penalty (English JSON -> Chinese JSON): {((json_zh_tokens / json_en_tokens) - 1) * 100:.2f}% (Chinese JSON uses more tokens due to tokenizer optimization)")

if __name__ == "__main__":
    main()
