"""
html_parser.py

Parses HTML content using BeautifulSoup to extract textual information.
"""

from bs4 import BeautifulSoup
from scraper.config import BaseConfig
from utilities.logger import Logger

class HTMLParser:
    def __init__(self):
        self.logger = Logger(__name__)

    def parse_html(self, html_content):
        """
        Parse the given HTML content and extract text.

        :param html_content: HTML content as a string.
        :return: Extracted text as a string.
        """
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            self.remove_irrelevant_content(soup)
            text = self.extract_text(soup)
            return text
        except Exception as e:
            self.logger.logger.error(f"Error parsing HTML content: {e}")
            return ""

    def remove_irrelevant_content(self, soup):
        """
        Remove irrelevant content from the soup object, such as scripts and styles.

        :param soup: BeautifulSoup object.
        """
        for script_or_style in soup(['script', 'style']):
            script_or_style.extract()  # Remove these two elements from the BS4 object

    def extract_text(self, soup):
        """
        Extract text from the BeautifulSoup object.

        :param soup: BeautifulSoup object.
        :return: Cleaned text as a string.
        """
        # Get text and remove leading/trailing whitespaces
        text = soup.get_text(separator=' ', strip=True)
        # Replace multiple spaces with a single space
        text = ' '.join(text.split())
        return text

# Example usage:
if __name__ == "__main__":
    example_html = "<html><head><title>Test</title></head><body><p>Hello, World!</p></body></html>"
    parser = HTMLParser()
    extracted_text = parser.parse_html(example_html)
    print(extracted_text)  # Output should be "Hello, World!"
