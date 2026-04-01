# English to ZhiWen Translation Benchmark Report

This report details the token efficiency, latency, and semantic similarity of translating English prompts into dense Classical Chinese (ZhiWen) across 9 small local models.

Semantic similarity is calculated using Universal Sentence Encoder (USE) Multilingual (`tensorflow_hub`).

| Model                       |   Eng Toks |   ZW Toks | Reduction   |   Similarity | Latency   | Result Preview       |
|-----------------------------|------------|-----------|-------------|--------------|-----------|----------------------|
| Qwen2.5-0.5B-Instruct       |         27 |        38 | -40.74%     |       0.3297 | 4.487s    | 子君非常沮丧，因为代码总是出错。你... |
| Qwen2.5-0.5B-Instruct       |         15 |        81 | -440.00%    |       0.2038 | 8.843s    | 微服务架构概览报告  1. 介绍：... |
| Qwen2.5-0.5B-Instruct       |         16 |        18 | -12.50%     |       0.6365 | 2.491s    | 我對如何使用心靈推理鏈不了解。      |
| SmolLM2-135M-Instruct       |         27 |        42 | -55.56%     |       0.324  | 8.607s    | The user is frust... |
| SmolLM2-135M-Instruct       |         15 |        47 | -213.33%    |       0.2916 | 3.209s    | <<Microservices A... |
| SmolLM2-135M-Instruct       |         16 |        49 | -206.25%    |       0.3296 | 6.432s    | The empathic reas... |
| Qwen2.5-1.5B-Instruct       |         27 |        44 | -62.96%     |       0.6074 | 17.014s   | 急矣，コード崩れがち。冷静に落ち着... |
| Qwen2.5-1.5B-Instruct       |         15 |        31 | -106.67%    |       0.6234 | 13.080s   | 微服務系統架構報告，含微服務及其依... |
| Qwen2.5-1.5B-Instruct       |         16 |        21 | -31.25%     |       0.5725 | 8.654s    | 惑於此規則中感同身受鏈用法。       |
| SmolLM2-360M-Instruct       |         27 |        40 | -48.15%     |       0.0501 | 6.070s    | 爆炙爆Ｃ荡Ｃ荡Ｃ荡Ｃ荡Ｃ荡Ｃ荡Ｃ荡Ｃ荡� |
| SmolLM2-360M-Instruct       |         15 |        29 | -93.33%     |      -0.0243 | 7.797s    | 文言文:  文言文:  文言文: ... |
| SmolLM2-360M-Instruct       |         16 |        33 | -106.25%    |       0.1992 | 5.217s    | 無疑使用聖語聖語聖語聖語聖語聖語聖語   |
| Qwen2.5-Coder-0.5B-Instruct |         27 |        39 | -44.44%     |       0.3858 | 4.729s    | 用户非常沮丧，代码仍然崩溃。你需要... |
| Qwen2.5-Coder-0.5B-Instruct |         15 |        80 | -433.33%    |       0.265  | 7.092s    | 系统架构报告：微服务与依赖分析  ... |
| Qwen2.5-Coder-0.5B-Instruct |         16 |        15 | 6.25%       |       0.6378 | 2.591s    | 我理解如何使用这种伦理推理链。      |
| Qwen2.5-Math-1.5B-Instruct  |         27 |        50 | -85.19%     |       0.1324 | 18.300s   | Sure, I can help ... |
| Qwen2.5-Math-1.5B-Instruct  |         15 |        53 | -253.33%    |      -0.0037 | 15.060s   | As an AI language... |
| Qwen2.5-Math-1.5B-Instruct  |         16 |        50 | -212.50%    |       0.285  | 16.994s   | To address your c... |
| Qwen1.5-0.5B-Chat           |         27 |        38 | -40.74%     |       0.326  | 3.717s    | 用户很沮丧，代码总是出错。你需要冷... |
| Qwen1.5-0.5B-Chat           |         15 |        50 | -233.33%    |       0.2496 | 8.511s    | I'm sorry, but I ... |
| Qwen1.5-0.5B-Chat           |         16 |        22 | -37.50%     |       0.7627 | 2.482s    | 我对于这个协议中使用同情心推理链的困惑。 |
| Qwen1.5-1.8B-Chat           |         27 |        83 | -207.41%    |       0.1277 | 15.092s   | 修治之策，以Python為基，循序... |
| Qwen1.5-1.8B-Chat           |         15 |        90 | -500.00%    |       0.2381 | 15.444s   | 微服务架构报告  一、系统概述 本... |
| Qwen1.5-1.8B-Chat           |         16 |        22 | -37.50%     |       0.7813 | 7.538s    | 我困惑于如何在本协议中运用同情推理链。  |
