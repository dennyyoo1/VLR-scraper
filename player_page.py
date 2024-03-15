from bs4 import BeautifulSoup
import requests

def getPlayers(url):
    url = url

    response = requests.get(url)
    html = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table by class
    tables = soup.find_all('table', {'class': 'wf-table-inset mod-overview'})

    players = []
    for table in tables:
        for row in table.find_all('a', href = True):
            players.append(row['href'])
    players = players[10:20]
    return players

def getTwitter(url):
    url = url

    response = requests.get(url)
    html = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    header = soup.find('div', {'class': 'player-header'})
    link = header.find('a', href = True)
    if 'twitter' in link['href']:
        return link.text
    else:
        return ''
    
