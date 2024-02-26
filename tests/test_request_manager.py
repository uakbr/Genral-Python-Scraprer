import unittest
from unittest.mock import patch
from requests.exceptions import RequestException

from scraper.request_manager import RequestManager

class TestRequestManager(unittest.TestCase):

    @patch('scraper.request_manager.requests')
    def test_get_page_success(self, mock_requests):
        # Arrange
        url = 'http://example.com'
        expected_response = mock_requests.get.return_value
        expected_response.status_code = 200
        expected_response.text = '<html>content</html>'
        request_manager = RequestManager()

        # Act
        response = request_manager.get_page(url)

        # Assert
        self.assertEqual(response, expected_response.text)
        mock_requests.get.assert_called_once_with(url)

    @patch('scraper.request_manager.requests')
    def test_get_page_failure(self, mock_requests):
        # Arrange
        url = 'http://example.com'
        mock_requests.get.side_effect = RequestException
        request_manager = RequestManager()

        # Act & Assert
        with self.assertRaises(RequestException):
            request_manager.get_page(url)

    @patch('scraper.request_manager.requests')
    def test_get_page_with_retry(self, mock_requests):
        # Arrange
        url = 'http://example.com'
        mock_requests.get.side_effect = [RequestException, mock_requests.get.return_value]
        mock_requests.get.return_value.status_code = 200
        mock_requests.get.return_value.text = '<html>content</html>'
        request_manager = RequestManager(retry_count=2)

        # Act
        response = request_manager.get_page(url)

        # Assert
        self.assertEqual(response, mock_requests.get.return_value.text)
        self.assertEqual(mock_requests.get.call_count, 2)

    @patch('scraper.request_manager.requests')
    def test_get_page_with_max_retries_exceeded(self, mock_requests):
        # Arrange
        url = 'http://example.com'
        mock_requests.get.side_effect = RequestException
        request_manager = RequestManager(retry_count=3)

        # Act & Assert
        with self.assertRaises(RequestException):
            request_manager.get_page(url)
        self.assertEqual(mock_requests.get.call_count, 3)

if __name__ == '__main__':
    unittest.main()
