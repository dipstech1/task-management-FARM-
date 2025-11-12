from loguru import logger
import sys
import os

logger.remove(0)

log_folder = "logs"
log_file_name = "error.log"

os.makedirs(log_folder, exist_ok=True)

log_file_path = os.path.join(log_folder, log_file_name)


logger.add(
         sys.stdout,
         level="DEBUG",
         format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>",
         colorize=True
         ) 

# Sink 2: JSON file for production monitoring
logger.add("app.log",
         serialize=True,
         level="INFO")

# Sink 3: Error-only file for alerts
logger.add(log_file_path,
         level="ERROR",rotation="500 MB", retention="10 days")

def log_error(msg:str):
    logger.error(msg)

def log_info(msg:str):
    logger.info(msg)