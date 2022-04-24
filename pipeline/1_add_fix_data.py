import pandas as pd
from dateutil import parser

from matchers.league_matcher import league_levels, league_matcher
from config import LEAGUE_NAME

england = pd.read_csv(f'../{LEAGUE_NAME}_v1.1.csv')


def create_season(season):
    return f'{season}-{season+1}'


weekdays = []
levels = []
leagues = []
seasons = []
months = []
for i, row in england.iterrows():
    season = create_season(league_matcher.get(row['league']))
    seasons.append(season)
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

england.to_csv(f'../{LEAGUE_NAME}_v1.2.csv', index=False)