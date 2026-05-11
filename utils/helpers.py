import re
import uuid


# case-insensitive
def ci(text: str):
    return re.compile(text, re.IGNORECASE)


def exact_ci(text: str):
    return re.compile(f"^{text}$", re.IGNORECASE)


def generate_email():
    return f"test_{uuid.uuid4().hex[:6]}@mail.com"
