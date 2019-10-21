""" 
Bite 215
"""
import re

def validate_license(key: str):
    """
    Write a regex that matches a PyBites license key
    (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    pattern = r"([A-Z]{2}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8})"
    check: re.Pattern = re.compile(pattern)

    if check.match(key) and len(key) == 38:
        return True
    return False
