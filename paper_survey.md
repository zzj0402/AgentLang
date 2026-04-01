# Survey: Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search

**Paper:** [arXiv:2602.22983](https://arxiv.org/abs/2602.22983)
**Authors:** Xun Huang, Simeng Qin, Xiaoshuang Jia, Ranjie Duan, Huanqian Yan, Zhitao Zeng, Fei Yang, Yang Liu, Xiaojun Jia
**Topics:** Large Language Models (LLMs), AI Security, Jailbreak Attacks, Classical Chinese, Bio-Inspired Optimization

## Overview

This paper introduces a novel perspective on LLM vulnerabilities by exploring the security risks associated with **Classical Chinese**. Due to its semantic succinctness, rich metaphors, inherent ambiguity, and asymmetry in semantic correspondence with modern Chinese, Classical Chinese represents a unique "safety blind spot" in modern AI models. While models are often capable of comprehending the obscure inputs, existing safety guardrails (which are predominantly optimized for modern languages like English) frequently fail to detect and block harmful intent concealed within this ancient context.

To exploit this vulnerability systematically, the authors propose **CC-BOS** (Classical Chinese - Bio-Inspired Search), an automated black-box jailbreak framework.

## Core Contributions

1. **Discovery of the Classical Chinese Vulnerability:**
   The authors establish that the concise and obscure nature of Classical Chinese naturally bypasses modern safety alignments. Unlike low-resource languages that lack training data, Classical Chinese has abundant historical corpora but fundamentally distinct linguistic properties that current safeguards struggle to parse for harmful intent.

2. **The CC-BOS Framework:**
   - **8-Dimensional Strategy Space:** Jailbreak prompts are formalized into eight policy dimensions: role identity, behavior guidance, mechanism, metaphor mapping, expression style, knowledge relation, trigger pattern, and context setting.
   - **Bio-Inspired Optimization:** CC-BOS leverages a fruit-fly optimization algorithm utilizing smell search, visual search, and Cauchy mutation. This enables iterative and efficient exploration of the Classical Chinese strategy space for prompt refinement.

3. **Two-Stage Translation Module:**
   To overcome the difficulty of evaluating highly compressed and metaphorical Classical Chinese outputs across cross-lingual scenarios, the researchers developed a translation module that progressively unpacks metaphors and semantic compression into English for reliable safety evaluation.

4. **Experimental Validation:**
   The proposed framework was tested against six mainstream LLMs in black-box settings, achieving a nearly 100% attack success rate, consistently outperforming state-of-the-art methods in modern languages.
