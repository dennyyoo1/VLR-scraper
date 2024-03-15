from bs4 import BeautifulSoup
import requests

def fetty(data):
    forward = []
    reverse = []
    for player in data:
        if player[1] == 17:
            if player[2] == 38:
                forward.append(player)
        if player[1] == 38:
            if player[2] == 17:
                reverse.append(player)
    return forward, reverse

def getKDA(url):
    url = url

    response = requests.get(url)
    html = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table by class
    tables = soup.find_all('table', {'class': 'wf-table-inset mod-overview'})

    # Grab all data from table
    match = []
    for table in tables:
        game = []
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            data = [cell.text.strip().replace('\n', ' ').replace('\t', '') for cell in cells]
            game.append(data)
        match.append(game)
    series = []
    for game in match:
        new_game = []
        for player in game:
            new_player = []
            for stat in player:
                if "      " in stat:
                    new_player.extend(stat.split("      "))
                elif ' ' in stat:
                    new_player.extend(stat.split())
                elif stat == '':
                    continue
                elif stat == '/':
                    break
                else:
                    new_player.append(stat)
            new_game.append(new_player)
        new_game.pop(0)
        series.append(new_game)
    final = []
    #grabs overall values
    for game in series[2:4]:
        for player in game:
            # forfeit case
            if len(player) == 4:
                break
            # general case
            if len(player) == 40:
                player = [player[i] for i in [0, 8, 12]]
            # china game
            else:
                player = [player[i] for i in [0, 3, 5]]
            final.append(player)

    return final

