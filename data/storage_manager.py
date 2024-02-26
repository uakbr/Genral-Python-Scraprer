import json
import csv
import os
from scraper.config import BaseConfig
from utilities.logger import Logger

class StorageManager:
    def __init__(self, output_format=BaseConfig.OUTPUT_FORMAT):
        self.output_format = output_format
        self.logger = Logger(__name__).logger
        self.data_folder = 'data'
        self.ensure_data_folder_exists()

    def ensure_data_folder_exists(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
            self.logger.info(f"Created data folder: {self.data_folder}")

    def get_output_file_path(self, prefix='scraped_data'):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{prefix}_{timestamp}.{self.output_format}"
        return os.path.join(self.data_folder, file_name)

    def save_data(self, data, prefix='scraped_data'):
        file_path = self.get_output_file_path(prefix)
        try:
            if self.output_format == 'json':
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            elif self.output_format == 'csv':
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data[0].keys())  # Assuming all items have the same keys
                    for item in data:
                        writer.writerow(item.values())
            self.logger.info(f"Data successfully saved to {file_path}")
        except Exception as e:
            self.logger.error(f"Error saving data to {file_path}: {e}")

# Example usage:
# storage_manager = StorageManager()
# storage_manager.save_data(scraped_data, prefix='example_site')
