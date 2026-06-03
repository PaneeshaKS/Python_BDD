import logging

def setup_logger():
    logger = logging.getLogger("AutomationLogger")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("logs/automation.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger