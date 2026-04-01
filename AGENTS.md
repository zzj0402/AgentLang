# Agent Instructions — 智文 AgentLang

## Project Overview

**智文 AgentLang** is a high-density, human-machine bilingual semantic protocol for AI Agents. It fuses the conciseness of classical Chinese (文言文) with an empathic reasoning engine (观→感→需→请), achieving 50–80% token reduction while maintaining full human readability, auditability, and emotional intelligence.

- **Repository**: `AgentLang`
- **License**: Apache 2.0

---

## Core Philosophy

Understand these before writing any code or content:

| Principle | Meaning | Implication for Agents |
|---|---|---|
| **Density** | Classical Chinese conveys in 4 characters what English requires a sentence for. | Minimize verbosity in protocol syntax, code comments, and documentation. Every token must earn its place. |
| **Readability** | Every instruction is auditable by a human developer. | Never sacrifice clarity for compression. No minification, no obfuscation. A security auditor must be able to read any `.zw` protocol file. |
| **Human-Agent Bilingual** | 智文 is a shared language — equally readable by Agents and humans. | Protocol syntax must be parseable by LLMs *and* understandable by developers. Design for both audiences simultaneously. |
| **Empathic Reasoning** | The empathic chain (观→感→需→请) is embedded at the protocol layer, not bolted on as an afterthought. | Agents must *understand before they answer*. The chain is the reasoning scaffold that ensures responses are grounded in observation, emotionally aware, need-oriented, and action-concrete. |
| **Dynamic, Not Static** | All states are transient. Describe behavior and context as they are *now*, never crystallize a momentary observation into a fixed identity or label. | Never assign static labels to users, situations, or states (e.g., "beginner", "confused"). Always describe observable, transient behavior (e.g., "the user has asked three times", "first interaction with this feature"). |

### Name Etymology

- **智** (*Zhì*) — 智能体 (Agent)
- **文** (*Wén*) — 文言文 (Classical Chinese)

Together: the language of Agents, rooted in classical Chinese conciseness.

---

## The Empathic Reasoning Chain (观→感→需→请)

The empathic chain is a communication framework built on four components:

1. **观 Observation** — Describe what is happening without evaluation or judgment.
2. **感 Feeling** — Acknowledge the emotions present, owned by the speaker.
3. **需 Need** — Identify the universal human need behind the feeling.
4. **请 Request** — Make a concrete, actionable, doable request.

### Why Empathic Reasoning is the Core of 智文

Most AI protocols optimize for *what the Agent should do*. 智文 optimizes for *how the Agent should reason before doing*. The chain (观→感→需→请) ensures:

- **Agents observe before judging.** `#观` forces the Agent to ground its understanding in facts, not assumptions.
- **Agents acknowledge emotional context.** `#感` makes the Agent emotionally literate — it registers the human state before responding.
- **Agents address root needs, not surface symptoms.** `#需` ensures the response targets what the human actually needs, not what they literally said.
- **Agents produce concrete actions, not vague platitudes.** `#请` constrains the response to something doable.

This is not sentiment analysis. This is structured empathic reasoning built into the protocol grammar itself.

### Anti-Patterns to Avoid

When writing protocols and in project communication, avoid these common failures:

| Anti-Pattern | Example | Correction |
|---|---|---|
| **Evaluation disguised as observation** | "The user is confused" | "The user asked the same question three times" (`#观`) |
| **Static label disguised as observation** | "This is a beginner" / "他是个急性子" | "The user has indicated this is their first project" / "他连续发送了三条消息" |
| **Thinking disguised as feeling** | "I feel that this is wrong" | "I feel uncertain when I read this logic" (`#感`) |
| **Strategy disguised as need** | "I need you to rewrite this" | "I need clarity about the expected behavior" (`#需`) |
| **Demand disguised as request** | "You must fix this" | "Would you be willing to add a docstring here?" (`#请`) |

---

## 智文 Protocol Syntax Reference

### File Extension

智文 protocol files use the `.zw` extension.

### Core Directives

Directives are prefixed with `#` followed by a Chinese keyword. Each directive serves a specific structural role:

```
#角色    Role definition — who the Agent is
#观      Observation — what is objectively happening, without judgment
#感      Feeling — emotional context to acknowledge, owned by the observer
#需      Need — underlying universal need to address
#请      Request — concrete, doable action to take
#约束    Constraints — boundaries and rules
#输出    Output — response structure/format
#上下文  Context — background information
#工具    Tools — available tools/functions
#记忆    Memory — state to persist across turns
```

### The Empathic Chain (观→感→需→请) — Deep Dive

The four directives `#观`, `#感`, `#需`, `#请` form the **empathic reasoning chain**. This is the protocol's empathic logic layer — the mechanism by which 智文 Agents reason with emotional intelligence. For the standard vocabulary of single-character feelings and needs, refer to the [Lexicon of Feelings & Needs](feeling_need_lexicon.md).

```
#观  Observation  — Describe what is happening without judgment or evaluation.
                    State only what a camera would record.
                    ✓ "用户连续三次询问同一问题"
                    ✗ "用户很困惑" (this is evaluation, not observation)

#感  Feeling      — Acknowledge the emotional state present.
                    Use feeling words, not thinking words.
                    ✓ "识其焦虑与挫败"
                    ✗ "觉得用户不理解" (this is a thought, not a feeling)

#需  Need         — Identify the underlying universal human need.
                    Needs are universal (clarity, safety, connection, autonomy).
                    ✓ "用户需：清晰理解，恢复信心"
                    ✗ "用户需要一个更好的文档" (this is a strategy, not a need)

#请  Request      — Formulate a concrete, actionable, doable request.
                    Requests are specific and time-bound.
                    ✓ "以三步示例回应；每步附代码"
                    ✗ "好好解释一下" (this is vague, not actionable)
```

**Ordering rule**: When the empathic chain is present, `#观` → `#感` → `#需` → `#请` must appear in this order. The parser validates this sequence. Partial chains (e.g., `#观` + `#请` without `#感` and `#需`) are permitted but the parser emits a warning — because skipping feelings and needs often produces shallow responses.

**Why order matters**: The chain models a cognitive progression:
1. First, ground yourself in reality (观 Observation).
2. Then, register the emotional landscape (感 Feeling).
3. Then, understand what is actually at stake (需 Need).
4. Only then, formulate a response (请 Request).

An Agent that skips to `#请` without `#观` is guessing. An Agent that skips `#感` is emotionally blind. The chain enforces *understanding before acting*.

### Complete Example (with annotations)

```
#角色 助手·技术文档

#上下文 用户正在使用智文协议编写首个Agent应用

# --- Empathic Chain begins ---
#观 用户询问协议语法，初次接触
    # Observation: factual, no judgment — "asking about syntax, first contact"

#感 识其好奇与些许困惑
    # Feeling: curiosity and slight confusion — owned by the observer

#需 用户需：快速理解核心语法，建立信心
    # Need: understanding and confidence — universal human needs

#请 以示例为主，逐步讲解；避免术语堆砌
    # Request: concrete strategy — use examples, step by step, avoid jargon
# --- Empathic Chain ends ---

#约束 {
  长度: ≤300字
  语言: zh-CN
  风格: 温和、鼓励
  # Empathic style: warm and encouraging, not authoritative
}

#工具 [代码高亮, 语法检查]

#输出 概念简述→核心语法→示例→练习建议
```

## Coding Standards

### Documentation

- Write documentation in **English** by default.
- Protocol examples and `.zw` files
- Keep prose concise. Apply the project's own density principle to docs.
- When explaining protocol features, always connect them back to the empathic reasoning foundation. Don't just describe *what* a directive does — explain *why* it exists in terms of the empathic chain.

### Commits

- Use [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- Short and precise commit messages.

---

## Communication Guidelines — Empathic Collaboration

All contributions — code reviews, issues, PRs, discussions — follow empathic communication principles. This is not a stylistic preference; it is a project requirement. The same empathic chain (观→感→需→请) that structures Agent reasoning also structures human collaboration.

### The Four Steps Applied to Collaboration

| Step | Directive | Pattern | ✓ Example | ✗ Anti-Pattern |
|---|---|---|---|---|
| **Observation** | `观` | Describe facts without judgment | *"This function returns None on line 42 when given an empty list"* | *"This code is broken"* |
| **Feeling** | `感` | Own your experience using feeling words | *"I feel confused by this control flow"* | *"This is confusing"* (evaluation, not feeling) |
| **Need** | `需` | Name the universal need behind the feeling | *"I need clarity on the expected return type"* | *"Fix this"* (demand, not need) |
| **Request** | `请` | Make concrete, doable, time-bound requests | *"Could we add a type annotation and a docstring here?"* | *"Needs documentation"* (vague, not actionable) |

### Why Empathic Code Review?

Traditional code review language is evaluative: "This is wrong," "Bad pattern," "Needs work." This language triggers defensiveness, which slows collaboration. Empathic code review separates *observation from evaluation*, making feedback easier to receive and act on.

**Example — empathic code review comment:**

> **观**: The `parse_directive()` function on line 87 does not handle the case where the input is an empty string.
> **感**: I feel uneasy about this because empty inputs are common in user-facing tools.
> **需**: I need confidence that edge cases are covered before merging.
> **请**: Would you be willing to add a test case for empty string input?

### Empathic Issue Reports

When filing issues, structure them using the empathic chain:

```
## 观 Observation
[Describe what happened factually — steps to reproduce, error messages, exact behavior]

## 感 Feeling
[Optional but encouraged — acknowledge the emotional impact: frustration, confusion, urgency]

## 需 Need
[Name the need: reliability, clarity, compatibility, etc.]

## 请 Request
[Concrete ask: fix, investigation, documentation, workaround, etc.]
```

---

## Key Design Decisions

1. **No minification** — The protocol is meant to be read. Never implement a "minify" mode that removes readability.
2. **Chinese directives are canonical** — `#角色` is the directive, not `#role`. English may appear in documentation but not in protocol syntax.
3. **Empathic chain is optional but strongly encouraged** — Protocols can omit `#观/#感/#需/#请`, but the parser validates them when present:
   - **Order**: `#观` → `#感` → `#需` → `#请` must appear in sequence.
   - **Completeness**: Partial chains (e.g., `#观` + `#请` without `#感/#需`) are valid but emit a warning. Skipping `#感` (feeling) or `#需` (need) often produces responses that are technically correct but emotionally tone-deaf.
   - **Anti-pattern detection**: The empathy validator should flag common anti-patterns (evaluation-as-observation, thought-as-feeling, strategy-as-need, demand-as-request) when possible.
4. **Security-first** — Any feature that would make protocol files harder for humans to audit is rejected by design.
5. **Empathic chain is structural, not decorative** — The empathic chain is not a "nice-to-have" comment block. It is a first-class data structure in the Protocol model, with its own type, its own validator, and its own test suite.
6. **Dynamic, not static** — All descriptions are transient observations, not fixed labels. The protocol describes *what is happening*, never *what something is*. Static labels ("beginner", "confused", "急性子") are anti-patterns; dynamic descriptions ("asked three times", "first interaction") are correct.

---

## Quick Reference for Agents

When contributing to this project, remember:

- **Think dense.** Every line of code, every line of docs — earn its place.
- **Think auditable.** If a human can't read it, it doesn't ship.
- **Think bilingual.** Protocol syntax is Chinese. Code and docs are English.
- **Think empathically.** The empathic chain (观→感→需→请) is not decoration — it is the reasoning engine that makes 智文 Agents different from prompt templates. Observe before judging. Feel before analyzing. Need before strategizing. Request before demanding.
- **Think dynamically.** Never freeze a moment into a label. Describe what is happening *now*, not what something *is*. States are transient — treat them that way.
- **Communicate empathically.** Use the empathic chain in code reviews, issues, and discussions. Separate observation from evaluation. Own your feelings. Name needs, not strategies. Make requests, not demands.
- **Test everything.** All tests must pass before any PR.
