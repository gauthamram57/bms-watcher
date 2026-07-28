from playwright.sync_api import sync_playwright

TARGET_DATE = "20260801"


def check_booking(url: str) -> bool:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, wait_until="networkidle")

        current_url = page.url
        print("Current URL:", current_url)

        browser.close()

        return current_url.endswith(TARGET_DATE)
