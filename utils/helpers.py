from playwright.sync_api import Page
import re


def open_app(page: Page):
    page.goto("http://beholdaword.atwebpages.com/")


def ci(text: str):
    return re.compile(text, re.IGNORECASE)
