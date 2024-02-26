"""
helpers.py

Helper functions for common tasks within the scraping framework.
"""

import os
from urllib.parse import urljoin
from scraper.config import BaseConfig

def build_absolute_url(base_url, relative_url):
    """
    Construct an absolute URL from a base URL and a relative URL.
    """
    return urljoin(base_url, relative_url)

def create_data_directory(directory_name='data'):
    """
    Create a directory for storing data if it does not already exist.
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def normalize_whitespace(text):
    """
    Replace multiple whitespace characters with a single space and strip leading/trailing spaces.
    """
    return ' '.join(text.split())

def remove_special_characters(text, characters_to_remove="!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"):
    """
    Remove special characters from a string.
    """
    return ''.join(c for c in text if c not in characters_to_remove)

def apply_rate_limiting(last_request_time, rate_limit_period=BaseConfig.RATE_LIMIT_PERIOD):
    """
    Enforce rate limiting by sleeping if the time since the last request is less than the rate limit period.
    """
    if BaseConfig.RATE_LIMIT_ENABLED:
        current_time = time.time()
        time_since_last_request = current_time - last_request_time
        if time_since_last_request < rate_limit_period:
            time.sleep(rate_limit_period - time_since_last_request)
        return current_time
    return last_request_time

def get_file_extension(format):
    """
    Get the file extension based on the specified format.
    """
    if format.lower() == 'json':
        return '.json'
    elif format.lower() == 'csv':
        return '.csv'
    else:
        raise ValueError(f"Unsupported format: {format}")

# Example usage:
# absolute_url = build_absolute_url('https://www.example.com', '/path/to/resource')
# create_data_directory()
# normalized_text = normalize_whitespace('  This   is   some text  ')
# cleaned_text = remove_special_characters(normalized_text)
# last_request_time = apply_rate_limiting(last_request_time)
# file_extension = get_file_extension(BaseConfig.OUTPUT_FORMAT)
