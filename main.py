from playwright.sync_api import sync_playwright
from core.engine import run_task_flow
from reporting.exporter import export_all_reports

context = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    run_task_flow("tasks/sample_login_flow.json", page, context)
    browser.close()

# 获取执行日志
actions = globals().get("report_log", [])

# 🧠 一键导出 HTML + Markdown + JSON + Retry失败任务
export_all_reports(actions)
