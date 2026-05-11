from playwright.sync_api import Page, expect

from utils.helpers import ci, exact_ci


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.get_by_role("textbox", name=ci("Name"))
        self.email_input = page.get_by_role("textbox", name=ci("Email"))
        self.password_input = page.get_by_role("textbox", name=exact_ci("Password"))
        self.password_confirm_input = page.get_by_role(
            "textbox", name=exact_ci("Confirm password")
        )
        self.submit_button = page.get_by_role("button", name=ci("Create account"))
        self.form = page.locator("form")

    def open(self):
        self.page.goto("/signup")

    def signup(self, name: str, email: str, password: str, password_confirm: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.password_confirm_input.fill(password_confirm)
        self.submit_button.click()

    def expect_field_error(self, text):
        expect(self.form.get_by_text(ci(text))).to_be_visible()

    def go_to_login(self):
        self.page.locator("main").get_by_role("link", name=ci("Log in")).click()
