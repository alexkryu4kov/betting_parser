import pandas as pd

from config import LEAGUE_NAME
from src.matchers.stadiums_matcher import StadiumsMatcher
from src.matchers.team_matcher import TeamsMatcher


england = pd.read_csv(f'../../data/{LEAGUE_NAME}.csv')


teams_matcher = TeamsMatcher(england)
print('Teams: \n')
teams_matcher.check_teams_match()


stadiums_matcher = StadiumsMatcher(england)
print('Stadiums: \n')
stadiums_matcher.check_stadiums_match()
