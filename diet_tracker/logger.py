"""System logging module to fulfill Non-Functional Requirements."""

import logging

def setup_logger():
    """Sets up a file-based logger to record app execution and errors."""
    logger = logging.getLogger("DietTracker")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        log_file = "app.log"
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger