import json

import pandas as pd

from config import COUNTRY, LEAGUE_NAME

england = pd.read_csv(f'../{LEAGUE_NAME}_v1.4.csv')


with open(f"../data/{COUNTRY}/stadiums.json") as f:
    stadiums = json.load(f)


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
        if stadium['name'] == row['home_team'] and row['year'] == stadium['season']:
            is_home += 1
            home_stadiums.append(stadium['stadium'])
            home_cities.append(stadium['city'])
            home_capacities.append(stadium['capacity'])
        if stadium['name'] == row['away_team'] and row['year'] == stadium['season']:
            is_away += 1
            away_cities.append(stadium['city'])

    if is_home != 1:
        print(row['home_team'])
        home_stadiums.append('-')
        home_cities.append('-')
        home_capacities.append('0')
    if is_away == 0:
        print(row['away_team'])
        away_cities.append('-')


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

england.to_csv(f'../{LEAGUE_NAME}_v1.5.csv', index=False)
