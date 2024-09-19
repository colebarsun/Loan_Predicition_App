import unittest
from scraper.scrape import scrape_page
from scraper.login import authenticate_user

class TestScraper(unittest.TestCase):
    
    def test_scrape_page(self):
        """
        Tests if scraping a single page returns valid loan data.
        """
        session = authenticate_user()  # Mock login for testing
        url = 'https://example-loans-website.com/loans/page-1.html'
        data = scrape_page(url, session)
        self.assertTrue(len(data) > 0)  # Check if data was scraped successfully
        self.assertEqual(len(data[0]), 4)  # Check if each loan record has 4 attributes (lender name, interest rate, etc.)

if __name__ == "__main__":
    unittest.main()
