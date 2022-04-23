import json

import pandas as pd

england = pd.read_csv('../england-league-two_v1.4.csv')

with open("../teams_detailed.json") as f:
    teams = json.load(f)

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


def extract_market_value(market_value):
    if 'bn' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000_000
    if 'm' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000
    elif 'Th' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000
    else:
        print(market_value)
        return 0.0


def extract_age(age):
    if age == '-':
        return 0.0
    return age


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
home_is_manager_and_league_same_country = []
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
away_is_manager_and_league_same_country = []


for index, row in england.iterrows():
    home_is_manager_and_league_same_country.append(int(row['country'] == row['home_manager_country']))
    away_is_manager_and_league_same_country.append(int(row['country'] == row['away_manager_country']))
    if row['home_team'] in ['Bury AFC', 'Macclesfield FC']:
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
    if row['away_team'] in ['Bury AFC', 'Macclesfield FC']:
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
    is_home = 0
    for team in teams:
        if team['name'] == row['home_team'] and league_matcher[row['league']] == team['season']:
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
        elif team['name'] == row['away_team'] and league_matcher[row['league']] == team['season']:
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
england['home_is_manager_and_league_same_country'] = home_is_manager_and_league_same_country
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
england['away_is_manager_and_league_same_country'] = away_is_manager_and_league_same_country

england.to_csv('england-league-two_v1.5.csv', index=False)
