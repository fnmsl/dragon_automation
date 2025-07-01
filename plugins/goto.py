# plugins/goto.py

def run(page, task, context):
    url = task["url"]
    page.goto(url)
    print(f"🚀 跳转到页面: {url}")
