import requests
from bs4 import BeautifulSoup

def main(url):
    try:
        # Send an HTTP GET request to the specified URL
        r = requests.get(url)
        
        # Parse the HTML content of the page using BeautifulSoup
        doc = BeautifulSoup(r.text, 'html.parser')
        
        # Find all title tags (case-insensitive) in the HTML document
        # Note: 'title' or 'TITLE' will always evaluate to 'title'
        title = doc.find_all('title' or 'TITLE')
        
        # Return the text content of the first title tag found
        return title[0].text
    except:
        # Handle exceptions, return an empty string if an error occurs
        return " "
