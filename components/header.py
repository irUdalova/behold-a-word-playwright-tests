from playwright.sync_api import Page, expect
from utils.helpers import ci


class Header:
    def __init__(self, page: Page):
        self.page = page
        self.root = page.locator("header")

    def link(self, name: str):
        return self.root.get_by_role("link", name=ci(name))

    def expect_visible(self):
        expect(self.root).to_be_visible()

    def expect_logged_in(self):
        expect(self.link("MY WORDS")).to_be_visible()
        expect(self.link("FAVORITES")).to_be_visible()
        expect(self.link("PROFILE")).to_be_visible()
        expect(self.link("LOG OUT")).to_be_visible()

        expect(self.link("LOG IN")).to_have_count(0)
        expect(self.link("SIGN UP")).to_have_count(0)

    def expect_logged_out(self):
        expect(self.link("LOG IN")).to_be_visible()
        expect(self.link("SIGN UP")).to_be_visible()

        expect(self.link("MY WORDS")).to_have_count(0)
        expect(self.link("FAVORITES")).to_have_count(0)
        expect(self.link("PROFILE")).to_have_count(0)
        expect(self.link("LOG OUT")).to_have_count(0)

    def logout(self):
        self.root.get_by_role("link", name=ci("LOG OUT")).click()

    def go_to_explore_from_header(self):
        self.root.get_by_role("link", name=ci("EXPLORE")).click()
