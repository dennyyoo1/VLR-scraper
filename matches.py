from bs4 import BeautifulSoup
import requests
import time

url = "https://www.vlr.gg/matches/results"

response = requests.get(url)
html = response.content

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

table = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == ['wf-card'])

def getMatches():
    links = []
    for row in table.find_all('a', href = True):
        links.append(row['href'])
    return links