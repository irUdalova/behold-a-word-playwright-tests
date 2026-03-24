import re
from playwright.sync_api import Page, expect
from utils.helpers import open_app, ci
from utils.auth import login_user, open_login_page


def test_home_page_loads_successfully(page: Page):
    open_app(page)
    expect(page).to_have_title(re.compile("Behold-a-Word"))
    expect(page).to_have_url(re.compile(r"/?$"))
    expect(page.locator("header")).to_be_visible()


def test_navigation_explore_link_navigates_to_explore(page: Page):
    open_app(page)
    header = page.locator("header")
    header.get_by_role("link", name=ci("EXPLORE")).click()
    expect(page).to_have_url(re.compile(r"/explore$"))
    expect(page.get_by_placeholder("Find a word")).to_be_visible()


def test_navigation_for_guest(page: Page):
    open_app(page)
    header = page.locator("header")
    expect(header.get_by_role("link", name=ci("LOG IN"))).to_be_visible()
    expect(header.get_by_role("link", name=ci("SIGN UP"))).to_be_visible()

    expect(header.get_by_role("link", name=ci("MY WORDS"))).to_have_count(0)
    expect(header.get_by_role("link", name=ci("FAVORITES"))).to_have_count(0)
    expect(header.get_by_role("link", name=ci("PROFILE"))).to_have_count(0)
    expect(header.get_by_role("link", name=ci("LOG OUT"))).to_have_count(0)


def test_navigation_for_logged_in_user(page: Page):
    open_login_page(page)
    expect(page.get_by_role("heading")).to_contain_text(ci("LOG IN"))
    login_user(page, "test-mail@gmail.com", "1234567u")

    expect(page.locator("header")).to_be_visible()
    header = page.locator("header")

    expect(header.get_by_role("link", name=ci("MY WORDS"))).to_be_visible()
    expect(header.get_by_role("link", name=ci("FAVORITES"))).to_be_visible()
    expect(header.get_by_role("link", name=ci("PROFILE"))).to_be_visible()
    expect(header.get_by_role("link", name=ci("LOG OUT"))).to_be_visible()

    expect(header.get_by_role("link", name=ci("LOG IN"))).to_have_count(0)
    expect(header.get_by_role("link", name=ci("SIGN UP"))).to_have_count(0)


def test_hero_explore_button_navigates_to_explore(page: Page):
    open_app(page)
    hero = page.locator("main section").first
    explore_button = hero.get_by_role("link", name=ci("EXPLORE"))
    expect(explore_button).to_be_visible()
    explore_button.click()
    expect(page).to_have_url(re.compile(r"/explore$"))
    expect(page.get_by_placeholder("Find a word")).to_be_visible()


def test_random_word_link_navigates_to_post(page: Page):
    open_app(page)
    random_section = page.locator("section.random-word")
    expect(random_section.get_by_role("link")).to_have_count(1)
    random_word = random_section.get_by_role("link")
    expect(random_word).to_be_visible()
    word_text = random_word.inner_text().strip()
    random_word.click()
    expect(page).to_have_url(re.compile(r"/posts/\d+"))
    expect(page.get_by_role("heading")).to_contain_text(ci(word_text))


def test_popular_words_are_displayed(page: Page):
    open_app(page)
    top_favorites = page.locator("section.top-rated").get_by_role("link")
    expect(top_favorites).to_have_count(3)
    for link in top_favorites.all():
        expect(link).to_be_visible()


def test_popular_word_navigates_to_post(page: Page):
    open_app(page)
    top_favorites_section = page.locator("section.top-rated")
    first_word_link = top_favorites_section.get_by_role("link").first
    word_text = first_word_link.get_by_role("heading").inner_text().strip()
    first_word_link.click()
    expect(page).to_have_url(re.compile(r"/posts/\d+"))
    expect(page.get_by_role("heading")).to_contain_text(ci(word_text))
