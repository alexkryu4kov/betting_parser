import json
import difflib

from config import COUNTRY

from data.world.matches import matches

with open('../../data/world/managers.json', 'r') as f:
    managers = json.load(f)


class TeamsMatcher:

    def __init__(self, dataset):
        self.dataset = dataset
        self.teams = None

    def match_teams(self):
        for i, row in self.dataset.iterrows():
            try:
                local_matches = matches[row['country']]
            except KeyError:
                print(f"Нет данных для {row['country']}")
                continue
            if row['home_team'] in local_matches:
                self.dataset.at[i, 'home_team'] = local_matches.get(row['home_team'])
            if row['away_team'] in local_matches:
                self.dataset.at[i, 'away_team'] = local_matches.get(row['away_team'])
        return self.dataset

    def check_teams_match(self):

        for i, row in self.dataset.iterrows():
            home_team = row['home_team']
            away_team = row['away_team']
            try:
                managers[row['country']]
            except KeyError:
                print(row['country'])
                print(f"'{home_team}': ''")
                print(f"'{away_team}': ''")
                continue
            managers_teams = [manager['team'] for manager in managers[row['country']]]
            if home_team not in managers_teams:
                try:
                    print(
                        f"'{home_team}': '{','.join(difflib.get_close_matches(home_team, managers_teams))}',")
                except Exception:
                    print(f"'{home_team}': ''")
            if away_team not in managers_teams:
                try:
                    print(
                        f"'{away_team}': '{','.join(difflib.get_close_matches(away_team, managers_teams))}',")
                except Exception:
                    print(f"'{away_team}': ''")

