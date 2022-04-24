import json
from dataclasses import dataclass, asdict

import requests
from bs4 import BeautifulSoup


with open('../data/indices.json', 'r') as f:
    indices = json.load(f)

indices = {"Bury FC": "2413", "Macclesfield Town FC": "2436"}


def url(id, season):
    return f'https://www.transfermarkt.com/manchester-city/kader/verein/{id}/plus/0/galerie/0?saison_id={season}'


@dataclass
class Info:
    name: str
    position: str
    season: int
    age: str
    e_market: str
    total_market: str


teams = []
for k, v in indices.items():
    for s in range(2016, 2022):
        link = url(id=indices.get(k), season=s)
        page = requests.get(link, headers={'User-Agent': 'Custom'})
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find(class_='large-4 columns')
        table2 = table.find('tbody')
        table3 = str(table2).split('tr>')

        for row in table3:
            if 'hauptlink' in row:
                position = row.split('hauptlink">')[1].split('</td')[0]
                age = row.split('"zentriert">')[1].split('</td')[0]
                market = row.split('"rechts">')[1].split('</td')[0]
                e_market = row.split('"rechts">')[2].split('</td')[0]
                teams.append(
                    Info(
                        name=k,
                        season=s,
                        position=position,
                        age=age,
                        total_market=market,
                        e_market=e_market,
                    )
                )
        print(f'{k} {s} Done!')


with open('../data/teams_detailed.json', 'r') as f:
    teams_data = json.load(f)
    teams_data.extend([asdict(team) for team in teams])

with open('../data/teams_detailed.json', 'w') as f:
    json.dump(teams_data, f)
