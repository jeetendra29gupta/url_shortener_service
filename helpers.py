import hashlib

import validators


def is_string_an_url(url_string):
    """Check if the string is a valid URL."""
    return validators.url(url_string)


def generate_url_hash(original_url):
    """Generate a shortened URL hash using MD5."""
    shorten_url_hash = hashlib.md5(original_url.encode()).hexdigest()[:7]
    return shorten_url_hash
