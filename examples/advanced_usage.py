import sys
sys.path.append('..')  # Adjust the path accordingly if the scraper module is not in the parent directory

from scraper.request_manager import RequestManager
from scraper.html_parser import HTMLParser
from scraper.dynamic_content_handler import DynamicContentHandler
from scraper.data_preprocessor import DataPreprocessor
from scraper.gpt_integration import GPTIntegration
from utilities.logger import Logger
from utilities.helpers import build_absolute_url
from scraper.config import BaseConfig
from extensions.content_filters import AdvancedContentFilter
from extensions.dynamic_interaction_plugins import DynamicInteractionPlugin

def main():
    # Initialize the logger
    logger = Logger('AdvancedUsage')

    try:
        # Initialize the components with advanced configurations
        request_manager = RequestManager(
            user_agent=BaseConfig.USER_AGENT,
            timeout=BaseConfig.REQUEST_TIMEOUT,
            max_retries=BaseConfig.MAX_RETRIES,
            retry_delay=BaseConfig.RETRY_DELAY
        )
        html_parser = HTMLParser()
        dynamic_content_handler = DynamicContentHandler()
        data_preprocessor = DataPreprocessor()
        gpt_integration = GPTIntegration(
            api_base_url=BaseConfig.GPT_API_BASE_URL,
            api_key=BaseConfig.GPT_API_KEY
        )

        # Example target URL
        target_url = 'https://example.com/advanced-page'

        # Fetch the page content
        page_content = request_manager.fetch_page(target_url)
        logger.info(f'Fetched content from {target_url}')

        # Parse the HTML content
        parsed_content = html_parser.parse_content(page_content)
        logger.info('Parsed HTML content')

        # Handle dynamic content if necessary
        if BaseConfig.SCRAPE_DYNAMIC_CONTENT:
            dynamic_content = dynamic_content_handler.handle_dynamic_content(target_url)
            parsed_content += dynamic_content
            logger.info('Handled dynamic content')

        # Apply advanced content filtering
        filtered_content = AdvancedContentFilter.filter_content(parsed_content)
        logger.info('Applied advanced content filtering')

        # Preprocess the data
        preprocessed_data = data_preprocessor.preprocess_data(filtered_content)
        logger.info('Preprocessed the data')

        # Integrate with GPT-4-turbo-preview
        gpt_response = gpt_integration.send_to_gpt(preprocessed_data)
        logger.info('Sent data to GPT-4-turbo-preview and received response')

        # Output the response
        print('GPT-4-turbo-preview response:', gpt_response)

    except Exception as e:
        logger.error(f'An error occurred: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
