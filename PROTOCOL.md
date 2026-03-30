# 智文 AgentLang Protocol Specification

## Overview

This document defines the specification for the 智文 (ZhiWen) AgentLang protocol.
The protocol is a high-density, human-machine bilingual semantic protocol for AI Agents, fusing classical Chinese conciseness with an empathic reasoning engine.

## File Extension

The standard file extension for 智文 AgentLang files is `.zw`.

## Core Design Principles

1. **Density**: Classical Chinese conveys in 4 characters what English requires a sentence for. Minimize verbosity in protocol syntax, code comments, and documentation.
2. **Readability**: Every interaction is auditable by a human developer. No minification or obfuscation is permitted.
3. **Human-Agent Bilingual**: 智文 is a shared language. Protocol syntax must be parseable by LLMs and understandable by developers.
4. **Empathic Reasoning**: The empathic chain (观→感→需→请) is embedded at the protocol layer. Agents must observe before judging, feel before analyzing, need before strategizing, and request before demanding.

## Core Directives

Directives are prefixed with `#` followed by a Chinese keyword. Chinese directives are canonical.

*   `#角色` (Role): Role definition — who the Agent is.
*   `#观` (Observation): Describe what is objectively happening without judgment or evaluation. State only what a camera would record.
*   `#感` (Feeling): Acknowledge the emotional state present. Use feeling words, not thinking words.
*   `#需` (Need): Identify the underlying universal human need (clarity, safety, connection, autonomy).
*   `#请` (Request): Formulate a concrete, actionable, doable request. Requests are specific and time-bound.
*   `#约束` (Constraints): Boundaries and rules.
*   `#输出` (Output): Response structure/format.
*   `#上下文` (Context): Background information.
*   `#工具` (Tools): Available tools/functions.
*   `#记忆` (Memory): State to persist across turns.

## The Empathic Chain

The empathic chain consists of `#观`, `#感`, `#需`, `#请`.
When present, they **must** appear in this sequence: `#观` → `#感` → `#需` → `#请`.
Partial chains are valid but skipping `#感` or `#需` often produces responses that are technically correct but emotionally tone-deaf.

## Data Structures within Directives

When defining data structures within 智文 (`.zw`) files, such as inside `#记忆` or `#约束` blocks, **Python-style syntax must be used instead of JSON**.
This includes:
*   Python dictionaries (`{}`)
*   Python lists (`[]`)
*   Variable assignments
*   Triple quotes for multi-line strings (`"""` or `'''`)

Example:

```zw
#约束 {
  '长度': '<=300字',
  '语言': 'zh-CN',
  '风格': '温和、鼓励'
}
```
