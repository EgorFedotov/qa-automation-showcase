from playwright.sync_api import Page


class LoginPage:
    """Page Object for the SauceDemo login screen."""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def open(self, base_url: str) -> "LoginPage":
        self.page.goto(base_url)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self

    def error_text(self) -> str:
        return self.error_message.inner_text()
