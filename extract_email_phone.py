import re
import requests
from bs4 import BeautifulSoup

# Function to extract email addresses from text
def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(email_pattern, text)

# Function to extract phone numbers from text
def extract_phone_numbers(text):
    phone_pattern = r'\b(?:\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}\b'
    return re.findall(phone_pattern, text)

# Function to scan a website and extract email addresses and phone numbers
def scan_website(url):
    # Send an HTTP GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text content of the webpage
        webpage_text = soup.get_text()

        # Extract email addresses and phone numbers from the text content
        email_addresses = extract_emails(webpage_text)
        phone_numbers = extract_phone_numbers(webpage_text)

        # Print the extracted email addresses and phone numbers
        print("Email addresses:")
        for email in email_addresses:
            print(email)

        print("\nPhone numbers:")
        for phone in phone_numbers:
            print(phone)

        file_path="mail.txt"
        with open(file_path,"w") as file:
            for email in email_addresses :
                file.write(email + "\n")

        file_path="no.txt"
        with open(file_path,"w") as file:
            for phone in phone_numbers :
                file.write(phone + "\n")
    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)


# Take the URL as user input
url = input("Enter the URL of the website to scan: ")

# Call the scan_website function with the user-provided URL
scan_website(url)

