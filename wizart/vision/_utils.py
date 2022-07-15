import validators


def is_valid_url(url_str):
    return validators.url(url_str)
