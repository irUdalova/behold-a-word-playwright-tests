from playwright.sync_api import Page, expect

from utils.helpers import ci


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_role("textbox", name=ci("Email"))
        self.password_input = page.get_by_role("textbox", name=ci("Password"))
        self.submit_button = page.get_by_role("button", name=ci("Log in"))
        self.form = page.locator("form")

    def open(self):
        self.page.goto("/login")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_global_error(self, text):
        expect(self.page.get_by_text(ci(text))).to_be_visible()

    def expect_field_error(self, text):
        expect(self.form.get_by_text(ci(text))).to_be_visible()

    def go_to_signup(self):
        self.page.locator("main").get_by_role("link", name=ci("Sign up")).click()
