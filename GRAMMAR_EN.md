# Classical Chinese Grammar for ZhiWen

The ZhiWen (AgentLang) protocol relies on **Classical Chinese (文言文 - Wényánwén)** to achieve its extreme token density. To write truly efficient ZhiWen files, you must move away from conversational English (or even modern conversational Chinese) and embrace the elegant, compressed grammar of classical text.

This guide introduces the core grammatical principles of Classical Chinese for English speakers writing for AI agents.

---

## 1. The Core Principle: Extreme Omission (Ellipsis)

In English, grammar requires subjects, pronouns, and filler words to make a sentence complete. In Classical Chinese, **if the context implies it, you delete it.**

### Omit the Subject
If it's obvious who is acting, drop the pronoun entirely.
*   **English:** `The user asked a question.` (5 words / ~5 tokens)
*   **Modern Chinese:** `用户问了一个问题。` (8 chars / ~5 tokens)
*   **Classical Chinese:** `客问。` (2 chars / ~2 tokens) *Literally: "Guest asks."*

### Omit "It", "Them", "Him", "Her"
Objects are also routinely dropped if understood.
*   **English:** `I saw the error and I fixed it.`
*   **Classical Chinese:** `见错，改之。` (4 chars / ~3 tokens) *Literally: "See error, fix it." (`之` acts as a generic "it").*

---

## 2. Single-Character Words (Monosyllabism)

Modern Chinese relies heavily on two-character words to avoid ambiguity in spoken language (e.g., `喜欢` for like, `知道` for know). Classical Chinese overwhelmingly prefers **single characters**, because in written text, context clarifies the meaning.

For Agent prompting, use single-character equivalents:

| English | Modern Chinese (Verb) | Classical Chinese (Verb) |
| :--- | :--- | :--- |
| To know/understand | 知道 (zhīdào) | **知** (zhī) |
| To say/speak | 说话 (shuōhuà) | **言** (yán) / **曰** (yuē) |
| To make/do | 制作 (zhìzuò) | **作** (zuò) / **为** (wéi) |
| To see/observe | 看见 (kànjiàn) | **观** (guān) / **见** (jiàn) |
| To feel/sense | 感觉 (gǎnjué) | **感** (gǎn) |
| To ask/request | 请求 (qǐngqiú) | **请** (qǐng) |

**Example in ZhiWen:**
*   Instead of: `#感 感觉到用户的愤怒` *(Feel the user's anger)*
*   Write: `#感 察其怒` *(Observe their anger - 3 characters)*

---

## 3. Grammatical Flexibility (Parts of Speech)

In English, words usually have fixed parts of speech (a noun is a noun, a verb is a verb). In Classical Chinese, **any word can change its part of speech depending on its position in the sentence.**

### Nouns acting as Verbs
You can use a noun to describe an action associated with that noun.
*   **Word:** `衣` (yī) - Noun: Clothes.
*   **Usage:** `衣人` (yì rén) - Verb: To clothe someone.
*   **Agent Context:** `代码` (Code). `代码之` -> "Code it."

### Adjectives acting as Verbs
You can use an adjective to mean "to consider something [adjective]" or "to make something [adjective]".
*   **Word:** `善` (shàn) - Adjective: Good.
*   **Usage:** `善之` - Verb: To consider it good / to approve of it.
*   **Agent Context:** `简` (Simple). `简其辞` -> "Simplify its words/output."

---

## 4. The Essential Particles (虚词 - Xūcí)

While Classical Chinese omits filler words, it relies on a few crucial "empty words" (particles) to structure the sentence mathematically. Master these, and you can write highly complex instructions in very few tokens.

### 之 (zhī) - The Connector and Pronoun
1.  **Possessive (like 's or 'of'):**
    `用户之需` (The user's need).
2.  **Object Pronoun (him/her/it/them):**
    `改之` (Fix it). `助之` (Help them).

### 其 (qí) - The Pronoun "His/Her/Its/Their"
Used to show possession or identify a subject in a sub-clause.
*   `察其意` (Observe their intent).
*   `知其不可` (Know that it is impossible).

### 以 (yǐ) - The Instrument "With / By means of / In order to"
Crucial for telling the agent *how* to do something.
*   `以示例答` (Answer *with* examples).
*   `以安其心` (*In order to* calm their mind).

### 则 (zé) - The Conditional "Then"
Used for IF -> THEN logic.
*   `若报错，则止` (If it errors, *then* stop).

### 而 (ér) - The Conjunction "And / But"
Connects two verbs or clauses. It can mean sequence ("and then") or contrast ("but").
*   **Sequence:** `学而时习之` (Learn *and* constantly practice it).
*   **Contrast:** `观而不语` (Observe *but* do not speak).

### 矣 (yǐ) - The Completion Marker
Placed at the end of a sentence to indicate a change of state or a completed action (similar to modern `了`).
*   `事成矣` (The task is completed).

---

## 5. Practical Agent Framing (The 4-Character Idiom Style)

Because Classical Chinese is so dense, it often falls into rhythmic 4-character structures (成语 - Chéngyǔ). This is highly token-efficient and structurally clear to LLMs.

When formulating ZhiWen directives, aim for 4-character phrases:

*   **Need brevity?** `言简意赅` (Words simple, meaning complete).
*   **Need step-by-step?** `循序渐进` (Follow sequence, gradually advance).
*   **Need code only?** `唯出代码` (Only output code).

### A Before & After Example

**English Prompt (~30 tokens):**
> "The user is very frustrated because the code keeps breaking. You need to calm them down and provide a step-by-step fix using Python."

**Modern Chinese Prompt (~20 tokens):**
> "用户因为代码一直报错非常沮丧。你需要安抚他们，并提供一个使用Python的逐步修复方案。"

**Classical Chinese (ZhiWen Style) (~8 tokens):**
> `察其受挫。当安其心，以Python步步解之。`
> *(Observe their frustration. Should calm their mind, with Python step-by-step solve it.)*

By mastering these classical structures, you maximize the "Density" principle of ZhiWen, reducing token spend while giving the AI precise, elegant instructions.