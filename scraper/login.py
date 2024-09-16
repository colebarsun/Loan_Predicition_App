import requests
from utils.logging import setup_logging

logger = setup_logging()

def authenticate_user():
    """
    Authenticates the user using credentials and returns a session for authenticated requests.
    """
    login_url = 'https://example-loans-website.com/login'
    credentials = {
        'username': 'your_username',
        'password': 'your_password'
    }
    
    session = requests.Session()
    try:
        logger.info("Attempting login...")
        response = session.post(login_url, data=credentials)
        response.raise_for_status()

        if 'Logout' in response.text:  # Check if login was successful
            logger.info("Login successful.")
            return session
        else:
            logger.error("Login failed.")
            raise Exception("Login failed.")
    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        raise e
