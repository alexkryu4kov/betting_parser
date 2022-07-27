import json

from pipeline.steps.abstract_step import AbstractStep


with open("../../data/world/stadiums.json") as f:
    stadiums = json.load(f)


class AddStadiumsStep(AbstractStep):

    def run(self, dataset):
        home_stadiums = []
        home_cities = []
        away_cities = []
        is_derbys = []
        home_capacities = []

        print(len(dataset['home_team']))
        for index, row in dataset.iterrows():
            is_home = 0
            is_away = 0
            try:
                local_stadiums = stadiums[row['country']]
            except KeyError:
                print(f"Нет данных для {row['country']}")
                home_stadiums.append('-')
                home_cities.append('-')
                home_capacities.append('0')
                away_cities.append('-')
                continue
            for stadium in local_stadiums:
                if stadium['name'] == row['home_team'] and row['year'] == stadium['season']:
                    is_home += 1
                    home_stadiums.append(stadium['stadium'])
                    home_cities.append(stadium['city'])
                    home_capacities.append(stadium['capacity'])
                if stadium['name'] == row['away_team'] and row['year'] == stadium['season']:
                    is_away += 1
                    away_cities.append(stadium['city'])

            if is_home != 1:
                print(row['home_team'])
                home_stadiums.append('-')
                home_cities.append('-')
                home_capacities.append('0')
            if is_away == 0:
                print(row['away_team'])
                away_cities.append('-')

        print(len(home_cities))
        print(len(away_cities))
        for i, city in enumerate(home_cities):
            if city == away_cities[i] and away_cities[i] != '-':
                is_derbys.append(1)
            else:
                is_derbys.append(0)
        dataset['home_stadium'] = home_stadiums
        dataset['home_stadium_capacity'] = home_capacities
        dataset['home_city'] = home_cities
        dataset['away_city'] = away_cities
        dataset['is_derby'] = is_derbys

        return dataset
