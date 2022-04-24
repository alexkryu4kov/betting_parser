from copy import deepcopy

from matchers.matches import stadium_matches


class StadiumsMatcher:

    new_stadiums = []
    matched_stadiums = []

    def clear_stadiums(self, stadiums):
        for index, stadium in enumerate(stadiums):
            try:
                if stadium['name'] == stadiums[index - 1]['name'] and stadium['season'] == stadiums[index - 1]['season']:
                    continue
            except IndexError:
                self.new_stadiums.append(stadium)
                continue
            self.new_stadiums.append(stadium)

    def match_stadiums(self):
        for stadium in self.new_stadiums:
            if stadium['name'] not in stadium_matches:
                self.matched_stadiums.append(stadium)
            else:
                new_stadium = deepcopy(stadium)
                new_stadium['name'] = stadium_matches[stadium['name']]
                self.matched_stadiums.append(new_stadium)

    def check_stadiums_match(self, teams):
        for team in teams:
            if team not in [stadium['name'] for stadium in self.matched_stadiums]:
                print(team)
