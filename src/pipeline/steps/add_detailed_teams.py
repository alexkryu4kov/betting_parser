import json

from pipeline.steps.abstract_step import AbstractStep
from pipeline.utils import extract_age, extract_market_value

with open("../../data/world/teams_detailed.json") as f:
    teams = json.load(f)


class AddDetailedTeamsStep(AbstractStep):

    @classmethod
    def run(cls, dataset):
        home_goalkeepers_average_age = []
        home_defenders_average_age = []
        home_midfields_average_age = []
        home_attacks_average_age = []
        home_goalkeepers_total_markets = []
        home_defenders_total_markets = []
        home_midfields_total_markets = []
        home_attacks_total_markets = []
        home_goalkeepers_e_markets = []
        home_defenders_e_markets = []
        home_midfields_e_markets = []
        home_attacks_e_markets = []
        away_goalkeepers_average_age = []
        away_defenders_average_age = []
        away_midfields_average_age = []
        away_attacks_average_age = []
        away_goalkeepers_total_markets = []
        away_defenders_total_markets = []
        away_midfields_total_markets = []
        away_attacks_total_markets = []
        away_goalkeepers_e_markets = []
        away_defenders_e_markets = []
        away_midfields_e_markets = []
        away_attacks_e_markets = []
        
        for index, row in dataset.iterrows():
        
            is_home = 0
            is_away = 0
            try:
                local_teams = teams[row['country']]
            except KeyError:
                print(f"Нет данных для {row['country']}")
                home_goalkeepers_average_age.append(0)
                home_goalkeepers_total_markets.append(0)
                home_goalkeepers_e_markets.append(0)
                home_defenders_average_age.append(0)
                home_defenders_total_markets.append(0)
                home_defenders_e_markets.append(0)
                home_midfields_average_age.append(0)
                home_midfields_total_markets.append(0)
                home_midfields_e_markets.append(0)
                home_attacks_average_age.append(0)
                home_attacks_total_markets.append(0)
                home_attacks_e_markets.append(0)
                away_goalkeepers_average_age.append(0)
                away_goalkeepers_total_markets.append(0)
                away_goalkeepers_e_markets.append(0)
                away_defenders_average_age.append(0)
                away_defenders_total_markets.append(0)
                away_defenders_e_markets.append(0)
                away_midfields_average_age.append(0)
                away_midfields_total_markets.append(0)
                away_midfields_e_markets.append(0)
                away_attacks_average_age.append(0)
                away_attacks_total_markets.append(0)
                away_attacks_e_markets.append(0)
                continue
            for team in local_teams:
                if team['name'] == row['home_team'] and row['year'] == team['season']:
                    is_home += 1
                    if team['position'] == 'Goalkeeper':
                        home_goalkeepers_average_age.append(extract_age(team['age']))
                        home_goalkeepers_total_markets.append(extract_market_value(team['total_market']))
                        home_goalkeepers_e_markets.append(extract_market_value(team['e_market']))
                    elif team['position'] == 'Defender':
                        home_defenders_average_age.append(extract_age(team['age']))
                        home_defenders_total_markets.append(extract_market_value(team['total_market']))
                        home_defenders_e_markets.append(extract_market_value(team['e_market']))
                    elif team['position'] == 'midfield':
                        home_midfields_average_age.append(extract_age(team['age']))
                        home_midfields_total_markets.append(extract_market_value(team['total_market']))
                        home_midfields_e_markets.append(extract_market_value(team['e_market']))
                    elif team['position'] == 'attack':
                        home_attacks_average_age.append(extract_age(team['age']))
                        home_attacks_total_markets.append(extract_market_value(team['total_market']))
                        home_attacks_e_markets.append(extract_market_value(team['e_market']))
                elif team['name'] == row['away_team'] and row['year'] == team['season']:
                    is_away += 1
                    if team['position'] == 'Goalkeeper':
                        away_goalkeepers_average_age.append(extract_age(team['age']))
                        away_goalkeepers_total_markets.append(extract_market_value(team['total_market']))
                        away_goalkeepers_e_markets.append(extract_market_value(team['e_market']))
                    elif team['position'] == 'Defender':
                        away_defenders_average_age.append(extract_age(team['age']))
                        away_defenders_total_markets.append(extract_market_value(team['total_market']))
                        away_defenders_e_markets.append(extract_market_value(team['e_market']))
                    elif team['position'] == 'midfield':
                        away_midfields_average_age.append(extract_age(team['age']))
                        away_midfields_total_markets.append(extract_market_value(team['total_market']))
                        away_midfields_e_markets.append(extract_market_value(team['e_market']))
                    elif team['position'] == 'attack':
                        away_attacks_average_age.append(extract_age(team['age']))
                        away_attacks_total_markets.append(extract_market_value(team['total_market']))
                        away_attacks_e_markets.append(extract_market_value(team['e_market']))
            if is_home == 0:
                print(row['home_team'])
                home_goalkeepers_average_age.append(0)
                home_goalkeepers_total_markets.append(0)
                home_goalkeepers_e_markets.append(0)
                home_defenders_average_age.append(0)
                home_defenders_total_markets.append(0)
                home_defenders_e_markets.append(0)
                home_midfields_average_age.append(0)
                home_midfields_total_markets.append(0)
                home_midfields_e_markets.append(0)
                home_attacks_average_age.append(0)
                home_attacks_total_markets.append(0)
                home_attacks_e_markets.append(0)
            if is_away == 0:
                print(row['away_team'])
                away_goalkeepers_average_age.append(0)
                away_goalkeepers_total_markets.append(0)
                away_goalkeepers_e_markets.append(0)
                away_defenders_average_age.append(0)
                away_defenders_total_markets.append(0)
                away_defenders_e_markets.append(0)
                away_midfields_average_age.append(0)
                away_midfields_total_markets.append(0)
                away_midfields_e_markets.append(0)
                away_attacks_average_age.append(0)
                away_attacks_total_markets.append(0)
                away_attacks_e_markets.append(0)

        dataset['home_goalkeepers_average_age'] = home_goalkeepers_average_age
        dataset['home_defenders_average_age'] = home_defenders_average_age
        dataset['home_midfields_average_age'] = home_midfields_average_age
        dataset['home_attacks_average_age'] = home_attacks_average_age
        dataset['home_goalkeepers_total_market_value'] = home_goalkeepers_total_markets
        dataset['home_defenders_total_market_value'] = home_defenders_total_markets
        dataset['home_midfields_total_market_value'] = home_midfields_total_markets
        dataset['home_attacks_total_market_value'] = home_attacks_total_markets
        dataset['home_goalkeepers_e_market_value'] = home_goalkeepers_e_markets
        dataset['home_defenders_e_market_value'] = home_defenders_e_markets
        dataset['home_midfields_e_market_value'] = home_midfields_e_markets
        dataset['home_attacks_e_market_value'] = home_attacks_e_markets
        dataset['away_goalkeepers_average_age'] = away_goalkeepers_average_age
        dataset['away_defenders_average_age'] = away_defenders_average_age
        dataset['away_midfields_average_age'] = away_midfields_average_age
        dataset['away_attacks_average_age'] = away_attacks_average_age
        dataset['away_goalkeepers_total_market_value'] = away_goalkeepers_total_markets
        dataset['away_defenders_total_market_value'] = away_defenders_total_markets
        dataset['away_midfields_total_market_value'] = away_midfields_total_markets
        dataset['away_attacks_total_market_value'] = away_attacks_total_markets
        dataset['away_goalkeepers_e_market_value'] = away_goalkeepers_e_markets
        dataset['away_defenders_e_market_value'] = away_defenders_e_markets
        dataset['away_midfields_e_market_value'] = away_midfields_e_markets
        dataset['away_attacks_e_market_value'] = away_attacks_e_markets

        return dataset
