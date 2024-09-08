# Find the total number of pages
pagination = soup.find('ul', class_='pagination')
total_pages = int(pagination.find_all('li')[-2].text)

for page in range(1, total_pages + 1):
    # Scraping logic here
