from copy import deepcopy

import difflib

from data.world.matches import stadium_matches


class StadiumsMatcher:

    new_stadiums = {}
    matched_stadiums = {}

    def __init__(self, dataset):
        self.dataset = dataset

    def clear_stadiums(self, stadiums):
        for country, stads in stadiums.items():
            country_stadiums = []
            for index, stadium in enumerate(stads):
                try:
                    if stadium['name'] == stads[index - 1]['name'] and stadium['season'] == stads[index - 1]['season']:
                        continue
                except IndexError:
                    country_stadiums.append(stadium)
                    continue
                country_stadiums.append(stadium)
            self.new_stadiums[country] = country_stadiums

    def match_stadiums(self):
        for country, stads in self.new_stadiums.items():
            try:
                local_stadiums = stadium_matches[country]
            except KeyError:
                print(f"Нет данных для {country}")
                continue
            country_stadiums = []
            for stadium in stads:
                if stadium['name'] not in local_stadiums:
                    country_stadiums.append(stadium)
                else:
                    new_stadium = deepcopy(stadium)
                    new_stadium['name'] = local_stadiums[stadium['name']]
                    country_stadiums.append(new_stadium)
            self.matched_stadiums[country] = country_stadiums
        print(self.matched_stadiums)

    def check_stadiums_match(self):

        for i, row in self.dataset.iterrows():
            home_team = row['home_team']
            away_team = row['away_team']
            try:
                stadium_matches[row['country']]
            except KeyError:
                print(row['country'])
                print(f"'': '{home_team}'")
                print(f"'': '{away_team}'")
                continue
            stadium_names = list(set([stadium['name'] for stadium in stadium_matches[row['country']]]))
            if home_team not in stadium_names:
                try:
                    print(f"'{','.join(difflib.get_close_matches(home_team, stadium_names))}': '{home_team}',")
                except Exception:
                    print(f"'': '{home_team}'")
            if away_team not in stadium_names:
                try:
                    print(f"'{','.join(difflib.get_close_matches(away_team, stadium_names))}': '{away_team}',")
                except Exception:
                    print(f"'': '{away_team}'")
