import unittest
from scraper.data_preprocessor import DataPreprocessor
from scraper.config import BaseConfig

class TestDataPreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = DataPreprocessor(config=BaseConfig)

    def test_preprocess_text(self):
        # Test normalizing whitespace
        text_with_whitespace = "  This is a   sample text! It has whitespace issues.  "
        processed_text = self.preprocessor.preprocess_text(text_with_whitespace)
        self.assertEqual(processed_text, "This is a sample text! It has whitespace issues.")

        # Test removing special characters
        text_with_special_chars = "Another text@with#special$characters&to*remove+"
        processed_text = self.preprocessor.preprocess_text(text_with_special_chars)
        self.assertEqual(processed_text, "Another textwithspecialcharacterstoremove")

    def test_preprocess_batch(self):
        # Test preprocessing a batch of texts
        batch_of_texts = [
            "  This is a   sample text! It has whitespace issues.  ",
            "Another text@with#special$characters&to*remove+"
        ]
        processed_texts = self.preprocessor.preprocess_batch(batch_of_texts)
        expected_texts = [
            "This is a sample text! It has whitespace issues.",
            "Another textwithspecialcharacterstoremove"
        ]
        self.assertEqual(processed_texts, expected_texts)

if __name__ == '__main__':
    unittest.main()
