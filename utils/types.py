from typing import TypedDict


class SignupData(TypedDict):
    name: str
    email: str
    password: str
    password_confirm: str
