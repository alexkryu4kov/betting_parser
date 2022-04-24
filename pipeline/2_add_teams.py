import json

import pandas as pd

from config import LEAGUE_NAME
from utils import extract_market_value

england = pd.read_csv(f'../{LEAGUE_NAME}_v1.2.csv')

with open("../data/teams.json") as f:
    teams = json.load(f)


home_squads = []
away_squads = []
home_ages = []
away_ages = []
home_foreigners = []
away_foreigners = []
home_e_markets = []
away_e_markets = []
home_total_markets = []
away_total_markets = []
for index, row in england.iterrows():
    is_home = 0
    is_away = 0

    for team in teams:
        if team['name'] == row['home_team'] and row['year'] == team['season']:
            is_home += 1
            home_squads.append(team['squad'])
            home_ages.append(team['age'])
            home_foreigners.append(team['foreigners'])
            home_e_markets.append(extract_market_value(team['e_market']))
            home_total_markets.append(extract_market_value(team['total_market']))
        elif team['name'] == row['away_team'] and row['year'] == team['season']:
            is_away += 1
            away_squads.append(team['squad'])
            away_ages.append(team['age'])
            away_foreigners.append(team['foreigners'])
            away_e_markets.append(extract_market_value(team['e_market']))
            away_total_markets.append(extract_market_value(team['total_market']))
    if is_home == 0:
        print(row['home_team'])
        home_squads.append(0)
        home_ages.append(0)
        home_foreigners.append(0)
        home_e_markets.append(0)
        home_total_markets.append(0)
    if is_away == 0:
        print(row['away_team'])
        away_squads.append(0)
        away_ages.append(0)
        away_foreigners.append(0)
        away_e_markets.append(0)
        away_total_markets.append(0)

print(len(home_squads))
print(len(away_squads))
england['home_squad_size'] = home_squads
england['home_average_age'] = home_ages
england['home_amount_of_foreigners'] = home_foreigners
england['home_e_market_value'] = home_e_markets
england['home_total_market_value'] = home_total_markets
england['away_squad_size'] = away_squads
england['away_average_age'] = away_ages
england['away_amount_of_foreigners'] = away_foreigners
england['away_e_market_value'] = away_e_markets
england['away_total_market_value'] = away_total_markets

england.to_csv(f'../{LEAGUE_NAME}_v1.3.csv', index=False)
