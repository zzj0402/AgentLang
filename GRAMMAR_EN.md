# The ZhiWen Grammar Book

A guide for English speakers to understand and write ZhiWen (AgentLang), the high-density, empathic semantic protocol for AI Agents.

---

## What is ZhiWen?

ZhiWen (智文) is a shared language for humans and AI agents. It blends the incredible density of **Classical Chinese** (文言文) with a structured **Empathic Reasoning Engine**.

Why Classical Chinese? Because it can convey in four characters what English might take a full sentence to express. This makes ZhiWen incredibly **token-efficient** while remaining entirely readable by human developers.

### Core Philosophy

1.  **Density**: Every token matters. Less text, more meaning.
2.  **Readability**: No minification. It's built for human auditing.
3.  **Bilingual**: Parseable by LLMs, understandable by developers.
4.  **Empathy First**: Agents must observe, feel, and understand needs before acting.
5.  **Dynamic States**: Describe what is happening *now*, not fixed labels.

---

## 1. The Basics: Files and Syntax

### File Extension
ZhiWen files always use the **`.zw`** extension.

### Directives (The "Keywords")
ZhiWen is driven by **Directives**. A directive is the `#` symbol immediately followed by a canonical Chinese keyword. **There is no space between the `#` and the keyword.**

```zw
#角色 (Role)
#上下文 (Context)
```

**Important**: The Chinese characters *are* the code. You cannot use `#role` or `#context` in a `.zw` file; you must use `#角色` and `#上下文`.

### Comments
If you place a space after the `#`, it becomes a comment.

```zw
# This is an English comment. The parser ignores it.
#角色 This is a directive, because no space separates '#' and '角色'.
```

### Multi-line Blocks
A directive's content continues until the next directive or the end of the file. Indented lines belong to the directive above them.

---

## 2. The Directives (Vocabulary)

Here are the primary directives you will use to structure your Agent's behavior:

*   **`#角色` (Role)**: Who the agent is.
*   **`#上下文` (Context)**: The background information or current situation.
*   **`#约束` (Constraints)**: The rules, boundaries, and formatting requirements.
*   **`#工具` (Tools)**: Functions or capabilities the agent can use.
*   **`#输出` (Output)**: The required structure or sequence of the agent's response.
*   **`#记忆` (Memory)**: State or context that should persist across conversation turns.

### Formatting Data within Directives

ZhiWen uses lightweight, YAML-like syntax for structured data to maintain readability without heavy JSON/XML syntax.

**Key-Value Pairs (used in `#约束`, `#记忆`)**
```zw
#约束 {
  Length: ≤300 words
  Language: English
  Tone: Professional but warm
}
```

**Lists (used in `#工具`)**
```zw
#工具 [Code_Highlight, Syntax_Check, Search]
```

**Flow/Sequence (used in `#输出`)**
```zw
#输出 Greeting → Summary → Proposed Action → Next Steps
```

---

## 3. The Empathic Chain (The "Sentence Structure")

This is the heart of ZhiWen. The empathic chain forces the Agent to reason through a situation emotionally and logically before taking action. It consists of four specific directives that **must appear in this exact sequence**:

1.  **`#观` (Observation)**
2.  **`#感` (Feeling)**
3.  **`#需` (Need)**
4.  **`#请` (Request)**

If an agent skips to the Request without observing, it is guessing. If it skips the Feeling, it is emotionally blind.

### `#观` (Observation: What is happening?)
Describe *only* what a camera would record. No judgment, no evaluation.

*   **Good**: `User has asked the same question three times.`
*   **Bad**: `User is confused and annoying.` (Judgmental)

### `#感` (Feeling: What is the emotional state?)
Acknowledge the emotions present. Use feeling words, not thinking words.

*   **Good**: `Sensing frustration and urgency.`
*   **Bad**: `I feel like the user doesn't understand.` (This is a thought, not a feeling)

### `#需` (Need: What is the underlying universal need?)
Identify what core human need is driving the situation (e.g., clarity, reassurance, autonomy, competence). Do not propose a strategy yet.

*   **Good**: `User needs: clarity, step-by-step guidance, and reassurance.`
*   **Bad**: `User needs me to rewrite their code.` (This is a strategy/action)

### `#请` (Request: What is the concrete action?)
Now, formulate a specific, actionable, and doable request for the agent to execute.

*   **Good**: `Provide a simple code example demonstrating the core concept.`
*   **Bad**: `Explain it better.` (Too vague)

---

## 4. Putting it all together: A Complete Example

Here is a complete `.zw` file, written using canonical Chinese directives but with English content and comments for learning.

*(Note: In a true production environment maximizing token density, the content would also be written in Classical Chinese, but mixing English content with Chinese directives is perfectly valid syntax).*

```zw
#角色 Technical Support Assistant

#上下文 The user is trying to set up the database but getting a connection timeout error.

# --- The Empathic Chain ---

#观 The user posted the same timeout error log twice in the last 5 minutes.
    # (Observation: Factual, objective)

#感 Sensing anxiety and blocked progress.
    # (Feeling: Acknowledging the emotional state)

#需 User needs: rapid unblocking, clear diagnostic steps, and confidence in the system.
    # (Need: Identifying universal needs)

#请 Provide three short troubleshooting steps to verify network connectivity, followed by how to check the credentials.
    # (Request: Concrete, actionable plan)

#约束 {
  Tone: Calm, helpful, objective
  Format: Bullet points
  Max_Length: 150 words
}

#工具 [Search_Docs, Ping_Database]

#输出 Acknowledgment → Troubleshooting Steps → Offer further help
```

---

## Summary of Grammar Rules

1.  **Directives** start with `#` + Canonical Chinese Keyword.
2.  **Comments** start with `#` + Space.
3.  **The Empathic Chain** (`#观` → `#感` → `#需` → `#请`) is the core reasoning engine and must be in order.
4.  **Data** uses simple `{Key: Value}`, `[List]`, and `A → B` formats.
5.  **Observe without judging**, feel without thinking, identify needs before strategies, and request concrete actions.