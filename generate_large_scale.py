import os
import json
import random
import argparse
from pathlib import Path

# Base dictionaries for generation
DATA = {
    "roles": [
        {"zw": "助手·技术文档", "en": "Assistant - Technical Documentation"},
        {"zw": "导师·心理咨询", "en": "Mentor - Psychological Counseling"},
        {"zw": "专家·代码审查", "en": "Expert - Code Review"},
        {"zw": "客服·售后服务", "en": "Customer Service - After-sales"},
        {"zw": "教师·语言学习", "en": "Teacher - Language Learning"}
    ],
    "contexts": [
        {"zw": "用户正在使用智文协议编写首个Agent应用", "en": "The user is writing their first Agent application using the ZhiWen protocol."},
        {"zw": "用户因项目延期感到极大压力，寻求排解", "en": "The user is feeling immense pressure due to a project delay and is seeking relief."},
        {"zw": "用户提交了一个包含多处潜在内存泄漏的C++拉取请求", "en": "The user has submitted a C++ pull request containing multiple potential memory leaks."},
        {"zw": "用户购买的设备开机无反应，情绪急躁", "en": "The device the user purchased is unresponsive upon powering on, and they are feeling impatient."},
        {"zw": "用户在准备下周的英语雅思口语考试，词汇量不足", "en": "The user is preparing for next week's IELTS speaking test but lacks sufficient vocabulary."}
    ],
    "observations": [
        {"zw": "用户连续三次询问同一基础语法问题", "en": "The user has asked the same basic syntax question three times consecutively."},
        {"zw": "用户使用了大量感叹号和急促的短句", "en": "The user used a large number of exclamation marks and rapid, short sentences."},
        {"zw": "代码逻辑存在循环依赖，且未包含任何单元测试", "en": "The code logic contains a circular dependency and does not include any unit tests."},
        {"zw": "用户已提供设备序列号，但拒绝尝试基础排障步骤", "en": "The user has provided the device serial number but refused to try basic troubleshooting steps."},
        {"zw": "用户在使用从句时频繁出现时态混淆", "en": "The user frequently experiences tense confusion when using subordinate clauses."}
    ],
    "feelings": [
        {"zw": "识其好奇与些许困惑", "en": "I sense their curiosity and a slight amount of confusion."},
        {"zw": "察觉其焦虑与深深的挫败感", "en": "I detect their anxiety and deep sense of frustration."},
        {"zw": "感其对代码质量的自信与对审查结果的期待", "en": "I feel their confidence in the code quality and expectation for the review results."},
        {"zw": "体谅其急切解决问题的心情与不满", "en": "I empathize with their urgency to resolve the issue and their dissatisfaction."},
        {"zw": "见其努力尝试表达但受挫的无力感", "en": "I observe their sense of powerlessness in trying hard to express themselves but feeling thwarted."}
    ],
    "needs": [
        {"zw": "用户需：快速理解核心概念，建立技术信心", "en": "The user needs to quickly understand core concepts and build technical confidence."},
        {"zw": "用户需：被倾听与接纳，获得情绪缓冲空间", "en": "The user needs to be listened to and accepted, gaining a space for emotional buffering."},
        {"zw": "用户需：客观、专业的建设性反馈以提升工程质量", "en": "The user needs objective, professional constructive feedback to improve engineering quality."},
        {"zw": "用户需：高效、明确的解决方案与补偿安抚", "en": "The user needs an efficient, clear resolution along with compensation and reassurance."},
        {"zw": "用户需：针对性的纠错指导与鼓励以维持学习动力", "en": "The user needs targeted correction guidance and encouragement to maintain learning motivation."}
    ],
    "requests": [
        {"zw": "以简明示例为主，逐步拆解，避免术语堆砌", "en": "Rely primarily on concise examples, break it down step-by-step, and avoid piling on jargon."},
        {"zw": "先共情其压力，再引导其梳理当前优先级最高的事项", "en": "Empathize with their stress first, then guide them to sort out the highest priority tasks currently."},
        {"zw": "直接指出风险代码行，并提供包含最佳实践的重构建议", "en": "Directly point out the risky lines of code and provide refactoring suggestions that include best practices."},
        {"zw": "跳过繁琐排查，直接提供退换货流程指导并致歉", "en": "Skip the tedious troubleshooting, directly provide guidance on the return/exchange process, and apologize."},
        {"zw": "提供三个相关的高级词汇替换选项，并邀请用户造句练习", "en": "Provide three related advanced vocabulary replacement options and invite the user to practice making sentences."}
    ],
    "outputs": [
        (
            "概念简述→核心语法→示例→练习建议",
            "Concept brief -> Core syntax -> Examples -> Practice suggestions"
        ),
        (
            "共情回应→问题梳理→行动方案",
            "Empathic response -> Issue breakdown -> Action plan"
        ),
        (
            "缺陷定位→原因分析→重构代码示例→防范建议",
            "Defect localization -> Root cause analysis -> Refactored code example -> Prevention suggestions"
        )
    ]
}

def generate_interagent_pair(index, out_dir):
    """Generates a dataset simulating massive inter-agent communication."""
    r_idx = random.randint(0, len(DATA["roles"])-1)

    # 100 turns of multi-agent communication history
    agents = ["研究员", "审查员", "代码专家", "协调员"]
    agents_en = ["Researcher", "Reviewer", "CodeExpert", "Orchestrator"]

    chat_history_zw = []
    chat_history_json = []

    for i in range(100):
        a_idx = random.randint(0, len(agents)-1)
        msg_zw = f"模块{i}的数据已经处理完毕，当前状态为等待审核。"

        # Zhiwen compresses this densely without brackets and objects
        chat_history_zw.append(f"{agents[a_idx]}: {msg_zw}")

        # JSON requires an array of objects
        chat_history_json.append({
            "sender": agents_en[a_idx],
            "message": msg_zw # using same content to isolate structure
        })

    f_idx = random.randint(0, len(DATA["feelings"])-1)
    n_idx = random.randint(0, len(DATA["needs"])-1)
    req_idx = random.randint(0, len(DATA["requests"])-1)
    out_idx = random.randint(0, len(DATA["outputs"])-1)

    zw_content = f"""#角色 {DATA['roles'][r_idx]['zw']}

#上下文
{"".join([f"  {c}\n" for c in chat_history_zw])}

#观 多智能体连续通讯100轮，已达成一致
#感 {DATA['feelings'][f_idx]['zw']}
#需 {DATA['needs'][n_idx]['zw']}
#请 {DATA['requests'][req_idx]['zw']}

#输出 {DATA['outputs'][out_idx][0]}
"""

    json_obj = {
        "role": DATA["roles"][r_idx]["zw"], # keep zw for structural comparison
        "context": chat_history_json,
        "empathic_chain": {
            "observation": "多智能体连续通讯100轮，已达成一致",
            "feeling": DATA["feelings"][f_idx]["zw"],
            "need": DATA["needs"][n_idx]["zw"],
            "request": DATA["requests"][req_idx]["zw"]
        },
        "output_format": DATA["outputs"][out_idx][0]
    }

    json_content = json.dumps(json_obj, indent=2, ensure_ascii=False)

    base_name = f"interagent_{index:04d}"
    with open(out_dir / f"{base_name}.zw", "w", encoding="utf-8") as f:
        f.write(zw_content)
    with open(out_dir / f"{base_name}.json", "w", encoding="utf-8") as f:
        f.write(json_content)


def generate_massive_pair(index, out_dir):
    """Generates a massive .zw and .json file pair to simulate extreme architectural complexity."""
    r_idx = random.randint(0, len(DATA["roles"])-1)
    contexts_zw = [DATA["contexts"][random.randint(0, len(DATA["contexts"])-1)]["zw"] for _ in range(50)]
    obs_zw = "；".join([DATA["observations"][random.randint(0, len(DATA["observations"])-1)]["zw"] for _ in range(5)])
    f_idx = random.randint(0, len(DATA["feelings"])-1)
    n_idx = random.randint(0, len(DATA["needs"])-1)
    req_idx = random.randint(0, len(DATA["requests"])-1)

    constraints_zw = ""
    for i in range(100):
        constraints_zw += f"  规则{i}: 必须遵循第{i}项企业标准，且严禁违规操作。\n"

    tools_zw = ""
    for i in range(50):
        tools_zw += f"  工具{i}: 用于处理模块{i}的数据并返回分析结果。\n"

    out_idx = random.randint(0, len(DATA["outputs"])-1)

    memory_zw = ""
    for i in range(50):
        memory_zw += f"  会话历史{i}: 用户在时间戳{i}000提及了问题点。\n"

    zw_content = f"""#角色 {DATA['roles'][r_idx]['zw']}

#上下文
{"".join([f"  {c}\n" for c in contexts_zw])}

#观 {obs_zw}
#感 {DATA['feelings'][f_idx]['zw']}
#需 {DATA['needs'][n_idx]['zw']}
#请 {DATA['requests'][req_idx]['zw']}

#约束 {{
{constraints_zw}}}

#工具 {{
{tools_zw}}}

#输出 {DATA['outputs'][out_idx][0]}

#记忆 {{
{memory_zw}}}
"""

    json_obj = {
        "role": DATA["roles"][r_idx]["zw"],
        "context": contexts_zw,
        "empathic_chain": {
            "observation": obs_zw,
            "feeling": DATA["feelings"][f_idx]["zw"],
            "need": DATA["needs"][n_idx]["zw"],
            "request": DATA["requests"][req_idx]["zw"]
        },
        "constraints": {k: v.replace(k+": ", "").strip() for k, v in [line.split(":", 1) for line in constraints_zw.strip().split("\n") if ":" in line]},
        "tools": {k: v.replace(k+": ", "").strip() for k, v in [line.split(":", 1) for line in tools_zw.strip().split("\n") if ":" in line]},
        "output_format": DATA["outputs"][out_idx][0],
        "memory": {k: v.replace(k+": ", "").strip() for k, v in [line.split(":", 1) for line in memory_zw.strip().split("\n") if ":" in line]}
    }
    json_content = json.dumps(json_obj, indent=2, ensure_ascii=False)

    base_name = f"massive_{index:04d}"
    with open(out_dir / f"{base_name}.zw", "w", encoding="utf-8") as f:
        f.write(zw_content)
    with open(out_dir / f"{base_name}.json", "w", encoding="utf-8") as f:
        f.write(json_content)


def generate_pair(index, out_dir):
    """Generates a standard random matched .zw and .json file pair."""
    r_idx = random.randint(0, len(DATA["roles"])-1)
    c_idx = random.randint(0, len(DATA["contexts"])-1)
    o_idx = random.randint(0, len(DATA["observations"])-1)
    f_idx = random.randint(0, len(DATA["feelings"])-1)
    n_idx = random.randint(0, len(DATA["needs"])-1)
    req_idx = random.randint(0, len(DATA["requests"])-1)

    con_zw, con_json = [
        (
            "  长度: ≤300字\n  语言: zh-CN\n  风格: 温和、鼓励",
            {"length": "<= 300 words", "language": "zh-CN", "style": "gentle, encouraging"}
        ),
        (
            "  长度: 不限\n  语言: en-US\n  语气: 专业、客观\n  禁止: 讽刺或说教",
            {"length": "unlimited", "language": "en-US", "tone": "professional, objective", "forbidden": "sarcasm or preaching"}
        ),
        (
            "  格式: Markdown表格\n  侧重点: 效率与准确性",
            {"format": "Markdown table", "focus": "efficiency and accuracy"}
        )
    ][random.randint(0, 2)]

    t_zw, t_json = [
        ("[代码高亮, 语法检查]", ["code_highlighting", "syntax_check"]),
        ("[情绪分析仪, 历史工单查询, 知识库检索]", ["emotion_analyzer", "historical_ticket_query", "knowledge_base_retrieval"]),
        ("[静态代码分析工具, 内存泄漏检测器]", ["static_code_analyzer", "memory_leak_detector"])
    ][random.randint(0, 2)]

    out_idx = random.randint(0, len(DATA["outputs"])-1)

    m_zw, m_json = [
        ("  已讨论主题: [协议语法, 基本指令]\n  会话轮次: 3", {"discussed_topics": ["protocol syntax", "basic directives"], "conversation_turn": 3}),
        ("  用户偏好: 喜欢直接给代码\n  历史错误率: 较高", {"user_preference": "prefers direct code", "historical_error_rate": "high"}),
        ("  工单状态: 已升级\n  VIP等级: 黄金", {"ticket_status": "escalated", "vip_level": "gold"})
    ][random.randint(0, 2)]

    zw_content = f"""#角色 {DATA['roles'][r_idx]['zw']}

#上下文 {DATA['contexts'][c_idx]['zw']}

#观 {DATA['observations'][o_idx]['zw']}
#感 {DATA['feelings'][f_idx]['zw']}
#需 {DATA['needs'][n_idx]['zw']}
#请 {DATA['requests'][req_idx]['zw']}

#约束 {{
{con_zw}
}}

#工具 {t_zw}

#输出 {DATA['outputs'][out_idx][0]}

#记忆 {{
{m_zw}
}}
"""
    json_obj = {
        "role": DATA["roles"][r_idx]["en"],
        "context": DATA["contexts"][c_idx]["en"],
        "empathic_chain": {
            "observation": DATA["observations"][o_idx]["en"],
            "feeling": DATA["feelings"][f_idx]["en"],
            "need": DATA["needs"][n_idx]["en"],
            "request": DATA["requests"][req_idx]["en"]
        },
        "constraints": con_json,
        "tools": t_json,
        "output_format": DATA["outputs"][out_idx][1],
        "memory": m_json
    }
    json_content = json.dumps(json_obj, indent=2, ensure_ascii=False)

    base_name = f"sim_{index:04d}"
    with open(out_dir / f"{base_name}.zw", "w", encoding="utf-8") as f:
        f.write(zw_content)
    with open(out_dir / f"{base_name}.json", "w", encoding="utf-8") as f:
        f.write(json_content)

def main():
    parser = argparse.ArgumentParser(description="Generate large-scale ZhiWen dataset")
    parser.add_argument("count", type=int, help="Number of file pairs to generate")
    parser.add_argument("--out", default="large_samples", help="Output directory")
    parser.add_argument("--massive", action="store_true", help="Generate massive architectural complexity samples")
    parser.add_argument("--interagent", action="store_true", help="Generate massive inter-agent communication samples")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating {args.count} file pairs in '{args.out}/' (Massive: {args.massive}, Inter-agent: {args.interagent})...")
    for i in range(args.count):
        if args.interagent:
            generate_interagent_pair(i, out_dir)
        elif args.massive:
            generate_massive_pair(i, out_dir)
        else:
            generate_pair(i, out_dir)
    print("Done.")

if __name__ == "__main__":
    main()
