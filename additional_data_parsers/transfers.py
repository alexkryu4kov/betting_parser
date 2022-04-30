import json
from dataclasses import dataclass, asdict

import requests
from bs4 import BeautifulSoup

from config import COUNTRY


with open(f'../data/{COUNTRY}/indices.json', 'r') as f:
    indices = json.load(f)


def url(id, season, part_of_season):
    return f'https://www.transfermarkt.com/manchester-city/transfers/verein/{id}/plus/?saison_id={season}&pos=&detailpos=&w_s={part_of_season}'


@dataclass
class Info:
    name: str
    season: int
    part_of_year: str
    departures_age: str
    departures_sum: str
    departures_market_value: str
    arrivals_age: str
    arrivals_sum: str
    arrivals_market_value: str


transfers = []
for team, index in indices.items():
    for s in range(2015, 2022):
        for part_of_time in ['s', 'w']:
            link = url(id=indices.get(team), season=s, part_of_season=part_of_time)
            page = requests.get(link, headers={'User-Agent': 'Custom'})
            soup = BeautifulSoup(page.text, 'html.parser')
            departures_table = soup.find('div', {'id': 'yw2'}).find(class_='items')
            try:
                departures_table2 = departures_table.find('tfoot')
                departures_table3 = departures_table2.find_all('tr')
                departures_sum = str(departures_table3[0]).split('Sum: ')[1].split(' </td>')[0]
                departures_age = str(departures_table3[1]).split('age: ')[1].split(' </td>')[0]
                departures_value = str(departures_table3[2]).split('departures: ')[1].split(' </td>')[0]
            except AttributeError:
                departures_sum = '0'
                departures_age = '0'
                departures_value = '0'

            arrivals_table = soup.find('div', {'id': 'yw1'}).find(class_='items')
            try:
                arrivals_table2 = arrivals_table.find('tfoot')
                arrivals_table3 = arrivals_table2.find_all('tr')
                arrivals_sum = str(arrivals_table3[0]).split('Sum: ')[1].split(' </td>')[0]
                arrivals_age = str(arrivals_table3[1]).split('age: ')[1].split(' </td>')[0]
                arrivals_value = str(arrivals_table3[2]).split('arrivals: ')[1].split(' </td>')[0]
            except AttributeError:
                arrivals_sum = '0'
                arrivals_age = '0'
                arrivals_value = '0'

            transfers.append(
                Info(
                    season=s,
                    name=team,
                    part_of_year='summer' if part_of_time == 's' else 'winter',
                    departures_age=departures_age,
                    departures_sum=departures_sum,
                    departures_market_value=departures_value,
                    arrivals_age=arrivals_age,
                    arrivals_sum=arrivals_sum,
                    arrivals_market_value=arrivals_value,
                )
            )
        print(f'{team} {s} Done!')

with open(f'../data/{COUNTRY}/transfers.json', 'w') as f:
    json.dump([asdict(transfer) for transfer in transfers], f)
