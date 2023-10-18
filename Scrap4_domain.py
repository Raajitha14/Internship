import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


# Function to extract links
def extract_links(soup, base_url):
    if soup is not None:
        links = []
        for anchor in soup.find_all('a', href=True):
            link = anchor['href']
            
            absolute_url = urljoin(base_url, link)
            links.append(absolute_url)
        return links
    else:
        return []

# Function to extract phone numbers
def extract_phone_numbers(text):
    phone_number_pattern =r'\b(?:\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}\b'

    phone_numbers = set(re.findall(phone_number_pattern, text))
    return phone_numbers

# Function to extract email IDs
def extract_email_ids(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    email_ids = set(re.findall(email_pattern, text))
    return email_ids

def extract_social_media_links(soup):
    # response = requests.get(website_url)
    # soup = BeautifulSoup(response.text, 'html.parser')


    social_media_links = []
    social_media_patterns = [
        r'facebook\.com',
        r'twitter\.com',
        r'linkedin\.com',
        r'instagram\.com',
        r'youtube\.com',
        r'pinterest\.com',
    
    ]

    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        for pattern in social_media_patterns:
            if re.search(pattern, link):
                social_media_links.append(link)

    return social_media_links

# Function to crawl the website recursively using depth-first search
def crawl_website(website_url,main_domain,visited_links,visited_emails,visited_phones):
    print("website processing")
    try:
        if website_url not in visited_links and website_url.startswith(main_domain) and not website_url.endswith(".jpg") and not website_url.endswith(".pdf"):
            print("processing link")
            print(website_url)
            visited_links.add(website_url)


            with open("All_links4.txt","a") as link_file:
                link_file.write(website_url+"\n")
                

            response = requests.get(website_url)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

        
            links = extract_links(soup, website_url)
            phone_numbers = extract_phone_numbers(html_content)
            email_ids = extract_email_ids(html_content)
            social_media_links = extract_social_media_links(soup)

            # Store the extracted data in files without overwriting("a")
            with open("Email4.txt", "a") as email_file:
                for email in email_ids:
                    if email not in visited_emails:
                        visited_emails.add(email)
                        email_file.write(email + "\n")

            with open("Ph_no4.txt", "a") as phone_file:
                for phone in phone_numbers:
                    if phone not in visited_phones:
                        print(phone)
                        visited_phones.add(phone)
                        phone_file.write(phone + "\n")

            with open("SocialMedia4.txt", "a") as file:
                for Slink in social_media_links:
                    file.write(Slink + "\n")

            #print("Links")
            # Recursively crawl linked pages within the main domain
            for link in links:
                crawl_website(link,main_domain,visited_links,visited_emails,visited_phones)
    except :
        print("Error occured while calling",website_url)


#website_url = "http://127.0.0.1:5500/Day_2/Search/index.html"
#main_domain = website_url

#crawl_website(website_url)