"""
config.py

Central configuration file for scraper settings.
"""

# Define the base configuration for the scraper
class BaseConfig:
    # User-Agent to be used in HTTP headers to simulate a real browser
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    # Default timeout for HTTP requests
    REQUEST_TIMEOUT = 10

    # Maximum number of retries for HTTP requests
    MAX_RETRIES = 3

    # Delay between retries in seconds
    RETRY_DELAY = 5

    # Whether to scrape dynamic content by default
    SCRAPE_DYNAMIC_CONTENT = False

    # Default depth for scraping
    SCRAPING_DEPTH = 1

    # Base URL for GPT-4-turbo-preview API
    GPT_API_BASE_URL = 'https://api.openai.com/v1/engines/gpt-4-turbo-preview/completions'

    # API key for GPT-4-turbo-preview
    GPT_API_KEY = 'your-gpt-api-key'

    # Default output format for scraped data
    OUTPUT_FORMAT = 'json'  # Options: 'json', 'csv'

    # Default log level
    LOG_LEVEL = 'INFO'  # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'

    # Selenium WebDriver executable path
    SELENIUM_DRIVER_PATH = '/path/to/your/webdriver'

    # Rate limiting settings
    RATE_LIMIT_ENABLED = True
    RATE_LIMIT_REQUESTS = 10
    RATE_LIMIT_PERIOD = 60  # In seconds

# Development-specific configurations
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

# Production-specific configurations
class ProductionConfig(BaseConfig):
    DEBUG = False

# Choose the appropriate configuration based on the environment
# This can be set through an environment variable or directly in the code
ENVIRONMENT = 'development'  # Options: 'development', 'production'

if ENVIRONMENT == 'development':
    CurrentConfig = DevelopmentConfig
else:
    CurrentConfig = ProductionConfig

# Export the current configuration to be used by the scraper
config = CurrentConfig()
