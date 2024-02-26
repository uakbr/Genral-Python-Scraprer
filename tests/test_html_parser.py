import unittest
from scraper.html_parser import HTMLParser

class TestHTMLParser(unittest.TestCase):
    def setUp(self):
        self.parser = HTMLParser()

    def test_parse_html_with_valid_content(self):
        html_content = """
        <html>
            <head>
                <title>Test HTML</title>
            </head>
            <body>
                <h1>Heading</h1>
                <p>This is a paragraph.</p>
                <script type="text/javascript">alert('Hello, World!');</script>
                <style type="text/css">body {background-color: #fff;}</style>
            </body>
        </html>
        """
        expected_text = 'Test HTML\nHeading\nThis is a paragraph.\n'
        parsed_text = self.parser.parse_html(html_content)
        self.assertEqual(parsed_text.strip(), expected_text.strip(), "The extracted text does not match the expected result.")

    def test_parse_html_with_empty_content(self):
        html_content = ""
        expected_text = ""
        parsed_text = self.parser.parse_html(html_content)
        self.assertEqual(parsed_text, expected_text, "The extracted text should be empty for empty HTML content.")

    def test_parse_html_with_invalid_content(self):
        html_content = "<html><h1>Without closing tags"
        expected_text = ""
        parsed_text = self.parser.parse_html(html_content)
        self.assertEqual(parsed_text, expected_text, "The extracted text should be empty for invalid HTML content.")

    def test_remove_irrelevant_content(self):
        html_content = """
        <html>
            <head>
                <title>Test HTML</title>
            </head>
            <body>
                <h1>Heading</h1>
                <p>This is a paragraph.</p>
                <script type="text/javascript">alert('Hello, World!');</script>
                <style type="text/css">body {background-color: #fff;}</style>
            </body>
        </html>
        """
        soup = self.parser.get_soup(html_content)
        self.parser.remove_irrelevant_content(soup)
        self.assertIsNone(soup.find('script'), "Script tags should be removed from the soup object.")
        self.assertIsNone(soup.find('style'), "Style tags should be removed from the soup object.")

    def test_extract_text(self):
        html_content = """
        <html>
            <head>
                <title>Test HTML</title>
            </head>
            <body>
                <h1>Heading</h1>
                <p>This is a paragraph.</p>
            </body>
        </html>
        """
        soup = self.parser.get_soup(html_content)
        extracted_text = self.parser.extract_text(soup)
        expected_text = 'Test HTML\nHeading\nThis is a paragraph.\n'
        self.assertEqual(extracted_text.strip(), expected_text.strip(), "The extracted text does not match the expected result.")

if __name__ == '__main__':
    unittest.main()
