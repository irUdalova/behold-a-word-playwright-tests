import re
from playwright.sync_api import Page, expect
from utils.helpers import ci
from pages.home_page import HomePage


def test_home_page_loads_successfully(page: Page, home_page: HomePage):
    home_page.open()
    expect(page).to_have_title(re.compile("Behold-a-Word"))
    expect(page).to_have_url(re.compile(r"/?$"))
    home_page.header.expect_visible()


def test_hero_explore_button_navigates_to_explore(page: Page, home_page: HomePage):
    home_page.open()
    expect(home_page.hero_explore_button()).to_be_visible()
    home_page.go_to_explore_from_hero()
    expect(page).to_have_url(re.compile(r"/explore$"))
    expect(page.get_by_placeholder("Find a word")).to_be_visible()


def test_random_word_link_navigates_to_post(page: Page, home_page: HomePage):
    home_page.open()
    random_word = home_page.random_word()
    expect(random_word).to_be_visible()
    word_text = random_word.inner_text().strip().lower()
    home_page.go_to_random_word()
    expect(page).to_have_url(re.compile(r"/posts/\d+"))
    expect(page.get_by_role("heading", name=ci(word_text))).to_be_visible()


def test_popular_words_are_displayed(home_page: HomePage):
    home_page.open()
    expect(home_page.top_favorites()).to_have_count(3)


def test_popular_word_navigates_to_post(page: Page, home_page: HomePage):
    home_page.open()
    first_favorite_word = home_page.first_favorite_word()
    word_text = first_favorite_word.get_by_role("heading").inner_text().strip().lower()
    home_page.go_to_first_favorite_word()
    expect(page).to_have_url(re.compile(r"/posts/\d+"))
    expect(page.get_by_role("heading", name=ci(word_text))).to_be_visible()
