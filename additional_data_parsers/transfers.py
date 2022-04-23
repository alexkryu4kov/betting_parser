import json
import requests
from dataclasses import dataclass, asdict

from bs4 import BeautifulSoup

indices = {
    'Manchester City': '281', 'Liverpool FC': '31', 'Chelsea FC': '631', 'Manchester United': '985',
    'Tottenham Hotspur': '148', 'Arsenal FC': '11', 'Leicester City': '1003', 'Everton FC': '29', 'Aston Villa': '405',
    'Wolverhampton Wanderers': '543', 'West Ham United': '379', 'Newcastle United': '762', 'Leeds United': '399',
    'Southampton FC': '180', 'Crystal Palace': '873', 'Brighton &amp; Hove Albion': '1237', 'Brentford FC': '1148',
    'Norwich City': '1123', 'Burnley FC': '1132', 'Watford FC': '1010', 'AFC Bournemouth': '989', 'Fulham FC': '931',
    'Sheffield United': '350', 'West Bromwich Albion': '984', 'Stoke City': '512', 'Nottingham Forest': '703',
    'Middlesbrough FC': '641', 'Blackburn Rovers': '164', 'Millwall FC': '1028', 'Queens Park Rangers': '1039',
    'Swansea City': '2288', 'Huddersfield Town': '1110', 'Reading FC': '1032', 'Birmingham City': '337',
    'Preston North End': '466', 'Bristol City': '698', 'Cardiff City': '603', 'Derby County': '22',
    'Barnsley FC': '349', 'Hull City': '3008', 'Luton Town': '1031', 'Coventry City': '990', 'Blackpool FC': '1181',
    'Peterborough United': '1072', 'Sheffield Wednesday': '1035', 'Sunderland AFC': '289', 'Ipswich Town': '677',
    'Wigan Athletic': '1071', 'Rotherham United': '1194', 'Charlton Athletic': '358', 'Milton Keynes Dons': '991',
    'Wycombe Wanderers': '2805', 'Portsmouth FC': '1020', 'Oxford United': '988', 'Lincoln City': '1198',
    'Doncaster Rovers': '2454', 'Burton Albion': '2963', 'Bolton Wanderers': '355', 'Gillingham FC': '2814',
    'Plymouth Argyle': '2262', 'Crewe Alexandra': '1042', 'Cheltenham Town': '3371', 'Fleetwood Town': '11177',
    'Shrewsbury Town': '3054', 'Morecambe FC': '3697', 'AFC Wimbledon': '3884', 'Accrington Stanley': '3688',
    'Cambridge United': '986', 'Salford City': '34888', 'Mansfield Town': '3820', 'Swindon Town': '352',
    'Bristol Rovers': '2455', 'Colchester United': '1060', 'Tranmere Rovers': '1074', 'Northampton Town': '1302',
    'Bradford City': '1027', 'Oldham Athletic': '1078', 'Rochdale AFC': '1088', 'Carlisle United': '1220',
    'Barrow AFC': '6168', 'Stevenage FC': '3684', 'Crawley Town': '3537', 'Port Vale FC': '1211',
    'Leyton Orient': '1150', 'Walsall FC': '899', 'Scunthorpe United': '2964', 'Forest Green Rovers': '3455',
    'Exeter City': '6699', 'Hartlepool United': '2577', 'Newport County': '3716', 'Harrogate Town': '12020',
    'Sutton United': '3052', 'Southend United': '2793', 'Chesterfield FC': '1219',
}

lower_indices = {
    'Yeovil Town': '972', 'Grimsby Town': '1034', 'Barnet FC': '2804', 'Notts County': '1045',
}


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
for k, v in lower_indices.items():
    for s in range(2015, 2022):
        for part_of_time in ['s', 'w']:
            link = url(id=lower_indices.get(k), season=s, part_of_season=part_of_time)
            page = requests.get(link, headers={'User-Agent': 'Custom'})
            print(link)
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
                    name=k,
                    part_of_year='summer' if part_of_time == 's' else 'winter',
                    departures_age=departures_age,
                    departures_sum=departures_sum,
                    departures_market_value=departures_value,
                    arrivals_age=arrivals_age,
                    arrivals_sum=arrivals_sum,
                    arrivals_market_value=arrivals_value,
                )
            )

with open('../transfers_lower.json', 'w') as f:
    json.dump([asdict(transfer) for transfer in transfers], f)
