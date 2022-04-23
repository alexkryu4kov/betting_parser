import json

import requests
from bs4 import BeautifulSoup

from data.leagues import leagues

indices = {}
for league in leagues:
    url = f'https://www.transfermarkt.com/national-league-north/startseite/wettbewerb/{league}'

    page = requests.get(url, headers={'User-Agent': 'Custom'})

    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_='items')
    table2 = table.find('tbody')
    table3 = table2.find_all('tr')
    for row in table3:
        try:
            zentriert = row.find(class_='zentriert')
            name = str(zentriert).split("title=\"")[1].split("\"><img")[0]
            index = str(zentriert).split("verein/")[1].split("/saison_id/")[0]
            indices.update({name: index})
        except Exception:
            continue

with open('data/indices.json', 'w') as f:
    json.dump(indices, f)
