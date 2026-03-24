from playwright.sync_api import Page, expect
from utils.helpers import open_app
import re


def open_login_page(page: Page):
    open_app(page)
    page.get_by_role("link", name=re.compile("LOG IN", re.IGNORECASE)).click()


def login_user(page: Page, email: str, password: str):
    expect(page.get_by_role("textbox", name="Email")).to_be_visible()
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Log in").click()
