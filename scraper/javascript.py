from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from utils.logging import setup_logging

logger = setup_logging()

def scrape_js_page(url):
    """
    Scrapes a JavaScript-rendered page using Selenium and returns the BeautifulSoup object.
    """
    logger.info(f"Loading JavaScript-based page: {url}")

    # Set up headless Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # Wait for JavaScript content to load (adjust the time depending on the website)
    time.sleep(5)  # Wait for JS to execute

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    driver.quit()
    return soup
