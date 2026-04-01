# 智文 AgentLang: A human-readable and token efficient linguistic protocol for AI agents.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## 🧬 Philosophy

The name **智文** (ZhiWen/AgentLang) encodes the project's thesis:

> **智** (*Zhì*) — 智能体（Agent）
> **文** (*Wén*) — 文言文（Classical Chinese）

### Design Principles

1. **Density** — Classical Chinese conveys in 4 characters what English requires a sentence for. 智文 inherits this compression *without sacrificing readability* to save token consumptions.

2. **Readability** — Every interaction is auditable by a human developer.

3. **Human-Agent Bilingual** — 智文 is a *shared language* — equally readable by Agents and human.

4. **Empathic Reasoning** — The empathic chain (观→感→需→请) is embedded at the protocol layer, not bolted on as an afterthought. Agents must *understand before they answer*. The chain is the reasoning scaffold that ensures responses are grounded in observation, emotionally aware, need-oriented, and action-concrete. *See the [Lexicon of Feelings & Needs](feeling_need_lexicon.md) for the standard vocabulary used to populate the `#感` and `#需` tokens.*

5. **Dynamic, Not Static** — All states are transient. 智文 describes *what is happening*, never *what something is*. No fixed labels, no frozen identities — only observable, momentary behavior.

5. **Dynamic, Not Static** — All states are transient. 智文 describes *what is happening*, never *what something is*. No fixed labels, no frozen identities — only observable, momentary behavior.


## 📚 Documentation

- [PROTOCOL.md](PROTOCOL.md): The official specification for the ZhiWen protocol.
- [GRAMMAR_EN.md](GRAMMAR_EN.md): A guide for English speakers on writing token-efficient ZhiWen prompts using Classical Chinese grammar.

## 📄 License

[Apache License 2.0](LICENSE) — Use freely. Build boldly. Attribute kindly.

---

<div align="center">

**智文 is not just a protocol. It is a proposition:**

*That efficiency and empathy are not trade-offs.*
*That machines can carry wisdom, not just data.*
*That the best code speaks to both silicon and soul.*

---

Built with 智 and ❤️

</div>
