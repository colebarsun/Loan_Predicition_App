session = requests.Session()

# URL of the login page
login_url = 'https://example-loans-website.com/login'

# Login credentials
login_payload = {
    'username': 'your_username',
    'password': 'your_password'
}

# Perform login
session.post(login_url, data=login_payload)

# Now use the session to scrape pages that require login
response = session.get('https://example-loans-website.com/loans/page-1.html')
