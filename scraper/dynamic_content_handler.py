from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraper.config import BaseConfig
from utilities.logger import Logger

class DynamicContentHandler:
    def __init__(self, driver_path='chromedriver', headless=True):
        self.logger = Logger(__name__).logger
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.options.add_argument(f'user-agent={BaseConfig.USER_AGENT}')
        self.driver = webdriver.Chrome(executable_path=driver_path, options=self.options)

    def fetch_dynamic_content(self, url, wait_time=10, element_to_wait_for=None):
        """
        Fetches dynamic content from a URL by using Selenium WebDriver to render JavaScript.
        Optionally waits for a specific element to be present before returning the page source.
        """
        try:
            self.driver.get(url)
            if element_to_wait_for:
                WebDriverWait(self.driver, wait_time).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, element_to_wait_for))
                )
            return self.driver.page_source
        except Exception as e:
            self.logger.error(f'Error fetching dynamic content from {url}: {e}')
            return None

    def perform_click(self, css_selector):
        """
        Performs a click action on an element specified by the CSS selector.
        """
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            element.click()
        except Exception as e:
            self.logger.error(f'Error performing click action: {e}')

    def scroll_to_bottom(self):
        """
        Scrolls to the bottom of the page.
        """
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            self.logger.error(f'Error scrolling to bottom: {e}')

    def close(self):
        """
        Closes the Selenium WebDriver and quits the browser.
        """
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

