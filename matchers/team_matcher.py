import importlib

import difflib

from config import COUNTRY

matches = importlib.import_module(f'data.{COUNTRY}.matches')
matches = matches.matches


class TeamsMatcher:

    def __init__(self, dataset):
        self.dataset = dataset
        self.teams = None

    def match_teams(self):

        for i, row in self.dataset.iterrows():
            if row['home_team'] in matches:
                self.dataset.at[i, 'home_team'] = matches.get(row['home_team'])
            if row['away_team'] in matches:
                self.dataset.at[i, 'away_team'] = matches.get(row['away_team'])
        return self.dataset

    def check_teams_match(self, managers_teams):

        home_teams = list(set(self.dataset['home_team']))
        away_teams = list(set(self.dataset['away_team']))
        self.teams = list(set([*home_teams, *away_teams]))
        for team in self.teams:
            if team not in managers_teams:
                try:
                    print(f"'{team}': '{','.join(difflib.get_close_matches(team, managers_teams))}',")
                except Exception:
                    print(team)
