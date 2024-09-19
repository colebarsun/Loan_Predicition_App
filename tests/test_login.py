import unittest
from scraper.login import authenticate_user

class TestLogin(unittest.TestCase):
    
    def test_authenticate_user(self):
        """
        Tests the login functionality.
        """
        session = authenticate_user()
        self.assertIsNotNone(session)  # Ensure a session is returned after successful login
        self.assertTrue(hasattr(session, 'get'))  # Ensure session can make HTTP requests

if __name__ == "__main__":
    unittest.main()
