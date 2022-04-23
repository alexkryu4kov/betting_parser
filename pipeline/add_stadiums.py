import json

import pandas as pd

england = pd.read_csv('../england-league-two_v1.3.csv')


with open("../new_stadiums4.json") as f:
    stadiums = json.load(f)

with open("../new_stadiums3.json") as f:
    stadiums3 = json.load(f)

league_matcher = {
    'premier-league-2016-2017': 2016,
    'premier-league-2017-2018': 2017,
    'premier-league-2018-2019': 2018,
    'premier-league-2019-2020': 2019,
    'premier-league-2020-2021': 2020,
    'premier-league': 2021,
    'championship-2016-2017': 2016,
    'championship-2017-2018': 2017,
    'championship-2018-2019': 2018,
    'championship-2019-2020': 2019,
    'championship-2020-2021': 2020,
    'championship': 2021,
    'league-one-2016-2017': 2016,
    'league-one-2017-2018': 2017,
    'league-one-2018-2019': 2018,
    'league-one-2019-2020': 2019,
    'league-one-2020-2021': 2020,
    'league-one': 2021,
    'league-two-2016-2017': 2016,
    'league-two-2017-2018': 2017,
    'league-two-2018-2019': 2018,
    'league-two-2019-2020': 2019,
    'league-two-2020-2021': 2020,
    'league-two': 2021,
}

home_stadiums = []
home_cities = []
away_cities = []
is_derbys = []
home_capacities = []
print(len(england['home_team']))
for index, row in england.iterrows():
    is_home = 0
    is_away = 0

    for stadium in stadiums:
        if stadium['name'] == row['home_team'] and league_matcher[row['league']] == stadium['season']:
            is_home += 1
            home_stadiums.append(stadium['stadium'])
            home_cities.append(stadium['city'])
            home_capacities.append(stadium['capacity'])

    for stadium in stadiums:
        if stadium['name'] == row['away_team'] and league_matcher[row['league']] == stadium['season']:
            is_away += 1
            away_cities.append(stadium['city'])

    if row['home_team'] == 'Macclesfield FC' and is_home == 0:
        is_home += 1
        home_stadiums.append('-')
        home_cities.append('-')
        home_capacities.append('0')
    if row['away_team'] == 'Macclesfield FC' and is_away == 0:
        is_away += 1
        away_cities.append('-')

    if is_home != 1:
        print(row['home_team'])
        print(league_matcher[row['league']])
    if is_away != 1:
        print(row['away_team'])

print(len(home_cities))
print(len(away_cities))
for i, city in enumerate(home_cities):
    if city == away_cities[i]:
        is_derbys.append(1)
    else:
        is_derbys.append(0)
england['home_stadium'] = home_stadiums
england['home_stadium_capacity'] = home_capacities
england['home_city'] = home_cities
england['away_city'] = away_cities
england['is_derby'] = is_derbys

england.to_csv('england-league-two_v1.4.csv', index=False)
