# reporting/exporter.py

from reporting.html_reporter import generate_html_report
from reporting.markdown_reporter import generate_markdown_report
import json
import os
import time

def export_json(actions, path="reports/task_report.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(actions, f, indent=2, ensure_ascii=False)
    print(f"📄 JSON 报告已生成：{path}")

def export_failed_tasks(actions, path="reports/retry_failed.json"):
    failed_tasks = [a.get("task") for a in actions if not a.get("success") and "task" in a]
    if failed_tasks:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(failed_tasks, f, indent=2, ensure_ascii=False)
        print(f"⚠️ 已导出失败任务：{path}")
    else:
        print("✅ 所有任务成功，无需生成失败任务文件")

def export_all_reports(actions, base_filename="task_report"):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    html_path  = f"reports/{base_filename}_{timestamp}.html"
    md_path    = f"reports/{base_filename}_{timestamp}.md"
    json_path  = f"reports/{base_filename}_{timestamp}.json"
    retry_path = f"reports/{base_filename}_{timestamp}_retry_failed.json"

    # 多格式输出
    generate_html_report(output_path=html_path)
    generate_markdown_report(actions, output_path=md_path)
    export_json(actions, path=json_path)
    export_failed_tasks(actions, path=retry_path)

    print("\n✅ 所有报告格式已导出：")
    print(f"- HTML: {html_path}")
    print(f"- Markdown: {md_path}")
    print(f"- JSON: {json_path}")
    print(f"- Retry Tasks: {retry_path}")
