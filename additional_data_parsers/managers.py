import json
from dataclasses import dataclass, asdict
from dateutil import parser

import requests
from bs4 import BeautifulSoup

from config import COUNTRY

with open(f'../data/{COUNTRY}/indices.json', 'r') as f:
    indices = json.load(f)


def url(index):
    return f'https://www.transfermarkt.com/manchester-city/mitarbeiterhistorie/verein/{index}'


@dataclass
class ManagerInfo:
    team: str
    name: str
    birthday: str
    country: str
    start: str
    end: str


managers = []
for team, index in indices.items():
    print(team)
    page = requests.get(url(index), headers={'User-Agent': 'Custom'})

    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_='items')
    table2 = table.find('tbody')
    table3 = table2.find_all('tr')
    for row in table3:
        try:
            zentrierts = row.find_all(class_='zentriert')
            end = str(zentrierts[2]).split('">')[1].split('</')[0]
            if end != '-' and parser.parse(end).year < 2015:
                continue
            inline = row.find(class_='inline-table')
            name = str(inline).split("title=\"")[1].split("\"/><")[0]
            birthday = str(inline).split("</td></tr><tr><td>")[1].split("</td></tr>")[0]

            country = str(zentrierts[0]).split("title=\"")[1].split("\"/><")[0]
            start = str(zentrierts[1]).split('">')[1].split('</')[0]
            managers.append(
                ManagerInfo(
                    team=team,
                    name=name,
                    birthday=birthday,
                    country=country,
                    start=start,
                    end=end,
                )
            )
        except Exception:
            continue

with open(f'../data/{COUNTRY}/managers.json', 'w') as f:
    json.dump([asdict(manager) for manager in managers], f)
