from pydoc import html

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed during the 'call' phase
    if report.when == "call" and report.failed:
        # Get the 'page' fixture from the test
        page = item.funcargs.get("page")
        if page:
            # Take a screenshot and save it
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            # Attach it to the Extent Report (if using the plugin)
            if hasattr(item, "extra"):
                item.extra.append("./screenshots/example.png")
