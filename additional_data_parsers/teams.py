import json
from dataclasses import dataclass, asdict

import requests
from bs4 import BeautifulSoup


def url(id):
    return f'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/NLN6/plus/?saison_id={id}'


@dataclass
class Info:
    name: str
    season: int
    age: str
    squad: str
    foreigners: str
    e_market: str
    total_market: str


teams = []
for id in range(2021, 2022):
    page = requests.get(url(id), headers={'User-Agent': 'Custom'})

    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_='items')
    table2 = table.find('tbody')
    table3 = table2.find_all('tr')
    for row in table3:
        zentrierts = row.find_all(class_='zentriert')
        rechts = row.find_all(class_='rechts')
        team = str(zentrierts[0]).split('title="')[1].split('">')[0]
        squad = str(zentrierts[1]).split('">')[-1].split('</a')[0]
        age = str(zentrierts[2]).split('zentriert">')[1].split('</')[0]
        foreigners = str(zentrierts[3]).split('zentriert">')[1].split('</')[0]
        try:
            e_market = str(rechts[0]).split('rechts">')[1].split('</')[0]
        except IndexError:
            e_market = 0.0
        try:
            total_market = str(rechts[1]).split('">')[-1].split('</a')[0]
        except IndexError:
            total_market = 0.0
        teams.append(
            Info(
                season=id,
                name=team,
                age=age,
                squad=squad,
                foreigners=foreigners,
                e_market=e_market,
                total_market=total_market,
            )
        )

with open('../data/teams.json', 'r') as f:
    teams_data = json.load(f)
    teams_data.extend([asdict(team) for team in teams])

with open('../data/teams.json', 'w') as f:
    json.dump([asdict(team) for team in teams], f)
