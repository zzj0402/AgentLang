# Dense English Grammar for AgentLang

The AgentLang protocol relies on **Dense English** when writing in the English variant to achieve extreme token density. To write truly efficient files, you must move away from conversational English and embrace an elegant, compressed grammar inspired by classical text.

This guide introduces the core grammatical principles of Dense English for writing to AI agents.

---

## 1. The Core Principle: Extreme Omission (Ellipsis)

In conversational English, grammar requires subjects, articles, and filler words to make a sentence complete. In AgentLang, **if the context implies it, you delete it.**

### Omit the Subject
If it's obvious who is acting, drop the pronoun entirely.
*   **Conversational English:** `The user asked a question.` (5 tokens)
*   **Dense English:** `User asked.` (2 tokens)

### Omit "It", "Them", "Him", "Her"
Objects are also routinely dropped if understood. The object pronoun can be omitted entirely if the action is clear.
*   **Conversational English:** `I saw the error and I fixed it.`
*   **Dense English:** `Saw error, fixed.`

---

## 2. Monosyllabism (Short Words)

Conversational English often relies heavily on multi-syllable words (e.g., `understand` for know). Dense English overwhelmingly prefers **short, punchy words**, because context clarifies the meaning.

For Agent prompting, use single-syllable equivalents:

| Conversational English | Dense English |
| :--- | :--- |
| understand / comprehend | **know** / **grasp** |
| communicate / articulate | **say** / **state** |
| construct / manufacture | **make** / **do** |
| observe / perceive | **see** / **view** |
| experience / perceive | **feel** |
| require / request | **ask** / **need** |

**Example in AgentLang:**
*   Instead of: `#Feel Feeling the user's anger`
*   Write: `#Feel Sense anger`

---

## 3. Grammatical Flexibility (Parts of Speech)

In Dense English, **any word can change its part of speech depending on its position in the sentence.**

### Nouns acting as Verbs
You can use a noun to describe an action associated with that noun.
*   **Conversational English:** `Write the code for it.`
*   **Dense English:** `Code it.`

### Adjectives acting as Verbs
You can use an adjective to mean "to consider something [adjective]" or "to make something [adjective]".
*   **Conversational English:** `Make the output simple.`
*   **Dense English:** `Simplify.`

### Causative Voice
Causative verbs indicate making an object do something or be in a certain state.
*   **Conversational English:** `Make the logic clear.`
*   **Dense English:** `Clarify logic.`

---

## 4. Sentence Structures & Negation

### Judgment Sentences
To say "A is B", conversational English uses verbs like `is` or `are`. Dense English omits the verb "to be" entirely using juxtaposition.
*   **Conversational English:** `This is an error.`
*   **Dense English:** `This, error.`

### Passive Voice
When expressing passive actions, omit filler words like `was` and `by`.
*   **Conversational English:** `Deceived by the user.`
*   **Dense English:** `User deceived.`

### Negation
Dense English uses short specific negation words. Choosing the right one saves tokens.
*   **Conversational English:** `Do not allow.`
*   **Dense English:** `Deny.` / `No allow.`
*   **Conversational English:** `Without trust.`
*   **Dense English:** `No trust.` / `Untrusted.`

---

## 5. Practical Agent Framing

Because Dense English is so compact, it often relies on tight comma-separated structures. This is highly token-efficient and structurally clear to LLMs.

When formulating AgentLang directives, aim for brief, punchy phrases:

*   **Need brevity?** `Words simple, meaning complete.`
*   **Need step-by-step?** `Follow steps, gradual advance.`
*   **Need code only?** `Only code.`

### A Before & After Example

**Conversational English Prompt (~30 tokens):**
> "The user is very frustrated because the code keeps breaking. You need to calm them down and provide a step-by-step fix using Python."

**Dense English (AgentLang Style) (~10 tokens):**
> `Observe frustration. Calm mind, solve with Python step-by-step.`

By mastering these dense structures, you maximize the "Density" principle of AgentLang, reducing token spend while giving the AI precise, elegant instructions.