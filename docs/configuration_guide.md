# Configuration Guide

This guide provides detailed instructions on how to configure the web scraping framework to suit your specific needs. The framework is designed to be flexible and customizable, allowing you to adjust various settings related to HTTP requests, HTML parsing, dynamic content handling, and integration with GPT-4-turbo-preview.

## Base Configuration

The `BaseConfig` class in `scraper/config.py` serves as the central configuration for the scraper settings. Here are the key settings you can customize:

- `USER_AGENT`: Set the User-Agent string to simulate a real browser during HTTP requests.
- `REQUEST_TIMEOUT`: Define the default timeout for HTTP requests in seconds.
- `MAX_RETRIES`: Specify the maximum number of retries for HTTP requests in case of failures.
- `RETRY_DELAY`: Set the delay between retries in seconds.
- `SCRAPE_DYNAMIC_CONTENT`: Enable or disable scraping of dynamic content by default.
- `SCRAPING_DEPTH`: Define the default depth for recursive scraping.
- `GPT_API_BASE_URL`: Set the base URL for the GPT-4-turbo-preview API.
- `GPT_API_KEY`: Provide your API key for GPT-4-turbo-preview.

To modify these settings, open `scraper/config.py` and adjust the values of the corresponding class variables.

## HTTP Request Manager

The `HTTPRequestManager` class in `scraper/request_manager.py` is responsible for making HTTP requests. It uses the settings from `BaseConfig` to configure retries and handle errors. You can customize the retry behavior and the list of HTTP status codes that trigger a retry.

## HTML Parser

The `HTMLParser` class in `scraper/html_parser.py` uses BeautifulSoup to parse HTML content. You can extend or override the parsing logic to extract different types of information from web pages.

## Dynamic Content Handler

For scraping dynamic content, the `dynamic_content_handler.py` module utilizes Selenium WebDriver. You can configure the Selenium options, such as headless mode and custom browser preferences, to optimize the scraping of JavaScript-rendered pages.

## GPT-4-turbo-preview Integration

The `gpt_integration.py` module formats the scraped data and sends it to the GPT-4-turbo-preview API. Ensure that you have set the correct `GPT_API_BASE_URL` and `GPT_API_KEY` in the `BaseConfig` class. You can also customize the payload structure to match the requirements of your specific use case.

## Logging

The `utilities/logger.py` module provides a custom logging mechanism. You can configure the logging level, output format, and destination (e.g., console, file) to suit your monitoring needs.

## Extending the Framework

The framework supports plugin-based extensions for content extraction and preprocessing. You can create custom plugins and place them in the `extensions/` directory. Refer to the `extending_framework.md` document for guidelines on developing and integrating plugins.

## Testing

Before deploying your scraper, make sure to run the tests located in the `tests/` directory to verify that your configuration changes work as expected.

## Conclusion

By following this configuration guide, you can tailor the web scraping framework to meet the requirements of your scraping tasks. The modular design ensures that you can easily update and extend the framework as needed.

