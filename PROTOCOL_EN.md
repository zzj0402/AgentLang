# AgentLang EN Protocol Specification

**Version**: 0.1.0

> A high-density, empathic, and human-machine bilingual semantic protocol for AI Agents.
> Dense English grammar fused with an empathic reasoning engine (Obs→Feel→Need→Req).

## Notation

The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** follow [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) semantics.

## File Extension

AgentLang protocol files MUST use the `.zw` extension.

## Language and Grammar

All content within a `.zw` file MUST be written in dense English using the principles of extreme omission and monosyllabism. All content SHOULD follow the defined grammar and the standard vocabulary if possible.

## Core Design Principles

| Principle | Implication |
|---|---|
| **Density** | Every token earns its place. Dense English conveys in a few words what conversational English requires a sentence for. |
| **Readability** | Every instruction is auditable by a human. No minification, no obfuscation. |
| **Human-Agent Bilingual** | Protocol syntax is parseable by LLMs *and* understandable by developers. |
| **Empathic Reasoning** | The chain (Obs→Feel→Need→Req) is embedded at the protocol layer. Agents observe before judging, feel before analyzing, need before strategizing, request before demanding. |
| **Dynamic, Not Static** | All states are transient. Describe behavior and context as they are *now*, never crystallize a momentary observation into a fixed identity or label. |

---

## Syntax

### Directives

Directives are prefixed with `#` immediately followed by an English keyword (no space between `#` and the keyword). English directives are **canonical**.

| Directive | Role | Required |
|---|---|---|
| `#Role` | Role definition — who the Agent is | SHOULD |
| `#Ctx` | Context — Background information | MAY |
| `#Obs` | Observation — what is objectively happening, without judgment | MAY* |
| `#Feel` | Feeling — emotional context, owned by the observer | MAY* |
| `#Need` | Need — underlying universal need to address | MAY* |
| `#Req` | Request — concrete, doable action to take | MAY* |
| `#Rules` | Constraints — boundaries and rules | MAY |
| `#Tools` | Tools — available tools/functions | MAY |
| `#Out` | Output — response structure/format | MAY |
| `#Mem` | Memory — state to persist across turns | MAY |

\* See [The Empathic Chain](#the-empathic-chain) for ordering and completeness rules.

### Comments

Lines where `#` is followed by a **space and non-keyword text** are comments. A parser MUST distinguish comments from directives by checking whether the text after `#` matches a known directive keyword.

```zw
# This is a comment — no known keyword follows #
#Obs This is an observation directive
# --- section divider --- (also a comment)
```

### Multi-line Content

A directive's content extends from the directive keyword to the next directive (`#keyword`) or end of file. Indented continuation lines belong to the preceding directive.

```zw
#Obs User asked same question thrice
    Phrased differently each time
    # ^ This indented line is part of #Obs's content
```

### Directive Ordering

Outside the empathic chain, directive ordering is **free-form** — `#Role` MAY appear before or after `#Ctx`, etc. However, the conventional ordering is:

```
#Role → #Ctx → [empathic chain] → #Rules → #Tools → #Out → #Mem
```

Directives MUST NOT repeat within a single protocol file. A parser MUST emit an error on duplicate directives.

---

## The Empathic Chain

The four directives `#Obs`, `#Feel`, `#Need`, `#Req` form the **empathic reasoning chain** — the mechanism by which AgentLang Agents reason with emotional intelligence. This chain models a cognitive progression:

1. Ground yourself in reality (Obs Observation).
2. Register the emotional landscape (Feel Feeling).
3. Understand what is actually at stake (Need Need).
4. Only then, formulate a response (Req Request).

An Agent that skips to `#Req` without `#Obs` is guessing. An Agent that skips `#Feel` is emotionally blind.

### Directive Definitions with ✓/✗ Examples

**`#Obs` Observation** — Describe what is happening without judgment or evaluation. State only what a camera would record.

| | Example |
|---|---|
| ✓ | `User asked same question thrice` |
| ✗ | `User is confused` ← evaluation, not observation |

**`#Feel` Feeling** — Acknowledge the emotional state present. Use feeling words, not thinking words. Feelings are owned by the observer.

| | Example |
|---|---|
| ✓ | `Sense anxiety and frustration` |
| ✗ | `Feel user does not understand` ← thought, not feeling |

**`#Need` Need** — Identify the underlying universal human need. Needs are universal: clarity, safety, connection, autonomy, etc.

| | Example |
|---|---|
| ✓ | `Need: clarity, regain confidence` |
| ✗ | `Need better documentation` ← strategy, not need |

**`#Req` Request** — Formulate a concrete, actionable, doable request. Requests are specific and time-bound.

| | Example |
|---|---|
| ✓ | `Reply with 3-step example; code in each step` |
| ✗ | `Explain it well` ← vague, not actionable |

### Anti-Patterns

| Anti-Pattern | Trap | Example | Correction |
|---|---|---|---|
| Evaluation as observation | `#Obs` contains judgment | "The user is confused" | "The user asked the same question three times" |
| Static label | Any directive assigns a fixed identity | "This is a beginner" | "The user has indicated this is their first project" |
| Thought as feeling | `#Feel` uses thinking words | "I feel that this is wrong" | "I feel uncertain when I read this logic" |
| Strategy as need | `#Need` prescribes a solution | "I need you to rewrite this" | "I need clarity about the expected behavior" |
| Demand as request | `#Req` makes a demand | "You must fix this" | "Would you be willing to add a docstring here?" |

---

## Data Structures within Directives

### `#Rules` Constraints

Uses **YAML-like key-value syntax** for readability. Keys are bare (unquoted), values MAY be quoted or bare.

```zw
#Rules {
  length: <=300 words
  lang: en
  tone: warm, encouraging
}
```

### `#Tools` Tools

A comma-separated list inside `[]`.

```zw
#Tools [code_highlight, syntax_check, file_search]
```

For tools with descriptions, use key-value pairs:

```zw
#Tools {
  code_highlight: Apply syntax coloring to code blocks
  syntax_check: Validate .zw file protocol compliance
}
```

### `#Out` Output

A flow description using `->` to denote sequence.

```zw
#Out Concept brief -> Core syntax -> Examples -> Practice suggestions
```

### `#Mem` Memory

Uses the same YAML-like key-value syntax as `#Rules`.

```zw
#Mem {
  user_level: beginner
  discussed_topics: [protocol syntax, directives format]
  session_turns: 3
}
```

---

## Parser Validation Rules

### Empathic Chain Ordering

When any empathic chain directive is present, a parser MUST validate:

| Rule | Severity | Condition |
|---|---|---|
| **Sequence** | ERROR | If present, `#Obs` → `#Feel` → `#Need` → `#Req` MUST appear in this order. Out-of-order is invalid. |
| **Partial chain** | WARNING | A partial chain (e.g., `#Obs` + `#Req` without `#Feel` / `#Need`) is valid but SHOULD emit a warning. Skipping `#Feel` or `#Need` often produces responses that are technically correct but emotionally tone-deaf. |
| **Standalone `#Req`** | WARNING | `#Req` without any preceding chain directive SHOULD emit a warning — the Agent is acting without grounding. |

### Duplicate Directives

A parser MUST emit an **ERROR** if any directive appears more than once in a single `.zw` file.

### Anti-Pattern Detection

A parser SHOULD attempt to flag common anti-patterns when possible:

- **Evaluation in `#Obs`**: Text containing judgment words (e.g., "confused", "wrong", "bad") without factual anchoring.
- **Static labels**: Text in any directive that assigns a fixed identity or trait (e.g., "is a beginner") rather than describing observable, transient behavior. All states are momentary — the protocol describes *what is happening*, never *what something is*.
- **Thinking in `#Feel`**: Phrases like "I feel that..." (thought, not feeling).
- **Strategy in `#Need`**: Text that prescribes a specific action rather than naming a universal need.
- **Demand in `#Req`**: Imperative language without optionality (e.g., "You must...").

Anti-pattern detection is best-effort. Parsers MAY implement this as a linter rather than a hard validation step.

---

## Complete Example

```zw
#Role TechDoc Assistant

#Ctx User writing first Agent app using AgentLang protocol

# --- Empathic Chain ---
#Obs User asking about protocol syntax, first contact

#Feel Sense curiosity and slight confusion

#Need Need: fast understanding of core syntax, build confidence

#Req Rely primarily on examples, step-by-step; avoid jargon

#Rules {
  length: <=300 words
  lang: en
  tone: warm, encouraging
}

#Tools [code_highlight, syntax_check]

#Out Concept brief -> Core syntax -> Examples -> Practice suggestions
```

---

## Design Decisions

1. **No minification** — The protocol is meant to be read. Never implement a "minify" mode that removes readability.
2. **English directives are canonical** — `#Role` is the directive, not `#角色`.
3. **Empathic chain is optional but strongly encouraged** — Protocols can omit `#Obs/#Feel/#Need/#Req`, but presence triggers validation.
4. **Security-first** — Any feature that would make protocol files harder for humans to audit is rejected by design.
5. **Empathic chain is structural, not decorative** — It is a first-class data structure with its own type, validator, and test suite — not a comment block.

---

*See [CHANGELOG.md](CHANGELOG.md) for version history.*
