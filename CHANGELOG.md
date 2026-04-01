# Changelog

All notable changes to the 智文 AgentLang Protocol are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added

- `GRAMMAR_EN.md` - A comprehensive Classical Chinese grammar guide tailored for English-speaking developers to write highly token-efficient ZhiWen prompts (including sections on extreme omission, monosyllabism, causative/passive voice, judgment sentences, and negation).

## [0.1.0] — 2026-03-31

### Added

- Initial protocol specification
- Core directives: `#角色`, `#观`, `#感`, `#需`, `#请`, `#约束`, `#输出`, `#上下文`, `#工具`, `#记忆`
- Empathic chain (观→感→需→请) ordering and validation rules
- Anti-pattern definitions for each empathic directive
- Parser validation rules (ERROR/WARNING severity)
- Data structure format specifications for `#约束`, `#工具`, `#输出`, `#记忆`
- Comment and multi-line content syntax rules
- Complete annotated `.zw` example
- Design decisions section
