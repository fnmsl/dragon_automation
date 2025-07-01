# resilience/fallback.py

import time
import os

def try_selectors(page, action_fn, selectors, label):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    for selector in selectors:
        try:
            print(f"🔍 尝试 selector: {selector}")
            page.wait_for_selector(selector, timeout=5000)
            element = page.locator(selector)

            before_path = f"screenshots/{label}_before_{timestamp}.png"
            after_path = f"screenshots/{label}_after_{timestamp}.png"

            page.screenshot(path=before_path)
            action_fn(element)  # 执行传入的操作，如 element.click()
            page.screenshot(path=after_path)

            return selector, before_path, after_path

        except Exception as e:
            print(f"⚠️ 失败：{selector} | 错误：{e}")
            continue

    raise Exception("所有选择器均尝试失败")
