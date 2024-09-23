import requests
from bs4 import BeautifulSoup

def google_search(query):
    # Format the search query
    query = query.replace(' ', '+')
    url = f'https://www.google.com/search?q={query}'
    
    # Set headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Send request to Google
    response = requests.get(url, headers=headers)
    
    # Check for valid response
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract search result titles and URLs
        for g in soup.find_all('div', class_='g'):
            title = g.find('h3')
            if title:
                title_text = title.text
                link = g.find('a')['href']
                print(f'Title: {title_text}')
                print(f'Link: {link}')
                print('-' * 60)
    else:
        print(f'Failed to retrieve search results. Status code: {response.status_code}')

# Example search
google_search('Flask Firebase web scraping example')
