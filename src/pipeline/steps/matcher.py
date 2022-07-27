import json

from src.matchers.stadiums_matcher import StadiumsMatcher
from src.matchers.team_matcher import TeamsMatcher
from pipeline.steps.abstract_step import AbstractStep

with open('../../data/world/managers.json', 'r') as f:
    managers = json.load(f)

with open('../../data/world/stadiums.json', 'r') as f:
    stadiums = json.load(f)


class MatcherStep(AbstractStep):

    def run(self, dataset):

        teams_matcher = TeamsMatcher(dataset)
        teams_matcher.match_teams()
        print('Teams: \n')
        teams_matcher.check_teams_match()

        stadiums_matcher = StadiumsMatcher(dataset)
        stadiums_matcher.clear_stadiums(stadiums)
        stadiums_matcher.match_stadiums()
        print('Stadiums: \n')
        stadiums_matcher.check_stadiums_match()

        # with open(f'../../data/world/stadiums.json', 'w') as f:
        #    json.dump([stadium for stadium in stadiums_matcher.matched_stadiums], f)

        return teams_matcher.dataset
