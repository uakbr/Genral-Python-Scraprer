import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Create file handler which logs even debug messages
        fh = logging.FileHandler(f'logs/{name}_{datetime.now().strftime("%Y%m%d%H%M%S")}.log')
        fh.setLevel(level)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # Create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger

# Example usage:
# logger = Logger(__name__).get_logger()
# logger.info('This is an info message')
# logger.error('This is an error message')
