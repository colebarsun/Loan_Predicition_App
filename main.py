import requests
from bs4 import BeautifulSoup
import csv

# Base URL of the website to scrape
base_url = 'https://example-loans-website.com/loans/page-{}.html'

# Create or open a CSV file to save the scraped data
with open('loan_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Lender Name', 'Interest Rate', 'Loan Term', 'Max Loan Amount'])  # CSV Header

    # Loop through multiple pages (example: first 5 pages)
    for page in range(1, 6):
        # Construct the URL for the current page
        url = base_url.format(page)
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all loan containers on the page
        loans = soup.find_all('div', class_='loan-container')

        # Loop through each loan container to extract details
        for loan in loans:
            lender_name = loan.find('h2', class_='lender-name').text.strip()  # Extract lender name
            interest_rate = loan.find('span', class_='interest-rate').text.strip()  # Extract interest rate
            loan_term = loan.find('span', class_='loan-term').text.strip()  # Extract loan term
            max_loan_amount = loan.find('span', class_='max-loan-amount').text.strip()  # Extract max loan amount

            # Write the extracted data to the CSV file
            writer.writerow([lender_name, interest_rate, loan_term, max_loan_amount])

            # Print the data to the console (optional)
            print(f"Lender: {lender_name}, Interest Rate: {interest_rate}, Loan Term: {loan_term}, Max Loan Amount: {max_loan_amount}")

print("Scraping completed and data saved to loan_data.csv")
