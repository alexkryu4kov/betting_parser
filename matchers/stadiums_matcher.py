from copy import deepcopy


matches = {
    'Watford': 'Watford FC',
    'Fulham': 'Fulham FC',
    'Arsenal': 'Arsenal FC',
    'Burnley': 'Burnley FC',
    'Blackpool': 'Blackpool FC',
    'Chelsea': 'Chelsea FC',
    'Southampton': 'Southampton FC',
    'Everton': 'Everton FC',
    'Brentford': 'Brentford FC',
    'Liverpool': 'Liverpool FC',
    'Sunderland': 'Sunderland AFC',
    'Barnsley': 'Barnsley FC',
    'Millwall': 'Millwall FC',
    'Middlesbrough': 'Middlesbrough FC',
    'Reading': 'Reading FC',
    'Gillingham': 'Gillingham FC',
    'Port Vale': 'Port Vale FC',
    'Morecambe': 'Morecambe FC',
    'Bury': 'Bury AFC',
    'Portsmouth': 'Portsmouth FC',
    'Walsall': 'Walsall FC',
    'Chesterfield': 'Chesterfield FC',
    'Rochdale': 'Rochdale AFC',
    'Stevenage': 'Stevenage FC',
    'Macclesfield': 'Macclesfield FC',
    'Barnet': 'Barnet FC',
    'Barrow': 'Barrow AFC',
}


class StadiumsMatcher:

    new_stadiums = []

    def match_stadiums(self, stadiums):

        for stadium in stadiums:
            if stadium.name not in matches:
                self.new_stadiums.append(stadium)
            else:
                new_stadium = deepcopy(stadium)
                new_stadium.name = matches[stadium.name]
                self.new_stadiums.append(new_stadium)

    def check_stadiums_match(self, teams):
        for team in teams:
            if team not in [stadium.name for stadium in self.new_stadiums]:
                print(team)
