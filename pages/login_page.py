from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("/login")

    def login(self, email: str, password: str):
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Log in").click()
