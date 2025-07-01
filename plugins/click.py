# plugins/click.py

from resilience.fallback import try_selectors
from reporting.html_reporter import record_action

def run(page, task, context):
    selectors = task.get("selector") or task.get("selectors")
    label = task.get("label", "click")

    # 保证是列表格式
    if isinstance(selectors, str):
        selectors = [selectors]

    clicked_selector, before_img, after_img = try_selectors(
        page=page,
        action_fn=lambda el: el.click(),
        selectors=selectors,
        label=label
    )

    record_action(
        action="click",
        selector=clicked_selector,
        label=label,
        success=True,
        before_img=before_img,
        after_img=after_img
    )
