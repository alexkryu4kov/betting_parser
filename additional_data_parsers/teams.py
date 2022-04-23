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
    'Sutton United': '3052',
}


def url(id):
    return f'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB4/plus/?saison_id={id}'


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
for id in range(2016, 2022):
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
        e_market = str(rechts[0]).split('rechts">')[1].split('</')[0]
        total_market = str(rechts[1]).split('">')[-1].split('</a')[0]
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

with open('../teams4.json', 'w') as f:
    json.dump([asdict(team) for team in teams], f)
