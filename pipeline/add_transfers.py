import json

import pandas as pd

from matchers.league_matcher import league_matcher

england = pd.read_csv('../england-league-two_v1.5.csv')


with open("../data/transfers.json") as f:
    teams = json.load(f)



def extract_market_value(market_value):
    if 'bn' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000_000
    if 'm' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000
    elif 'Th' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000
    else:
        return 0.0


home_winter_departures_age = []
home_winter_departures_sum = []
home_winter_departures_market_value = []
home_winter_arrivals_age = []
home_winter_arrivals_sum = []
home_winter_arrivals_market_value = []
home_summer_departures_age = []
home_summer_departures_sum = []
home_summer_departures_market_value = []
home_summer_arrivals_age = []
home_summer_arrivals_sum = []
home_summer_arrivals_market_value = []
away_winter_departures_age = []
away_winter_departures_sum = []
away_winter_departures_market_value = []
away_winter_arrivals_age = []
away_winter_arrivals_sum = []
away_winter_arrivals_market_value = []
away_summer_departures_age = []
away_summer_departures_sum = []
away_summer_departures_market_value = []
away_summer_arrivals_age = []
away_summer_arrivals_sum = []
away_summer_arrivals_market_value = []


for index, row in england.iterrows():
    is_home = 0
    if row['home_team'] in ['Bury AFC', 'Macclesfield FC']:
        is_home += 1
        home_winter_departures_age.append('0')
        home_winter_departures_sum.append('0')
        home_winter_departures_market_value.append('0')
        home_winter_arrivals_age.append('0')
        home_winter_arrivals_sum.append('0')
        home_winter_arrivals_market_value.append('0')
        home_summer_departures_age.append('0')
        home_summer_departures_sum.append('0')
        home_summer_departures_market_value.append('0')
        home_summer_arrivals_age.append('0')
        home_summer_arrivals_sum.append('0')
        home_summer_arrivals_market_value.append('0')
    if row['away_team'] in ['Bury AFC', 'Macclesfield FC']:
        away_winter_departures_age.append('0')
        away_winter_departures_sum.append('0')
        away_winter_departures_market_value.append('0')
        away_winter_arrivals_age.append('0')
        away_winter_arrivals_sum.append('0')
        away_winter_arrivals_market_value.append('0')
        away_summer_departures_age.append('0')
        away_summer_departures_sum.append('0')
        away_summer_departures_market_value.append('0')
        away_summer_arrivals_age.append('0')
        away_summer_arrivals_sum.append('0')
        away_summer_arrivals_market_value.append('0')
    for team in teams:
        if 1 < row['month'] < 9:
            if team['name'] == row['home_team']:
                if (league_matcher[row['league']] - 1) == team['season'] and team['part_of_year'] == 'summer':
                    is_home += 1
                    home_summer_departures_age.append(team['departures_age'])
                    home_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                    home_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    home_summer_arrivals_age.append(team['arrivals_age'])
                    home_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    home_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                if league_matcher[row['league']] == team['season'] and team['part_of_year'] == 'winter':
                    is_home += 1
                    home_winter_departures_age.append(team['departures_age'])
                    home_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                    home_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    home_winter_arrivals_age.append(team['arrivals_age'])
                    home_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    home_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
            if team['name'] == row['away_team']:
                if (league_matcher[row['league']] - 1) == team['season']and team['part_of_year'] == 'summer':
                    away_summer_departures_age.append(team['departures_age'])
                    away_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                    away_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    away_summer_arrivals_age.append(team['arrivals_age'])
                    away_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    away_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                if league_matcher[row['league']] == team['season'] and team['part_of_year'] == 'winter':
                    away_winter_departures_age.append(team['departures_age'])
                    away_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                    away_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    away_winter_arrivals_age.append(team['arrivals_age'])
                    away_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    away_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
        elif row['month'] == 1:
            if team['name'] == row['home_team']:
                if (league_matcher[row['league']] - 1) == team['season'] and team['part_of_year'] == 'summer':
                    is_home += 1
                    home_summer_departures_age.append(team['departures_age'])
                    home_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                    home_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    home_summer_arrivals_age.append(team['arrivals_age'])
                    home_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    home_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                if (league_matcher[row['league']] - 1) == team['season'] and team['part_of_year'] == 'winter':
                    is_home += 1
                    home_winter_departures_age.append(team['departures_age'])
                    home_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                    home_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    home_winter_arrivals_age.append(team['arrivals_age'])
                    home_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    home_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
            if team['name'] == row['away_team']:
                if (league_matcher[row['league']] - 1) == team['season'] and team['part_of_year'] == 'summer':
                    away_summer_departures_age.append(team['departures_age'])
                    away_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                    away_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    away_summer_arrivals_age.append(team['arrivals_age'])
                    away_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    away_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                if (league_matcher[row['league']] - 1) == team['season'] and team['part_of_year'] == 'winter':
                    away_winter_departures_age.append(team['departures_age'])
                    away_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                    away_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    away_winter_arrivals_age.append(team['arrivals_age'])
                    away_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    away_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
        else:
            if team['name'] == row['home_team']:
                if league_matcher[row['league']] == team['season'] and team['part_of_year'] == 'summer':
                    is_home += 1
                    home_summer_departures_age.append(team['departures_age'])
                    home_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                    home_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    home_summer_arrivals_age.append(team['arrivals_age'])
                    home_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    home_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                if league_matcher[row['league']] == team['season'] and team['part_of_year'] == 'winter':
                    is_home += 1
                    home_winter_departures_age.append(team['departures_age'])
                    home_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                    home_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    home_winter_arrivals_age.append(team['arrivals_age'])
                    home_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    home_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
            if team['name'] == row['away_team']:
                if league_matcher[row['league']] == team['season'] and team['part_of_year'] == 'summer':
                    away_summer_departures_age.append(team['departures_age'])
                    away_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                    away_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    away_summer_arrivals_age.append(team['arrivals_age'])
                    away_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    away_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                if league_matcher[row['league']] == team['season'] and team['part_of_year'] == 'winter':
                    away_winter_departures_age.append(team['departures_age'])
                    away_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                    away_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                    away_winter_arrivals_age.append(team['arrivals_age'])
                    away_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                    away_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
    if is_home == 0:
        print(row['home_team'])
        print(row['league'])
        print(league_matcher[row['league']])
        print(row['month'])

england['home_last_winter_window_departures_average_age'] = home_winter_departures_age
england['home_last_winter_window_departures_sum'] = home_winter_departures_sum
england['home_last_winter_window_departures_total_market_value'] = home_winter_departures_market_value
england['home_last_winter_window_arrivals_average_age'] = home_winter_arrivals_age
england['home_last_winter_window_arrivals_sum'] = home_winter_arrivals_sum
england['home_last_winter_window_arrivals_total_market_value'] = home_winter_arrivals_market_value
england['home_last_summer_window_departures_average_age'] = home_summer_departures_age
england['home_last_summer_window_departures_sum'] = home_summer_departures_sum
england['home_last_summer_window_departures_total_market_value'] = home_summer_departures_market_value
england['home_last_summer_window_arrivals_average_age'] = home_summer_arrivals_age
england['home_last_summer_window_arrivals_sum'] = home_summer_arrivals_sum
england['home_last_summer_window_arrivals_total_market_value'] = home_summer_arrivals_market_value
england['away_last_winter_window_departures_average_age'] = away_winter_departures_age
england['away_last_winter_window_departures_sum'] = away_winter_departures_sum
england['away_last_winter_window_departures_total_market_value'] = away_winter_departures_market_value
england['away_last_winter_window_arrivals_average_age'] = away_winter_arrivals_age
england['away_last_winter_window_arrivals_sum'] = away_winter_arrivals_sum
england['away_last_winter_window_arrivals_total_market_value'] = away_winter_arrivals_market_value
england['away_last_summer_window_departures_average_age'] = away_summer_departures_age
england['away_last_summer_window_departures_sum'] = away_summer_departures_sum
england['away_last_summer_window_departures_total_market_value'] = away_summer_departures_market_value
england['away_last_summer_window_arrivals_average_age'] = away_summer_arrivals_age
england['away_last_summer_window_arrivals_sum'] = away_summer_arrivals_sum
england['away_last_summer_window_arrivals_total_market_value'] = away_summer_arrivals_market_value

england.to_csv('england-league-two_v1.6.csv', index=False)
