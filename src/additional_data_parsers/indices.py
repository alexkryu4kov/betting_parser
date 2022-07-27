import json
import importlib

import requests
from bs4 import BeautifulSoup

from config import COUNTRY
leagues = importlib.import_module(f'data.{COUNTRY}.leagues')

leagues = leagues.leagues
indices = {}
for league in leagues:
    for id in range(2016, 2022):
        url = f'https://www.transfermarkt.com/national-league-north/startseite/wettbewerb/{league}/plus/?saison_id={id}'

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
                if name not in indices:
                    print(name)
                    indices.update({name: index})
            except Exception:
                continue

with open(f'../data/{COUNTRY}/indices.json', 'w') as f:
    json.dump(indices, f)
