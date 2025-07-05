import logging
import os
from datetime import datetime

# log directory
LOGS_DIR = 'logs'
os.makedirs(LOGS_DIR, exist_ok=True)

# creating log file for separate dates
# eg: log_2025-07-04.log
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Config the logging
# format: time - level(like warning, error) - message
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# function to create a logger
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger 
