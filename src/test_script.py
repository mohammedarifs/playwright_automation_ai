from playwright.sync_api import sync_playwright




def test_scripting():
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        page.screenshot(path="./screenshots/example.png")
        browser.close()