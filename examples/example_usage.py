import sys
sys.path.append('..')  # Adjust the path accordingly if the scraper module is not in the parent directory

from scraper.request_manager import HTTPRequestManager
from scraper.html_parser import HTMLParser
from scraper.dynamic_content_handler import DynamicContentHandler
from scraper.data_preprocessor import DataPreprocessor
from scraper.gpt_integration import GPTIntegration
from utilities.logger import Logger
from scraper.config import BaseConfig

def main():
    # Initialize logger
    logger = Logger('example_usage')

    # Create instances of the core components
    request_manager = HTTPRequestManager()
    html_parser = HTMLParser()
    dynamic_content_handler = DynamicContentHandler()
    data_preprocessor = DataPreprocessor()
    gpt_integration = GPTIntegration()

    # Example target URL
    target_url = 'http://example.com'

    try:
        # Fetch the web page
        logger.logger.info(f'Fetching URL: {target_url}')
        response = request_manager.fetch(target_url)

        # Check if dynamic content needs to be handled
        if BaseConfig.SCRAPE_DYNAMIC_CONTENT:
            logger.logger.info('Handling dynamic content')
            dynamic_content = dynamic_content_handler.process(response)
            content = html_parser.parse(dynamic_content)
        else:
            # Parse the static HTML content
            logger.logger.info('Parsing HTML content')
            content = html_parser.parse(response.text)

        # Preprocess the extracted text
        logger.logger.info('Preprocessing data')
        preprocessed_data = data_preprocessor.preprocess(content)

        # Integrate with GPT-4-turbo-preview
        logger.logger.info('Integrating with GPT-4-turbo-preview')
        gpt_response = gpt_integration.send_to_gpt(preprocessed_data)

        # Output the response from GPT-4-turbo-preview
        logger.logger.info('Output from GPT-4-turbo-preview:')
        print(gpt_response)

    except Exception as e:
        logger.logger.error(f'An error occurred: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
