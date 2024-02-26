"""
dynamic_interaction_plugins.py

This module contains plugins for specific dynamic interactions that can be used
with the DynamicContentHandler to perform complex scraping tasks on dynamic web pages.
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from scraper.dynamic_content_handler import DynamicContentHandler
from utilities.logger import Logger

class DynamicInteractionPlugin:
    def __init__(self, content_handler):
        if not isinstance(content_handler, DynamicContentHandler):
            raise ValueError("content_handler must be an instance of DynamicContentHandler")
        self.content_handler = content_handler
        self.logger = Logger(__name__).logger

    def perform_interaction(self):
        raise NotImplementedError("Subclasses must implement the perform_interaction method")

class InfiniteScrollPlugin(DynamicInteractionPlugin):
    """
    A plugin to handle infinite scrolling pages.
    """
    def __init__(self, content_handler, max_scrolls=10, scroll_pause_time=1.5):
        super().__init__(content_handler)
        self.max_scrolls = max_scrolls
        self.scroll_pause_time = scroll_pause_time

    def perform_interaction(self):
        driver = self.content_handler.driver
        scrolls_performed = 0
        last_height = driver.execute_script("return document.body.scrollHeight")

        while scrolls_performed < self.max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.content_handler.wait(self.scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            scrolls_performed += 1

        return scrolls_performed

class ClickToRevealContentPlugin(DynamicInteractionPlugin):
    """
    A plugin to handle pages where content is revealed after clicking a button or link.
    """
    def __init__(self, content_handler, css_selector, wait_time=3):
        super().__init__(content_handler)
        self.css_selector = css_selector
        self.wait_time = wait_time

    def perform_interaction(self):
        driver = self.content_handler.driver
        try:
            element = driver.find_element_by_css_selector(self.css_selector)
            ActionChains(driver).move_to_element(element).click().perform()
            self.content_handler.wait(self.wait_time)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f'Error performing click interaction: {e}')
            return False
        return True

# Additional plugins can be defined here following the same structure.

