"""
Project: ReconShield

Module:
URL Validator

Responsibility:
Url Validator is responsible for validating the given URL and returning the normalized URL.
Also remove www. and add https:// if not present in the URL.

Author:
Alen Joy

TODO:
Validate URL format
Normalize URL
Handle invalid input
Return normalized URL
Write unit tests
"""

def validate_url(user_input):
    if user_input is None or user_input.strip() =="":
        return False, None
    # Implementation for URL validation and normalization goes here
    normalized_url = user_input.strip().lower()
    normalized_url = normalized_url.replace("www.", "")
    if not (
    normalized_url.startswith("https://")
    or normalized_url.startswith("http://")):

        normalized_url = "https://" + normalized_url
    
    if "@" in normalized_url or "." not in normalized_url:
        return False, None  
    
    return True, normalized_url