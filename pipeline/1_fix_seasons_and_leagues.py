import importlib

import pandas as pd
from dateutil import parser

from config import COUNTRY, LEAGUE_NAME

leagues = importlib.import_module(f'data.{COUNTRY}.leagues')
league_levels = leagues.league_levels
league_matcher = leagues.league_matcher
seasons_matcher = leagues.seasons_matcher

england = pd.read_csv(f'../{LEAGUE_NAME}_v1.1.csv')


def create_season(season):
    return f'{season}-{season+1}'


weekdays = []
levels = []
leagues = []
seasons = []
months = []
years = []
for i, row in england.iterrows():
    year = seasons_matcher.get(row['league'])
    season = create_season(year)
    seasons.append(season)
    years.append(year)
    league = league_matcher.get(row['league'])
    leagues.append(league)
    levels.append(league_levels.get(league))
    parsed_date = parser.parse(row['date'])
    weekdays.append(parsed_date.weekday())
    months.append(parsed_date.month)

england['league_level'] = levels
england['season'] = seasons
england['league'] = leagues
england['day_of_week'] = weekdays
england['month'] = months
england['year'] = years

england.to_csv(f'../{LEAGUE_NAME}_v1.2.csv', index=False)