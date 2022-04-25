import json

import pandas as pd

from config import COUNTRY, LEAGUE_NAME
from matchers.stadiums_matcher import StadiumsMatcher
from matchers.team_matcher import TeamsMatcher

with open(f'../data/{COUNTRY}/managers.json', 'r') as f:
    managers = json.load(f)

with open(f'../data/{COUNTRY}/stadiums.json', 'r') as f:
    stadiums = json.load(f)


england = pd.read_csv(f'../{LEAGUE_NAME}.csv')


teams_matcher = TeamsMatcher(england)
teams_matcher.match_teams()
print('Teams: \n')
teams_matcher.check_teams_match(list(set(manager['team'] for manager in managers)))


stadiums_matcher = StadiumsMatcher()
stadiums_matcher.clear_stadiums(stadiums)
stadiums_matcher.match_stadiums()
print('Stadiums: \n')
stadiums_matcher.check_stadiums_match(teams_matcher.teams)

teams_matcher.dataset.to_csv(f'../{LEAGUE_NAME}_v1.1.csv', index=False)

with open(f'../data/{COUNTRY}/stadiums.json', 'w') as f:
    json.dump([stadium for stadium in stadiums_matcher.matched_stadiums], f)
