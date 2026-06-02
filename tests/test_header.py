import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from components.header import Header


def test_header_guest_user(home_page: HomePage):
    home_page.open()
    home_page.header.expect_logged_out()


def test_header_logged_in_user(login_page: LoginPage, header: Header):
    login_page.open()
    login_page.login("test-mail@gmail.com", "1234567u")
    header.expect_logged_in()


def test_header_after_logout(login_page: LoginPage, header: Header, page: Page):
    login_page.open()
    login_page.login("test-mail@gmail.com", "1234567u")
    header.expect_logged_in()
    header.logout()
    expect(page).to_have_url(re.compile(r"/?$"))
    header.expect_logged_out()


def test_header_explore_link_navigates_to_explore(page: Page, home_page: HomePage):
    home_page.open()
    expect(home_page.header.link("EXPLORE")).to_be_visible()
    home_page.header.go_to_explore_from_header()
    expect(page).to_have_url(re.compile(r"/explore$"))
    expect(page.get_by_placeholder("Find a word")).to_be_visible()
