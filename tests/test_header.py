import re
from playwright.sync_api import Page, expect
from utils.helpers import ci
from pages.home_page import HomePage
from pages.login_page import LoginPage
from components.header import Header


def test_header_guest_user(page: Page):
    home = HomePage(page)
    home.open()
    home.header.expect_logged_out()


def test_header_logged_in_user(page: Page):
    login_page = LoginPage(page)
    header = Header(page)
    login_page.open()
    expect(page.get_by_role("heading", name=ci("LOG IN"))).to_be_visible()
    login_page.login("test-mail@gmail.com", "1234567u")
    header.expect_logged_in()


def test_header_after_logout(page: Page):
    login_page = LoginPage(page)
    header = Header(page)
    login_page.open()
    login_page.login("test-mail@gmail.com", "1234567u")
    header.expect_logged_in()
    header.logout()
    expect(page).to_have_url(re.compile(r"/?$"))
    header.expect_logged_out()


def test_header_explore_link_navigates_to_explore(page: Page):
    home = HomePage(page)
    home.open()
    expect(home.header.link("EXPLORE")).to_be_visible()
    home.header.go_to_explore_from_header()
    expect(page).to_have_url(re.compile(r"/explore$"))
    expect(page.get_by_placeholder("Find a word")).to_be_visible()
