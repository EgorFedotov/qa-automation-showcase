"""Root pytest configuration.

Attaches a Playwright screenshot to the Allure report whenever a UI test fails.
"""
import allure
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot-on-failure",
                attachment_type=allure.attachment_type.PNG,
            )
