import pandas as pd

from config import LEAGUE_NAME

from pipeline.steps.add_detailed_teams import AddDetailedTeamsStep
from pipeline.steps.add_managers import AddManagersStep
from pipeline.steps.add_stadiums import AddStadiumsStep
from pipeline.steps.add_teams import AddTeamsStep
from pipeline.steps.add_transfers import AddTransfersStep
from pipeline.steps.fix_seasons_and_leagues import FixSeasonAndLeaguesStep
from pipeline.steps.matcher import MatcherStep


dataset = pd.read_csv(f'../../data/{LEAGUE_NAME}.csv')

dataset = MatcherStep().run(dataset)
dataset = FixSeasonAndLeaguesStep().run(dataset)
dataset = AddTeamsStep().run(dataset)
dataset = AddManagersStep().run(dataset)
dataset = AddStadiumsStep().run(dataset)
dataset = AddDetailedTeamsStep().run(dataset)
dataset = AddTransfersStep().run(dataset)

dataset.to_csv(f'../../data/{LEAGUE_NAME}_final.csv', index=False)
