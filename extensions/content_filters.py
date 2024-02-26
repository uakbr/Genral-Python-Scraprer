"""
content_filters.py

This module contains plugins for advanced content filtering within the web scraping framework.
These filters can be used to refine the extracted text from web pages, removing or altering
information based on specific criteria.
"""

import re
from bs4 import BeautifulSoup


class BaseContentFilter:
    """
    Base class for content filters. All custom content filters should inherit from this class.
    """
    def apply(self, text, soup=None):
        """
        Apply the filter to the given text.

        :param text: str - The text to filter.
        :param soup: BeautifulSoup - Parsed HTML content to allow for more complex filtering.
        :return: str - The filtered text.
        """
        raise NotImplementedError("Subclasses must implement this method")


class RemoveScriptStyleContentFilter(BaseContentFilter):
    """
    Filter that removes script and style elements from the HTML content.
    """
    def apply(self, text, soup=None):
        if soup is None:
            raise ValueError("soup parameter must not be None for HTML content filtering")

        for script_or_style in soup(['script', 'style']):
            script_or_style.extract()  # Remove these two elements from the BS4 object

        return soup.get_text()


class RegexFilter(BaseContentFilter):
    """
    Filter that applies a regular expression to the text and removes matches.
    """
    def __init__(self, pattern, replacement=''):
        self.pattern = re.compile(pattern)
        self.replacement = replacement

    def apply(self, text, soup=None):
        return self.pattern.sub(self.replacement, text)


class WhitespaceNormalizer(BaseContentFilter):
    """
    Filter that normalizes whitespace in the text, converting multiple spaces into a single space.
    """
    def apply(self, text, soup=None):
        return ' '.join(text.split())


# Example usage:
# To use these filters, instantiate them and call the apply method with the text you want to filter.
# filters = [
#     RemoveScriptStyleContentFilter(),
#     RegexFilter(r'\s+', ' '),
#     WhitespaceNormalizer()
# ]
# for filter in filters:
#     text = filter.apply(text, soup)
