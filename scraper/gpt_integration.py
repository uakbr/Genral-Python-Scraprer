import requests
import json
from .config import GPT_API_URL, GPT_API_KEY

class GPTIntegration:
    def __init__(self):
        self.api_url = GPT_API_URL
        self.headers = {
            'Authorization': f'Bearer {GPT_API_KEY}',
            'Content-Type': 'application/json'
        }

    def send_to_gpt(self, text_data):
        """
        Sends preprocessed text data to GPT-4-turbo-preview for analysis.
        
        :param text_data: Preprocessed text to be sent to GPT-4-turbo-preview.
        :return: The response from GPT-4-turbo-preview.
        """
        payload = {
            'prompt': text_data,
            'max_tokens': 1024,  # Adjust as needed
            'temperature': 0.7,  # Adjust as needed
            # Add any other parameters required by GPT-4-turbo-preview API
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Example usage:
# gpt_integration = GPTIntegration()
# result = gpt_integration.send_to_gpt("Extracted text to be analyzed by GPT-4-turbo-preview.")
# print(result)
