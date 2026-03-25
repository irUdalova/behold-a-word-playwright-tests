from playwright.sync_api import Page
from utils.helpers import ci
from components.header import Header


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = Header(page)

    def open(self):
        self.page.goto("/")

    def hero_explore_button(self):
        hero = self.page.locator("main section").first
        return hero.get_by_role("link", name=ci("EXPLORE"))

    def go_to_explore_from_hero(self):
        self.hero_explore_button().click()

    def random_word(self):
        return self.page.locator("section.random-word").get_by_role("link")

    def go_to_random_word(self):
        self.random_word().click()

    def top_favorites(self):
        return self.page.locator("section.top-rated").get_by_role("link")

    def first_favorite_word(self):
        return self.top_favorites().first

    def go_to_first_favorite_word(self):
        self.first_favorite_word().click()
