import re


def ci(text: str):
    return re.compile(text, re.IGNORECASE)
