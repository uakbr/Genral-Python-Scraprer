import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from scraper.config import BaseConfig
from utilities.logger import Logger

class HTTPRequestManager:
    def __init__(self):
        self.session = requests.Session()
        self.logger = Logger(__name__)
        self.configure_retries()

    def configure_retries(self):
        retries = Retry(
            total=BaseConfig.MAX_RETRIES,
            backoff_factor=BaseConfig.RETRY_DELAY,
            status_forcelist=[500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def make_request(self, url, method='GET', headers=None, params=None, data=None, json=None):
        if headers is None:
            headers = {'User-Agent': BaseConfig.USER_AGENT}
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=BaseConfig.REQUEST_TIMEOUT
            )
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            self.logger.logger.error(f'HTTP error occurred: {http_err}')
        except requests.exceptions.ConnectionError as conn_err:
            self.logger.logger.error(f'Connection error occurred: {conn_err}')
        except requests.exceptions.Timeout as timeout_err:
            self.logger.logger.error(f'Timeout error occurred: {timeout_err}')
        except requests.exceptions.RequestException as req_err:
            self.logger.logger.error(f'Unexpected error occurred: {req_err}')
        return None

# Example usage
if __name__ == "__main__":
    request_manager = HTTPRequestManager()
    response = request_manager.make_request('https://example.com')
    if response:
        print(response.text)
