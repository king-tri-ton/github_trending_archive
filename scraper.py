import requests
from datetime import datetime
from config import LANGUAGE
from database import insert_trends
from bs4 import BeautifulSoup

def fetch_trending_repos(language):
    url = f'https://github.com/trending/{language}?since=daily'
    response = requests.get(url)
    return response.text

def parse_trending_repos(html, date, language):
    soup = BeautifulSoup(html, 'html.parser')
    for repo in soup.find_all('article', class_='Box-row'):
        h2_tag = repo.find('h2', class_='h3 lh-condensed')
        if h2_tag:
            a_tag = h2_tag.find('a')
            if a_tag:
                project_name = a_tag.get_text(strip=True)
                project_url = 'https://github.com' + a_tag['href']
                
                # Поиск описания
                description_tag = repo.find('p', class_='color-fg-muted')
                description = description_tag.get_text(strip=True) if description_tag else 'No description available'
                
                insert_trends(date, language, project_name, description, project_url)

def scrape():
    date = datetime.now().strftime('%d.%m.%Y')
    for language in LANGUAGE:
        html = fetch_trending_repos(language)
        parse_trending_repos(html, date, language)
