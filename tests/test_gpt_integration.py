import unittest
from unittest.mock import patch
from scraper.gpt_integration import GPTIntegration

class TestGPTIntegration(unittest.TestCase):
    def setUp(self):
        self.gpt_integration = GPTIntegration()

    @patch('scraper.gpt_integration.requests.post')
    def test_send_to_gpt_success(self, mock_post):
        # Mocking the response of the GPT API
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'response': 'Mocked GPT-4-turbo-preview response'}

        # Call the method
        result = self.gpt_integration.send_to_gpt("Test text")

        # Assertions to check the correct behavior
        self.assertEqual(result, {'response': 'Mocked GPT-4-turbo-preview response'})
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertEqual(kwargs['headers'], self.gpt_integration.headers)
        self.assertEqual(kwargs['json']['prompt'], "Test text")

    @patch('scraper.gpt_integration.requests.post')
    def test_send_to_gpt_failure(self, mock_post):
        # Mocking the response of the GPT API to simulate a failure
        mock_response = mock_post.return_value
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = Exception("Mocked exception")

        # Call the method and assert it raises an exception
        with self.assertRaises(Exception) as context:
            self.gpt_integration.send_to_gpt("Test text")

        # Check if the exception raised is the one we mocked
        self.assertTrue("Mocked exception" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
