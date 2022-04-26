import json
import importlib
from dataclasses import dataclass, asdict

import requests
from bs4 import BeautifulSoup

from config import COUNTRY

leagues = importlib.import_module(f'data.{COUNTRY}.leagues')
matcher = leagues.stadiums_matcher


@dataclass
class StadiumInfo:
    season: int
    name: str
    stadium: str
    city: str
    capacity: str


stadiums = []

for league in matcher:
    for k, v in league.items():
        page = requests.get(v, headers={'User-Agent': 'Custom'})

        soup = BeautifulSoup(page.text, 'html.parser')
        thick = soup.find_all(class_='thick')
        h4 = soup.find_all(class_='right')
        for i, team in enumerate(thick):
            team_name = str(team).split('/">')[1].split('</a')[0]
            stadium_name = str(h4[i]).split('/venue/">')[1].split('</a>')[0]
            dd = str(h4[i]).split('<dd>')
            city = dd[1].split('</')[0]
            capacity = dd[2].split('/dt>')[0].split('</dd>')[0]
            stadiums.append(
                StadiumInfo(
                    season=k,
                    name=team_name,
                    stadium=stadium_name,
                    city=city,
                    capacity=capacity
                )
            )

with open(f'../data/{COUNTRY}/stadiums.json', 'w') as f:
    json.dump([asdict(stadium) for stadium in stadiums], f)
