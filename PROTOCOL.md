# 智文 AgentLang Protocol Specification

**Version**: 0.1.0

> A high-density, empathic, and human-machine bilingual semantic protocol for AI Agents.
> Classical Chinese conciseness fused with an empathic reasoning engine (观→感→需→请).

## Notation

The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** follow [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) semantics.

## File Extension

智文 protocol files MUST use the `.zw` extension.

## Core Design Principles

| Principle | Implication |
|---|---|
| **Density** | Every token earns its place. Classical Chinese conveys in 4 characters what English requires a sentence for. |
| **Readability** | Every instruction is auditable by a human. No minification, no obfuscation. |
| **Human-Agent Bilingual** | Protocol syntax is parseable by LLMs *and* understandable by developers. |
| **Empathic Reasoning** | The chain (观→感→需→请) is embedded at the protocol layer. Agents observe before judging, feel before analyzing, need before strategizing, request before demanding. |
| **Dynamic, Not Static** | All states are transient. Describe behavior and context as they are *now*, never crystallize a momentary observation into a fixed identity or label. |

---

## Syntax

### Directives

Directives are prefixed with `#` immediately followed by a Chinese keyword (no space between `#` and the keyword). Chinese directives are **canonical** — `#角色` is the directive, not `#role`.

| Directive | Role | Required |
|---|---|---|
| `#角色` | Role definition — who the Agent is | SHOULD |
| `#上下文` | Background information | MAY |
| `#观` | Observation — what is objectively happening, without judgment | MAY* |
| `#感` | Feeling — emotional context, owned by the observer | MAY* |
| `#需` | Need — underlying universal need to address | MAY* |
| `#请` | Request — concrete, doable action to take | MAY* |
| `#约束` | Constraints — boundaries and rules | MAY |
| `#工具` | Tools — available tools/functions | MAY |
| `#输出` | Output — response structure/format | MAY |
| `#记忆` | Memory — state to persist across turns | MAY |

\* See [The Empathic Chain](#the-empathic-chain) for ordering and completeness rules.

### Comments

Lines where `#` is followed by a **space and non-keyword text** are comments. A parser MUST distinguish comments from directives by checking whether the text after `#` matches a known directive keyword.

```zw
# This is a comment — no known keyword follows #
#观 This is an observation directive
# --- section divider --- (also a comment)
```

### Multi-line Content

A directive's content extends from the directive keyword to the next directive (`#keyword`) or end of file. Indented continuation lines belong to the preceding directive.

```zw
#观 用户连续三次询问同一问题
    且每次措辞不同
    # ^ This indented line is part of #观's content
```

### Directive Ordering

Outside the empathic chain, directive ordering is **free-form** — `#角色` MAY appear before or after `#上下文`, etc. However, the conventional ordering is:

```
#角色 → #上下文 → [empathic chain] → #约束 → #工具 → #输出 → #记忆
```

Directives MUST NOT repeat within a single protocol file. A parser MUST emit an error on duplicate directives.

---

## The Empathic Chain

The four directives `#观`, `#感`, `#需`, `#请` form the **empathic reasoning chain** — the mechanism by which 智文 Agents reason with emotional intelligence. This chain models a cognitive progression:

1. Ground yourself in reality (观 Observation).
2. Register the emotional landscape (感 Feeling).
3. Understand what is actually at stake (需 Need).
4. Only then, formulate a response (请 Request).

An Agent that skips to `#请` without `#观` is guessing. An Agent that skips `#感` is emotionally blind.

### Directive Definitions with ✓/✗ Examples

**`#观` Observation** — Describe what is happening without judgment or evaluation. State only what a camera would record.

| | Example |
|---|---|
| ✓ | `用户连续三次询问同一问题` |
| ✗ | `用户很困惑` ← evaluation, not observation |

**`#感` Feeling** — Acknowledge the emotional state present. Use feeling words, not thinking words. Feelings are owned by the observer.

| | Example |
|---|---|
| ✓ | `识其焦虑与挫败` |
| ✗ | `觉得用户不理解` ← thought, not feeling |

**`#需` Need** — Identify the underlying universal human need. Needs are universal: clarity, safety, connection, autonomy, etc.

| | Example |
|---|---|
| ✓ | `用户需：清晰理解，恢复信心` |
| ✗ | `用户需要一个更好的文档` ← strategy, not need |

**`#请` Request** — Formulate a concrete, actionable, doable request. Requests are specific and time-bound.

| | Example |
|---|---|
| ✓ | `以三步示例回应；每步附代码` |
| ✗ | `好好解释一下` ← vague, not actionable |

### Anti-Patterns

| Anti-Pattern | Trap | Example | Correction |
|---|---|---|---|
| Evaluation as observation | `#观` contains judgment | "The user is confused" | "The user asked the same question three times" |
| Static label | Any directive assigns a fixed identity | "This is a beginner" / "他是个急性子" | "The user has indicated this is their first project" / "他连续发送了三条消息" |
| Thought as feeling | `#感` uses thinking words | "I feel that this is wrong" | "I feel uncertain when I read this logic" |
| Strategy as need | `#需` prescribes a solution | "I need you to rewrite this" | "I need clarity about the expected behavior" |
| Demand as request | `#请` makes a demand | "You must fix this" | "Would you be willing to add a docstring here?" |

---

## Data Structures within Directives

### `#约束` Constraints

Uses **YAML-like key-value syntax** for readability. Keys are bare (unquoted), values MAY be quoted or bare.

```zw
#约束 {
  长度: ≤300字
  语言: zh-CN
  风格: 温和、鼓励
}
```

### `#工具` Tools

A comma-separated list inside `[]`.

```zw
#工具 [代码高亮, 语法检查, 文件搜索]
```

For tools with descriptions, use key-value pairs:

```zw
#工具 {
  代码高亮: 对代码块应用语法着色
  语法检查: 验证.zw文件的协议合规性
}
```

### `#输出` Output

A flow description using `→` to denote sequence.

```zw
#输出 概念简述→核心语法→示例→练习建议
```

### `#记忆` Memory

Uses the same YAML-like key-value syntax as `#约束`.

```zw
#记忆 {
  用户级别: 初学者
  已讨论主题: [协议语法, 指令格式]
  会话轮次: 3
}
```

---

## Parser Validation Rules

### Empathic Chain Ordering

When any empathic chain directive is present, a parser MUST validate:

| Rule | Severity | Condition |
|---|---|---|
| **Sequence** | ERROR | If present, `#观` → `#感` → `#需` → `#请` MUST appear in this order. Out-of-order is invalid. |
| **Partial chain** | WARNING | A partial chain (e.g., `#观` + `#请` without `#感` / `#需`) is valid but SHOULD emit a warning. Skipping `#感` or `#需` often produces responses that are technically correct but emotionally tone-deaf. |
| **Standalone `#请`** | WARNING | `#请` without any preceding chain directive SHOULD emit a warning — the Agent is acting without grounding. |

### Duplicate Directives

A parser MUST emit an **ERROR** if any directive appears more than once in a single `.zw` file.

### Anti-Pattern Detection

A parser SHOULD attempt to flag common anti-patterns when possible:

- **Evaluation in `#观`**: Text containing judgment words (e.g., "confused", "wrong", "bad") without factual anchoring.
- **Static labels**: Text in any directive that assigns a fixed identity or trait (e.g., "is a beginner", "是个急性子") rather than describing observable, transient behavior. All states are momentary — the protocol describes *what is happening*, never *what something is*.
- **Thinking in `#感`**: Phrases like "I feel that..." (thought, not feeling).
- **Strategy in `#需`**: Text that prescribes a specific action rather than naming a universal need.
- **Demand in `#请`**: Imperative language without optionality (e.g., "You must...").

Anti-pattern detection is best-effort. Parsers MAY implement this as a linter rather than a hard validation step.

---

## Complete Example

```zw
#角色 助手·技术文档

#上下文 用户正在使用智文协议编写首个Agent应用

# --- Empathic Chain ---
#观 用户询问协议语法，初次接触
    # Observation: factual, no judgment — "asking about syntax, first contact"

#感 识其好奇与些许困惑
    # Feeling: curiosity and slight confusion — owned by the observer

#需 用户需：快速理解核心语法，建立信心
    # Need: understanding and confidence — universal human needs

#请 以示例为主，逐步讲解；避免术语堆砌
    # Request: use examples, step by step, avoid jargon

#约束 {
  长度: ≤300字
  语言: zh-CN
  风格: 温和、鼓励
}

#工具 [代码高亮, 语法检查]

#输出 概念简述→核心语法→示例→练习建议
```

---

## Design Decisions

1. **No minification** — The protocol is meant to be read. Never implement a "minify" mode that removes readability.
2. **Chinese directives are canonical** — `#角色` is the directive, not `#role`. English appears in documentation, not in protocol syntax.
3. **Empathic chain is optional but strongly encouraged** — Protocols can omit `#观/#感/#需/#请`, but presence triggers validation.
4. **Security-first** — Any feature that would make protocol files harder for humans to audit is rejected by design.
5. **Empathic chain is structural, not decorative** — It is a first-class data structure with its own type, validator, and test suite — not a comment block.

---

*See [CHANGELOG.md](CHANGELOG.md) for version history.*
