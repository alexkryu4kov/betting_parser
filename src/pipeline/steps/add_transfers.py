import json

from pipeline.steps.abstract_step import AbstractStep
from pipeline.utils import extract_market_value


with open("../../data/world/transfers.json") as f:
    teams = json.load(f)


class AddTransfersStep(AbstractStep):
    
    def run(self, dataset):
        home_winter_departures_age = []
        home_winter_departures_sum = []
        home_winter_departures_market_value = []
        home_winter_arrivals_age = []
        home_winter_arrivals_sum = []
        home_winter_arrivals_market_value = []
        home_summer_departures_age = []
        home_summer_departures_sum = []
        home_summer_departures_market_value = []
        home_summer_arrivals_age = []
        home_summer_arrivals_sum = []
        home_summer_arrivals_market_value = []
        away_winter_departures_age = []
        away_winter_departures_sum = []
        away_winter_departures_market_value = []
        away_winter_arrivals_age = []
        away_winter_arrivals_sum = []
        away_winter_arrivals_market_value = []
        away_summer_departures_age = []
        away_summer_departures_sum = []
        away_summer_departures_market_value = []
        away_summer_arrivals_age = []
        away_summer_arrivals_sum = []
        away_summer_arrivals_market_value = []

        for index, row in dataset.iterrows():
            is_home_winter = 0
            is_home_summer = 0
            is_away_winter = 0
            is_away_summer = 0

            try:
                local_teams = teams[row['country']]
            except KeyError:
                print(f"Нет данных для {row['country']}")
                home_summer_departures_age.append('0')
                home_summer_departures_sum.append('0')
                home_summer_departures_market_value.append('0')
                home_summer_arrivals_age.append('0')
                home_summer_arrivals_sum.append('0')
                home_summer_arrivals_market_value.append('0')
                home_winter_departures_age.append('0')
                home_winter_departures_sum.append('0')
                home_winter_departures_market_value.append('0')
                home_winter_arrivals_age.append('0')
                home_winter_arrivals_sum.append('0')
                home_winter_arrivals_market_value.append('0')
                away_summer_departures_age.append('0')
                away_summer_departures_sum.append('0')
                away_summer_departures_market_value.append('0')
                away_summer_arrivals_age.append('0')
                away_summer_arrivals_sum.append('0')
                away_summer_arrivals_market_value.append('0')
                away_winter_departures_age.append('0')
                away_winter_departures_sum.append('0')
                away_winter_departures_market_value.append('0')
                away_winter_arrivals_age.append('0')
                away_winter_arrivals_sum.append('0')
                away_winter_arrivals_market_value.append('0')
                continue
        
            if 1 < row['month'] < 9:
                for team in local_teams:
                    if team['name'] == row['home_team']:
                        if (row['year'] - 1) == team['season'] and team['part_of_year'] == 'summer':
                            is_home_summer += 1
                            home_summer_departures_age.append(team['departures_age'])
                            home_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                            home_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            home_summer_arrivals_age.append(team['arrivals_age'])
                            home_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            home_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                        if row['year'] == team['season'] and team['part_of_year'] == 'winter':
                            is_home_winter += 1
                            home_winter_departures_age.append(team['departures_age'])
                            home_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                            home_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            home_winter_arrivals_age.append(team['arrivals_age'])
                            home_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            home_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                    if team['name'] == row['away_team']:
                        if (row['year'] - 1) == team['season'] and team['part_of_year'] == 'summer':
                            is_away_summer += 1
                            away_summer_departures_age.append(team['departures_age'])
                            away_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                            away_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            away_summer_arrivals_age.append(team['arrivals_age'])
                            away_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            away_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                        if row['year'] == team['season'] and team['part_of_year'] == 'winter':
                            is_away_winter += 1
                            away_winter_departures_age.append(team['departures_age'])
                            away_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                            away_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            away_winter_arrivals_age.append(team['arrivals_age'])
                            away_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            away_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
            elif row['month'] == 1:
                for team in local_teams:
                    if team['name'] == row['home_team']:
                        if (row['year'] - 1) == team['season'] and team['part_of_year'] == 'summer':
                            is_home_summer += 1
                            home_summer_departures_age.append(team['departures_age'])
                            home_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                            home_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            home_summer_arrivals_age.append(team['arrivals_age'])
                            home_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            home_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                        if (row['year'] - 1) == team['season'] and team['part_of_year'] == 'winter':
                            is_home_winter += 1
                            home_winter_departures_age.append(team['departures_age'])
                            home_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                            home_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            home_winter_arrivals_age.append(team['arrivals_age'])
                            home_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            home_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                    if team['name'] == row['away_team']:
                        if (row['year'] - 1) == team['season'] and team['part_of_year'] == 'summer':
                            is_away_summer += 1
                            away_summer_departures_age.append(team['departures_age'])
                            away_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                            away_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            away_summer_arrivals_age.append(team['arrivals_age'])
                            away_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            away_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                        if (row['year'] - 1) == team['season'] and team['part_of_year'] == 'winter':
                            is_away_winter += 1
                            away_winter_departures_age.append(team['departures_age'])
                            away_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                            away_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            away_winter_arrivals_age.append(team['arrivals_age'])
                            away_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            away_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
            else:
                for team in local_teams:
                    if team['name'] == row['home_team']:
                        if row['year'] == team['season'] and team['part_of_year'] == 'summer':
                            is_home_summer += 1
                            home_summer_departures_age.append(team['departures_age'])
                            home_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                            home_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            home_summer_arrivals_age.append(team['arrivals_age'])
                            home_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            home_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                        if row['year'] == team['season'] and team['part_of_year'] == 'winter':
                            is_home_winter += 1
                            home_winter_departures_age.append(team['departures_age'])
                            home_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                            home_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            home_winter_arrivals_age.append(team['arrivals_age'])
                            home_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            home_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                    if team['name'] == row['away_team']:
                        if row['year'] == team['season'] and team['part_of_year'] == 'summer':
                            is_away_summer += 1
                            away_summer_departures_age.append(team['departures_age'])
                            away_summer_departures_sum.append(extract_market_value(team['departures_sum']))
                            away_summer_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            away_summer_arrivals_age.append(team['arrivals_age'])
                            away_summer_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            away_summer_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
                        if row['year'] == team['season'] and team['part_of_year'] == 'winter':
                            is_away_winter += 1
                            away_winter_departures_age.append(team['departures_age'])
                            away_winter_departures_sum.append(extract_market_value(team['departures_sum']))
                            away_winter_departures_market_value.append(extract_market_value(team['departures_market_value']))
                            away_winter_arrivals_age.append(team['arrivals_age'])
                            away_winter_arrivals_sum.append(extract_market_value(team['arrivals_sum']))
                            away_winter_arrivals_market_value.append(extract_market_value(team['arrivals_market_value']))
            if is_home_summer == 0:
                print(row['home_team'])
                home_summer_departures_age.append('0')
                home_summer_departures_sum.append('0')
                home_summer_departures_market_value.append('0')
                home_summer_arrivals_age.append('0')
                home_summer_arrivals_sum.append('0')
                home_summer_arrivals_market_value.append('0')
            if is_home_winter == 0:
                print(row['home_team'])
                home_winter_departures_age.append('0')
                home_winter_departures_sum.append('0')
                home_winter_departures_market_value.append('0')
                home_winter_arrivals_age.append('0')
                home_winter_arrivals_sum.append('0')
                home_winter_arrivals_market_value.append('0')
            if is_away_summer == 0:
                print(row['away_team'])
                away_summer_departures_age.append('0')
                away_summer_departures_sum.append('0')
                away_summer_departures_market_value.append('0')
                away_summer_arrivals_age.append('0')
                away_summer_arrivals_sum.append('0')
                away_summer_arrivals_market_value.append('0')
            if is_away_winter == 0:
                print(row['away_team'])
                away_winter_departures_age.append('0')
                away_winter_departures_sum.append('0')
                away_winter_departures_market_value.append('0')
                away_winter_arrivals_age.append('0')
                away_winter_arrivals_sum.append('0')
                away_winter_arrivals_market_value.append('0')

        dataset['home_last_winter_window_departures_average_age'] = home_winter_departures_age
        dataset['home_last_winter_window_departures_sum'] = home_winter_departures_sum
        dataset['home_last_winter_window_departures_total_market_value'] = home_winter_departures_market_value
        dataset['home_last_winter_window_arrivals_average_age'] = home_winter_arrivals_age
        dataset['home_last_winter_window_arrivals_sum'] = home_winter_arrivals_sum
        dataset['home_last_winter_window_arrivals_total_market_value'] = home_winter_arrivals_market_value
        dataset['home_last_summer_window_departures_average_age'] = home_summer_departures_age
        dataset['home_last_summer_window_departures_sum'] = home_summer_departures_sum
        dataset['home_last_summer_window_departures_total_market_value'] = home_summer_departures_market_value
        dataset['home_last_summer_window_arrivals_average_age'] = home_summer_arrivals_age
        dataset['home_last_summer_window_arrivals_sum'] = home_summer_arrivals_sum
        dataset['home_last_summer_window_arrivals_total_market_value'] = home_summer_arrivals_market_value
        dataset['away_last_winter_window_departures_average_age'] = away_winter_departures_age
        dataset['away_last_winter_window_departures_sum'] = away_winter_departures_sum
        dataset['away_last_winter_window_departures_total_market_value'] = away_winter_departures_market_value
        dataset['away_last_winter_window_arrivals_average_age'] = away_winter_arrivals_age
        dataset['away_last_winter_window_arrivals_sum'] = away_winter_arrivals_sum
        dataset['away_last_winter_window_arrivals_total_market_value'] = away_winter_arrivals_market_value
        dataset['away_last_summer_window_departures_average_age'] = away_summer_departures_age
        dataset['away_last_summer_window_departures_sum'] = away_summer_departures_sum
        dataset['away_last_summer_window_departures_total_market_value'] = away_summer_departures_market_value
        dataset['away_last_summer_window_arrivals_average_age'] = away_summer_arrivals_age
        dataset['away_last_summer_window_arrivals_sum'] = away_summer_arrivals_sum
        dataset['away_last_summer_window_arrivals_total_market_value'] = away_summer_arrivals_market_value

        return dataset
