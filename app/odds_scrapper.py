import requests
from bs4 import BeautifulSoup

def get_odds_betano():
    url = 'https://www.betano.com/sports/football/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Exemplo de scraping, ajustar conforme o HTML real da Betano
    odds = soup.find_all('div', class_='odd-class')
    return odds
