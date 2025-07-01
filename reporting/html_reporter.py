# reporting/html_reporter.py

import time
import os
from jinja2 import Environment, FileSystemLoader

# 在内存中记录所有任务状态
def record_action(action, selector, label, success, before_img=None, after_img=None, error_msg=None):
    action_log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "selector": selector,
        "label": label,
        "success": success,
        "before_img": before_img,
        "after_img": after_img,
        "error_msg": error_msg
    }
    if "report_log" not in globals():
        globals()["report_log"] = []
    globals()["report_log"].append(action_log)


def generate_html_report(output_path="reports/task_report.html"):
    os.makedirs("reports", exist_ok=True)
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    html = template.render(actions=globals().get("report_log", []))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"📄 报告已生成：{output_path}")
