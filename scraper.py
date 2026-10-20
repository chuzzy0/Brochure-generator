import requests
from bs4 import BeautifulSoup

def fetch_website_contents(url: str) -> str:
    """Fetches and extracts clean text content from a given URL."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.extract()
        
    return soup.get_text(separator="\n", strip=True)