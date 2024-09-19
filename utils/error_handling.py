import traceback
from utils.logging import setup_logging

logger = setup_logging()

def handle_error(exception):
    """
    Logs error details including stack trace.
    """
    logger.error(f"An error occurred: {str(exception)}")
    logger.error("Traceback details:")
    logger.error(traceback.format_exc())
