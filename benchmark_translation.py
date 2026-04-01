import time
import tiktoken
from tabulate import tabulate
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import functools

@functools.lru_cache(maxsize=None)
def get_encoding_cached(model: str = "cl100k_base"):
    return tiktoken.get_encoding(model)

def count_tokens(text: str, model: str = "cl100k_base") -> int:
    """Counts tokens in a string using tiktoken."""
    enc = get_encoding_cached(model)
    return len(enc.encode(text))

def translate_english_to_zhiwen_local(english_text: str, pipe) -> tuple[str, float]:
    """Uses a pre-loaded local transformers pipeline to translate text."""
    start_time = time.time()

    try:
        system_prompt = (
            "Translate the following English text into Classical Chinese (文言文) "
            "following the ZhiWen protocol. Keep it extremely brief, use single-character words "
            "where possible, omit subjects/objects when clear from context, and output ONLY the translated text without any explanation."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": english_text},
        ]

        output = pipe(messages, max_new_tokens=50, temperature=0.1, return_full_text=False)
        result = output[0]["generated_text"].strip()

    except Exception as e:
        result = f"ERROR_{str(e)}"

    latency = time.time() - start_time
    return result, latency

def run_benchmark():
    from transformers import pipeline

    test_cases = [
        "The user is very frustrated because the code keeps breaking. You need to calm them down and provide a step-by-step fix using Python.",
        "Please generate a complete system architecture report detailing the microservices and their dependencies.",
        "I am confused about how to use the empathic reasoning chain in this protocol."
    ]

    # 9 models for the benchmark
    models = [
        "Qwen/Qwen2.5-0.5B-Instruct",
        "HuggingFaceTB/SmolLM2-135M-Instruct",
        "Qwen/Qwen2.5-1.5B-Instruct",
        "HuggingFaceTB/SmolLM2-360M-Instruct",
        "Qwen/Qwen2.5-Coder-0.5B-Instruct",
        "Qwen/Qwen2.5-Math-1.5B-Instruct",
        "allenai/OLMo-1B-0724-Instruct",
        "Qwen/Qwen1.5-0.5B-Chat",
        "Qwen/Qwen1.5-1.8B-Chat"
    ]

    from sentence_transformers import SentenceTransformer

    # Use Universal Sentence Encoder equivalent via sentence-transformers
    print("Loading Universal Sentence Encoder equivalent for similarity scoring...")
    embed = SentenceTransformer('sentence-transformers/use-cmlm-multilingual')

    def use_similarity(text1, text2):
        if not text1 or not text2:
            return 0.0
        embeddings = embed.encode([text1, text2])
        sim = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        return float(sim)

    encoder = use_similarity

    all_results = []

    print("Benchmarking English to ZhiWen Translation using local models...")

    for model in models:
        print(f"\nLoading model: {model}")
        try:
            # Setting truncation and ignoring long prompts to avoid warnings/errors
            pipe = pipeline("text-generation", model=model, device="cpu", truncation=True)
        except Exception as e:
            print(f"Failed to load model {model}: {e}")
            continue

        print(f"Benchmarking model: {model}")
        for i, case in enumerate(test_cases):
            eng_tokens = count_tokens(case)

            zw_text, latency = translate_english_to_zhiwen_local(case, pipe)

            if "ERROR_" in zw_text:
                zw_tokens = 0
                reduction = 0.0
                similarity = 0.0
            else:
                zw_tokens = count_tokens(zw_text)
                reduction = (1 - (zw_tokens / eng_tokens)) * 100 if eng_tokens > 0 else 0
                similarity = encoder(case, zw_text)

            # Shorten output for display
            display_text = zw_text.replace('\n', ' ')
            if len(display_text) > 20:
                display_text = display_text[:17] + "..."

            all_results.append([
                model.split('/')[-1],
                eng_tokens,
                zw_tokens,
                f"{reduction:.2f}%",
                f"{similarity:.4f}",
                f"{latency:.3f}s",
                display_text
            ])

            # Sleep briefly to avoid rate limits
            time.sleep(1)

    headers = ["Model", "Eng Toks", "ZW Toks", "Reduction", "Similarity", "Latency", "Result Preview"]
    table_output = tabulate(all_results, headers=headers, tablefmt="github")

    print("\n" + table_output)

    # Write report
    report_path = "TRANSLATION_BENCHMARK_REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# English to ZhiWen Translation Benchmark Report\n\n")
        f.write("This report details the token efficiency, latency, and semantic similarity of translating English prompts into dense Classical Chinese (ZhiWen) across 9 small local models.\n\n")
        f.write("Semantic similarity is calculated using Universal Sentence Encoder (USE) Multilingual (`tensorflow_hub`).\n\n")
        f.write(table_output)
        f.write("\n")

    print(f"\nReport written to {report_path}")

if __name__ == "__main__":
    run_benchmark()
