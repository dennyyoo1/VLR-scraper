from match_page import getKDA, fetty
from matches import getMatches
from player_page import getPlayers, getTwitter

prefix = "https://www.vlr.gg"
postfix = "/?game=all&tab=overview"

def checked(old, new):
    for link in old:
        if link in new:
            continue
        else:
            return True
    return False



links = getMatches()
for idx, link in enumerate(links):
    links[idx] = prefix + link
print(links)


data = []
for link in links:
    data.append(getKDA(link))

fwd, back = fetty(data)
print(data)
print(fwd)
print(back)

playerLinks = []
for link in links:
    players = getPlayers(link)
    for idx, line in enumerate(players):
        players[idx] = prefix + line
    playerLinks.append(players)
print(playerLinks)
twitter = []
for match in playerLinks:
    for link in match:
        twitter.append(getTwitter(link))
print(twitter)
