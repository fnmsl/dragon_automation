# plugins/screenshot.py

import time
import os
from reporting.html_reporter import record_action

def run(page, task, context):
    label = task.get("label", "screenshot")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    os.makedirs("screenshots", exist_ok=True)
    
    screenshot_path = f"screenshots/{label}_{timestamp}.png"
    page.screenshot(path=screenshot_path)

    print(f"📸 截图保存为: {screenshot_path}")
    record_action(
        action="screenshot",
        selector="page",
        label=label,
        success=True,
        before_img=screenshot_path,
        after_img=None
    )
