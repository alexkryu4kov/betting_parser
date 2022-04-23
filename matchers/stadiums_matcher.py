import json
import pandas as pd
from copy import deepcopy


with open("../stadiums4.json") as f:
    stadiums3 = json.load(f)

england = pd.read_csv('../england-league-two_v1.3.csv')

new_stadiums = []

homes_team = set(list(england['home_team']))
stadiums_team = set(s['name'] for s in stadiums3)

matches = {
    'Watford': 'Watford FC',
    'Fulham': 'Fulham FC',
    'Arsenal': 'Arsenal FC',
    'Burnley': 'Burnley FC',
    'Blackpool': 'Blackpool FC',
    'Chelsea': 'Chelsea FC',
    'Southampton': 'Southampton FC',
    'Everton': 'Everton FC',
    'Brentford': 'Brentford FC',
    'Liverpool': 'Liverpool FC',
    'Sunderland': 'Sunderland AFC',
    'Barnsley': 'Barnsley FC',
    'Millwall': 'Millwall FC',
    'Middlesbrough': 'Middlesbrough FC',
    'Reading': 'Reading FC',
    'Gillingham': 'Gillingham FC',
    'Port Vale': 'Port Vale FC',
    'Morecambe': 'Morecambe FC',
    'Bury': 'Bury AFC',
    'Portsmouth': 'Portsmouth FC',
    'Walsall': 'Walsall FC',
    'Chesterfield': 'Chesterfield FC',
    'Rochdale': 'Rochdale AFC',
    'Stevenage': 'Stevenage FC',
    'Macclesfield': 'Macclesfield FC',
    'Barnet': 'Barnet FC',
    'Barrow': 'Barrow AFC',
}


for stadium in stadiums3:
    if stadium['name'] not in matches:
        new_stadiums.append(stadium)
    else:
        new_stadium = deepcopy(stadium)
        new_stadium['name'] = matches[stadium['name']]
        new_stadiums.append(new_stadium)

for home_team in homes_team:
    if home_team not in [stadium['name'] for stadium in new_stadiums]:
        print(home_team)

with open('../new_stadiums4.json', 'w') as f:
    json.dump(new_stadiums, f)
