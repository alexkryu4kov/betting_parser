import json

import pandas as pd

from config import COUNTRY, LEAGUE_NAME
from utils import extract_age, extract_market_value

england = pd.read_csv(f'../{LEAGUE_NAME}_v1.5.csv')

with open(f"../data/{COUNTRY}/teams_detailed.json") as f:
    teams = json.load(f)


home_goalkeepers_average_age = []
home_defenders_average_age = []
home_midfields_average_age = []
home_attacks_average_age = []
home_goalkeepers_total_markets = []
home_defenders_total_markets = []
home_midfields_total_markets = []
home_attacks_total_markets = []
home_goalkeepers_e_markets = []
home_defenders_e_markets = []
home_midfields_e_markets = []
home_attacks_e_markets = []
away_goalkeepers_average_age = []
away_defenders_average_age = []
away_midfields_average_age = []
away_attacks_average_age = []
away_goalkeepers_total_markets = []
away_defenders_total_markets = []
away_midfields_total_markets = []
away_attacks_total_markets = []
away_goalkeepers_e_markets = []
away_defenders_e_markets = []
away_midfields_e_markets = []
away_attacks_e_markets = []


for index, row in england.iterrows():

    is_home = 0
    is_away = 0
    for team in teams:
        if team['name'] == row['home_team'] and row['year'] == team['season']:
            is_home += 1
            if team['position'] == 'Goalkeeper':
                home_goalkeepers_average_age.append(extract_age(team['age']))
                home_goalkeepers_total_markets.append(extract_market_value(team['total_market']))
                home_goalkeepers_e_markets.append(extract_market_value(team['e_market']))
            elif team['position'] == 'Defender':
                home_defenders_average_age.append(extract_age(team['age']))
                home_defenders_total_markets.append(extract_market_value(team['total_market']))
                home_defenders_e_markets.append(extract_market_value(team['e_market']))
            elif team['position'] == 'midfield':
                home_midfields_average_age.append(extract_age(team['age']))
                home_midfields_total_markets.append(extract_market_value(team['total_market']))
                home_midfields_e_markets.append(extract_market_value(team['e_market']))
            elif team['position'] == 'attack':
                home_attacks_average_age.append(extract_age(team['age']))
                home_attacks_total_markets.append(extract_market_value(team['total_market']))
                home_attacks_e_markets.append(extract_market_value(team['e_market']))
        elif team['name'] == row['away_team'] and row['year'] == team['season']:
            is_away += 1
            if team['position'] == 'Goalkeeper':
                away_goalkeepers_average_age.append(extract_age(team['age']))
                away_goalkeepers_total_markets.append(extract_market_value(team['total_market']))
                away_goalkeepers_e_markets.append(extract_market_value(team['e_market']))
            elif team['position'] == 'Defender':
                away_defenders_average_age.append(extract_age(team['age']))
                away_defenders_total_markets.append(extract_market_value(team['total_market']))
                away_defenders_e_markets.append(extract_market_value(team['e_market']))
            elif team['position'] == 'midfield':
                away_midfields_average_age.append(extract_age(team['age']))
                away_midfields_total_markets.append(extract_market_value(team['total_market']))
                away_midfields_e_markets.append(extract_market_value(team['e_market']))
            elif team['position'] == 'attack':
                away_attacks_average_age.append(extract_age(team['age']))
                away_attacks_total_markets.append(extract_market_value(team['total_market']))
                away_attacks_e_markets.append(extract_market_value(team['e_market']))
    if is_home == 0:
        print(row['home_team'])
        home_goalkeepers_average_age.append(0)
        home_goalkeepers_total_markets.append(0)
        home_goalkeepers_e_markets.append(0)
        home_defenders_average_age.append(0)
        home_defenders_total_markets.append(0)
        home_defenders_e_markets.append(0)
        home_midfields_average_age.append(0)
        home_midfields_total_markets.append(0)
        home_midfields_e_markets.append(0)
        home_attacks_average_age.append(0)
        home_attacks_total_markets.append(0)
        home_attacks_e_markets.append(0)
    if is_away == 0:
        print(row['away_team'])
        away_goalkeepers_average_age.append(0)
        away_goalkeepers_total_markets.append(0)
        away_goalkeepers_e_markets.append(0)
        away_defenders_average_age.append(0)
        away_defenders_total_markets.append(0)
        away_defenders_e_markets.append(0)
        away_midfields_average_age.append(0)
        away_midfields_total_markets.append(0)
        away_midfields_e_markets.append(0)
        away_attacks_average_age.append(0)
        away_attacks_total_markets.append(0)
        away_attacks_e_markets.append(0)


england['home_goalkeepers_average_age'] = home_goalkeepers_average_age
england['home_defenders_average_age'] = home_defenders_average_age
england['home_midfields_average_age'] = home_midfields_average_age
england['home_attacks_average_age'] = home_attacks_average_age
england['home_goalkeepers_total_market_value'] = home_goalkeepers_total_markets
england['home_defenders_total_market_value'] = home_defenders_total_markets
england['home_midfields_total_market_value'] = home_midfields_total_markets
england['home_attacks_total_market_value'] = home_attacks_total_markets
england['home_goalkeepers_e_market_value'] = home_goalkeepers_e_markets
england['home_defenders_e_market_value'] = home_defenders_e_markets
england['home_midfields_e_market_value'] = home_midfields_e_markets
england['home_attacks_e_market_value'] = home_attacks_e_markets
england['away_goalkeepers_average_age'] = away_goalkeepers_average_age
england['away_defenders_average_age'] = away_defenders_average_age
england['away_midfields_average_age'] = away_midfields_average_age
england['away_attacks_average_age'] = away_attacks_average_age
england['away_goalkeepers_total_market_value'] = away_goalkeepers_total_markets
england['away_defenders_total_market_value'] = away_defenders_total_markets
england['away_midfields_total_market_value'] = away_midfields_total_markets
england['away_attacks_total_market_value'] = away_attacks_total_markets
england['away_goalkeepers_e_market_value'] = away_goalkeepers_e_markets
england['away_defenders_e_market_value'] = away_defenders_e_markets
england['away_midfields_e_market_value'] = away_midfields_e_markets
england['away_attacks_e_market_value'] = away_attacks_e_markets

england.to_csv(f'../{LEAGUE_NAME}_v1.6.csv', index=False)
