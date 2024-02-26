# Usage Guide for the Web Scraping Framework

This document provides a comprehensive guide on how to use the web scraping framework developed for extracting text from both static and dynamic web pages and integrating with GPT-4-turbo-preview.

## Getting Started

Before you begin, ensure that you have installed all the required dependencies listed in `requirements.txt`. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

The framework's behavior can be customized through the `scraper/config.py` file. Here you can set various parameters such as `USER_AGENT`, `REQUEST_TIMEOUT`, `MAX_RETRIES`, `RETRY_DELAY`, and more.

For example, to change the User-Agent, modify the `USER_AGENT` variable:

```python
class BaseConfig:
    USER_AGENT = 'Your Custom User-Agent String Here'
```

## Basic Usage

To use the framework, you need to import and initialize the main components. Here's a simple example of how to scrape a static website:

```python
from scraper.request_manager import RequestManager
from scraper.html_parser import HTMLParser
from scraper.data_preprocessor import DataPreprocessor
from scraper.gpt_integration import GPTIntegration
from utilities.logger import Logger

# Initialize the logger
logger = Logger('scraper_log').logger

# Set the target URL
url = 'https://example.com'

# Create an instance of the RequestManager
request_manager = RequestManager(logger)

# Fetch the page content
response = request_manager.fetch(url)

# Parse the HTML content
parser = HTMLParser(response.content, logger)
text_content = parser.extract_text()

# Preprocess the text data
preprocessor = DataPreprocessor(logger)
clean_text = preprocessor.clean_text(text_content)

# Integrate with GPT-4-turbo-preview
gpt_integration = GPTIntegration(logger)
gpt_response = gpt_integration.send_to_gpt(clean_text)

# Output the response from GPT-4-turbo-preview
print(gpt_response)
```

## Dynamic Content

For dynamic websites that require interaction, use the `DynamicContentHandler`:

```python
from scraper.dynamic_content_handler import DynamicContentHandler

# Initialize the dynamic content handler
dynamic_handler = DynamicContentHandler(logger)

# Perform actions like clicking or scrolling
dynamic_handler.interact_with_page()

# Extract the dynamic content
dynamic_content = dynamic_handler.extract_dynamic_content()

# Continue with preprocessing and GPT integration as shown above
```

## Advanced Usage

For more advanced usage, including custom content filters and dynamic interaction plugins, refer to the `examples/advanced_usage.py` file. This will guide you through the process of extending the framework's capabilities.

## Logging

The framework logs its operations, which can be found in the `logs` directory. The `utilities/logger.py` module sets up the logging configuration.

## Extending the Framework

To extend the framework with new features, please read the `docs/extending_framework.md` for detailed instructions on how to create and integrate plugins.

## Conclusion

This usage guide should help you get started with the web scraping framework. For more detailed information on configuration and extension, please refer to the respective documentation in the `docs` directory.
