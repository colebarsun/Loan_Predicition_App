import requests
from bs4 import BeautifulSoup
from utils.logging import setup_logging
from scraper.pagination import get_all_pages
from scraper.login import authenticate_user

logger = setup_logging()

def scrape_page(url, session):
    """
    Scrapes a single page for loan-related data
    """
    try:
        logger.info(f"Scraping URL: {url}")
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        loans = soup.find_all('div', class_='loan-container')
        data = []

        for loan in loans:
            lender_name = loan.find('h2', class_='lender-name').text.strip()
            interest_rate = loan.find('span', class_='interest-rate').text.strip()
            loan_term = loan.find('span', class_='loan-term').text.strip()
            max_loan_amount = loan.find('span', class_='max-loan-amount').text.strip()
            data.append([lender_name, interest_rate, loan_term, max_loan_amount])

        return data
    except Exception as e:
        logger.error(f"Failed to scrape page {url}: {str(e)}")
        raise e

def scrape_website(base_url):
    """
    Scrapes all pages of the website
    """
    session = authenticate_user()  # Uses login functionality if required
    all_pages = get_all_pages(base_url, session)

    all_data = []
    for page_url in all_pages:
        data = scrape_page(page_url, session)
        all_data.extend(data)

    return all_data

if __name__ == "__main__":
    base_url = 'https://example-loans-website.com/loans'
    loan_data = scrape_website(base_url)
    logger.info(f"Scraped {len(loan_data)} loan records.")
