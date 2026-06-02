import pytest

from components.header import Header
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.helpers import generate_email
from utils.types import SignupData


@pytest.fixture
def header(page):
    return Header(page)


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)


@pytest.fixture
def signup_data() -> SignupData:
    return {
        "name": "Test User",
        "email": generate_email(),
        "password": "1234567u",
        "password_confirm": "1234567u",
    }
