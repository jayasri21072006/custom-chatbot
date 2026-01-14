import os
import yaml
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self):
        self.log_dir='logs'
        os.makedirs(self.log_dir, exist_ok=True)
        current_time_stamp=f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.log_file_name=f"log_{current_time_stamp}.log"
        self.log_file_path=os.path.join(self.log_dir,self.log_file_name)
        logging.basicConfig(filename=self.log_file_path,
                            level=logging.INFO,filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger=logging.getLogger()
    def get_logger(self):
        return self.logger