import re

from playwright.sync_api import Page, expect
import pytest

from components.header import Header
from pages.signup_page import SignupPage
from utils.types import SignupData


# happy path
def test_user_can_signup(
    signup_page: SignupPage, signup_data: SignupData, header: Header, page: Page
):
    signup_page.open()
    signup_page.signup(**signup_data)
    expect(page).to_have_url(re.compile(r"/?$"))
    header.expect_logged_in()


# negative cases
@pytest.mark.parametrize(
    "override, error_text",
    [
        ({"name": ""}, "Name is required"),
        ({"email": ""}, "Email is required"),
        ({"password": ""}, "Password is required"),
        ({"password_confirm": ""}, "Password confirmation is required"),
    ],
)
def test_signup_required_fields(
    signup_page: SignupPage,
    signup_data: SignupData,
    override: dict[str, str],
    error_text: str,
):
    data = {**signup_data, **override}
    signup_page.open()
    signup_page.signup(**data)

    signup_page.expect_field_error(error_text)


@pytest.mark.parametrize(
    "override, error_text",
    [
        ({"password_confirm": "u7654321"}, "Passwords must match"),
        (
            {"password": "12345u", "password_confirm": "12345u"},
            "Password must be at least 8 characters",
        ),
        (
            {"password": "1234567", "password_confirm": "1234567"},
            "Password must contain at least one letter",
        ),
        (
            {"password": "uuuuuuuu", "password_confirm": "uuuuuuuu"},
            "Password must contain at least one number",
        ),
    ],
)
def test_signup_password_validation(
    signup_page: SignupPage,
    signup_data: SignupData,
    override: dict[str, str],
    error_text: str,
):
    data = {**signup_data, **override}
    signup_page.open()
    signup_page.signup(**data)
    signup_page.expect_field_error(error_text)


def test_signup_with_existing_email(
    signup_page: SignupPage, signup_data: SignupData, header: Header
):
    signup_page.open()
    signup_page.signup(**signup_data)
    header.logout()
    signup_page.open()
    signup_page.signup(**signup_data)
    signup_page.expect_field_error("This email already taken")


def test_login_link_redirects(signup_page: SignupPage, page: Page):
    signup_page.open()
    signup_page.go_to_login()
    expect(page).to_have_url(re.compile(r"/login"))
