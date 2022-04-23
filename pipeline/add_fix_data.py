import pandas as pd
from dateutil import parser

england = pd.read_csv('../england-league-two_v1.6.csv')

levels = {
    'premier-league': 1,
    'championship': 2,
    'league-one': 3,
    'league-two': 4,
}

seasons_matcher = {
    'premier-league-2016-2017': '2016-2017',
    'premier-league-2017-2018': '2017-2018',
    'premier-league-2018-2019': '2018-2019',
    'premier-league-2019-2020': '2019-2020',
    'premier-league-2020-2021': '2020-2021',
    'premier-league': '2021-2022',
    'championship-2016-2017': '2016-2017',
    'championship-2017-2018': '2017-2018',
    'championship-2018-2019': '2018-2019',
    'championship-2019-2020': '2019-2020',
    'championship-2020-2021': '2020-2021',
    'championship': '2021-2022',
    'league-one-2016-2017': '2016-2017',
    'league-one-2017-2018': '2017-2018',
    'league-one-2018-2019': '2018-2019',
    'league-one-2019-2020': '2019-2020',
    'league-one-2020-2021': '2020-2021',
    'league-one': '2021-2022',
    'league-two-2016-2017': '2016-2017',
    'league-two-2017-2018': '2017-2018',
    'league-two-2018-2019': '2018-2019',
    'league-two-2019-2020': '2019-2020',
    'league-two-2020-2021': '2020-2021',
    'league-two': '2021-2022',
}

league_matcher = {
    'premier-league-2016-2017': 'premier-league',
    'premier-league-2017-2018': 'premier-league',
    'premier-league-2018-2019': 'premier-league',
    'premier-league-2019-2020': 'premier-league',
    'premier-league-2020-2021': 'premier-league',
    'premier-league': 'premier-league',
    'championship-2016-2017': 'championship',
    'championship-2017-2018': 'championship',
    'championship-2018-2019': 'championship',
    'championship-2019-2020': 'championship',
    'championship-2020-2021': 'championship',
    'championship': 'championship',
    'league-one-2016-2017': 'league-one',
    'league-one-2017-2018': 'league-one',
    'league-one-2018-2019': 'league-one',
    'league-one-2019-2020': 'league-one',
    'league-one-2020-2021': 'league-one',
    'league-one': 'league-one',
    'league-two-2016-2017': 'league-two',
    'league-two-2017-2018': 'league-two',
    'league-two-2018-2019': 'league-two',
    'league-two-2019-2020': 'league-two',
    'league-two-2020-2021': 'league-two',
    'league-two': 'league-two',
}

weekdays = []
league_levels = []
leagues = []
seasons = []
for i, row in england.iterrows():
    seasons.append(seasons_matcher.get(row['league']))
    league = league_matcher.get(row['league'])
    leagues.append(league)
    league_levels.append(levels.get(league))
    parsed_date = parser.parse(row['date'])
    weekdays.append(parsed_date.weekday())

england['league_level'] = league_levels
england['season'] = seasons
england['league'] = leagues
england['day_of_week'] = weekdays

england.to_csv('england-league-two_v1.7.csv', index=False)
