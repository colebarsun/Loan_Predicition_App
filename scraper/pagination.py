import requests
from bs4 import BeautifulSoup
from utils.logging import setup_logging

logger = setup_logging()

def get_all_pages(base_url, session):
    """
    Get all pages by following pagination links. Returns a list of URLs for all pages.
    """
    try:
        logger.info(f"Fetching first page: {base_url}")
        response = session.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get total number of pages from pagination controls
        pagination = soup.find('ul', class_='pagination')
        last_page = pagination.find_all('a')[-2].text.strip()  # Assumes the second-to-last <a> contains the last page number
        all_pages = [f"{base_url}/page-{i}.html" for i in range(1, int(last_page) + 1)]
        logger.info(f"Total pages to scrape: {len(all_pages)}")

        return all_pages
    except Exception as e:
        logger.error(f"Error in pagination: {str(e)}")
        raise e
