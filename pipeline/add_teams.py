import json

import pandas as pd

from matchers.league_matcher import league_matcher

england = pd.read_csv('../england-league-two_v1.1.csv')

with open("../teams4.json") as f:
    teams = json.load(f)


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


seasons = []
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
    is_away = 0
    seasons.append(league_matcher[row['league']])
    if row['home_team'] in ['Bury AFC', 'Macclesfield FC']:
        home_squads.append(0)
        home_ages.append(0)
        home_foreigners.append(0)
        home_e_markets.append(0)
        home_total_markets.append(0)
    if row['away_team'] in ['Bury AFC', 'Macclesfield FC']:
        is_away += 1
        away_squads.append(0)
        away_ages.append(0)
        away_foreigners.append(0)
        away_e_markets.append(0)
        away_total_markets.append(0)
    for team in teams:
        if team['name'] == row['home_team'] and league_matcher[row['league']] == team['season']:
            home_squads.append(team['squad'])
            home_ages.append(team['age'])
            home_foreigners.append(team['foreigners'])
            home_e_markets.append(extract_market_value(team['e_market']))
            home_total_markets.append(extract_market_value(team['total_market']))
        elif team['name'] == row['away_team'] and league_matcher[row['league']] == team['season']:
            is_away += 1
            away_squads.append(team['squad'])
            away_ages.append(team['age'])
            away_foreigners.append(team['foreigners'])
            away_e_markets.append(extract_market_value(team['e_market']))
            away_total_markets.append(extract_market_value(team['total_market']))
    if is_away == 0:
        print(row['away_team'])

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
england['season'] = seasons

england.to_csv('england-league-two_v1.2.csv', index=False)
