"""
data_preprocessor.py

Cleans and preprocesses text data extracted by the web scraping framework.
"""

from utilities.helpers import normalize_whitespace, remove_special_characters
from scraper.config import BaseConfig

class DataPreprocessor:
    def __init__(self, config=BaseConfig):
        self.config = config

    def preprocess_text(self, text):
        """
        Preprocess the extracted text by normalizing whitespace and removing special characters.
        """
        text = normalize_whitespace(text)
        text = remove_special_characters(text)
        return text

    def preprocess_batch(self, texts):
        """
        Preprocess a batch of texts.
        """
        return [self.preprocess_text(text) for text in texts]

# If this module is run directly, demonstrate its functionality
if __name__ == "__main__":
    preprocessor = DataPreprocessor()
    
    sample_texts = [
        "  This is a   sample text! It has whitespace issues.  ",
        "Another text@with#special$characters&to*remove+"
    ]
    
    print("Original texts:")
    for text in sample_texts:
        print(repr(text))
    
    processed_texts = preprocessor.preprocess_batch(sample_texts)
    
    print("\nProcessed texts:")
    for text in processed_texts:
        print(repr(text))
