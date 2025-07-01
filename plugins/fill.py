# plugins/fill.py

from reporting.html_reporter import record_action

def run(page, task, context):
    selector = task["selector"]
    value = task["value"]
    label = task.get("label", "fill")
    
    page.wait_for_selector(selector)
    page.fill(selector, value)

    print(f"⌨️ 填入内容: {value} -> {selector}")
    record_action(
        action="fill",
        selector=selector,
        label=label,
        success=True,
        before_img=None,
        after_img=None
    )
