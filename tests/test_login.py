import re
from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage
from utils.helpers import ci


# happy path
def test_user_can_login(login_page: LoginPage, page: Page):
    login_page.open()
    login_page.login("test-mail@gmail.com", "1234567u")
    expect(page).to_have_url(re.compile(r"/?$"))


# negative cases
@pytest.mark.parametrize(
    "email,password,error_text,error_type",
    [
        ("test-mail@gmail.com", "u7654321", "Invalid login", "global"),
        ("", "1234567u", "Email is required", "field"),
        ("test-mail@gmail.com", "", "Password is required", "field"),
        (
            "test-mail-no-signed-up@gmail.com",
            "1234567u",
            "There is no user with that email address",
            "global",
        ),
    ],
)
def test_login_negative(
    login_page: LoginPage, email: str, password: str, error_text: str, error_type: str
):
    login_page.open()
    login_page.login(email, password)
    if error_type == "global":
        login_page.expect_global_error(error_text)
    else:
        login_page.expect_field_error(error_text)


def test_login_both_fields_empty(login_page: LoginPage):
    login_page.open()
    login_page.login("", "")

    login_page.expect_field_error("Email is required")
    login_page.expect_field_error("Password is required")


def test_signup_link_redirects(login_page: LoginPage, page: Page):
    login_page.open()
    login_page.go_to_signup()
    expect(page).to_have_url(re.compile(r"/signup"))
