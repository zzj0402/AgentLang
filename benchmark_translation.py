import time
import tiktoken
from tabulate import tabulate

def count_tokens(text: str, model: str = "cl100k_base") -> int:
    """Counts tokens in a string using tiktoken."""
    enc = tiktoken.get_encoding(model)
    return len(enc.encode(text))

import os

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

    # Using small/quantized models that can be run locally on CPU for benchmarking
    # We include Qwen (strong in Chinese) and SmolLM2
    models = [
        "Qwen/Qwen2.5-0.5B-Instruct",
        "HuggingFaceTB/SmolLM2-135M-Instruct"
    ]

    all_results = []

    print("Benchmarking English to ZhiWen Translation using local models...")

    for model in models:
        print(f"\nLoading model: {model}")
        try:
            pipe = pipeline("text-generation", model=model, device="cpu")
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
            else:
                zw_tokens = count_tokens(zw_text)
                reduction = (1 - (zw_tokens / eng_tokens)) * 100 if eng_tokens > 0 else 0

            # Shorten output for display
            display_text = zw_text.replace('\n', ' ')
            if len(display_text) > 20:
                display_text = display_text[:17] + "..."

            all_results.append([
                model.split('/')[-1],
                eng_tokens,
                zw_tokens,
                f"{reduction:.2f}%",
                f"{latency:.3f}s",
                display_text
            ])

            # Sleep briefly to avoid rate limits
            time.sleep(1)

    headers = ["Model", "Eng Toks", "ZW Toks", "Reduction", "Latency", "Result Preview"]
    print("\n" + tabulate(all_results, headers=headers, tablefmt="github"))

if __name__ == "__main__":
    run_benchmark()
