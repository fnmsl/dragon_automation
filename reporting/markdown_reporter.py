import os
import time
import json

def generate_markdown_report(actions, output_path="reports/task_report.md"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    success_count = sum(1 for a in actions if a.get("success"))
    total_count = len(actions)
    failure_count = total_count - success_count
    success_rate = round(success_count / total_count * 100, 2) if total_count else 0.0

    lines = [
        f"# ✅ 执行任务报告",
        f"**生成时间：** {timestamp}",
        f"**任务总数：** {total_count}",
        f"**成功数：** {success_count}",
        f"**失败数：** {failure_count}",
        f"**成功率：** {success_rate}%",
        "\n---\n"
    ]

    for idx, action in enumerate(actions, 1):
        status = "🟢 成功" if action.get("success") else "🔴 失败"
        label = action.get("label", "未命名标签")
        selector = action.get("selector", "N/A")
        action_type = action.get("action", "unknown")

        lines.append(f"### 🔹 步骤 {idx}: `{label}` （{action_type}）")
        lines.append(f"- **选择器**：`{selector}`")
        lines.append(f"- **状态**：{status}")
        lines.append(f"- **时间**：{action.get('timestamp', 'N/A')}")

        if action.get("error_msg"):
            lines.append(f"- **错误信息**：`{action['error_msg']}`")

        if action.get("before_img"):
            lines.append(f"- **操作前截图：**\n\n![]({action['before_img']})")
        if action.get("after_img"):
            lines.append(f"- **操作后截图：**\n\n![]({action['after_img']})")

        # 可选打印任务原始 JSON（用于失败重试）
        if action.get("task"):
            lines.append(f"- **原始任务 JSON：**\n\n```json\n{json.dumps(action['task'], indent=2, ensure_ascii=False)}\n```")

        lines.append("\n---\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"📄 Markdown 报告已生成：{output_path}")
