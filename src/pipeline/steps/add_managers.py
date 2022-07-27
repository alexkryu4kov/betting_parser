import json
from datetime import datetime
from dataclasses import dataclass

from dateutil import parser

from pipeline.steps.abstract_step import AbstractStep


with open('../../data/world/managers.json', 'r') as f:
    managers = json.load(f)


@dataclass
class Manager:
    start_date: float
    days: int
    name: str
    birthday: float
    country: str


def extract_manager(country, team, current_date: datetime):
    try:
        local_managers = managers[country]
    except KeyError:
        print(f"Нет данных для {country}")
        return Manager(
            start_date=0.0,
            days=0,
            name='-',
            birthday=0.0,
            country='-',
        )
    for manager in local_managers:
        if team == manager['team']:
            start_date = parser.parse(manager['start'])
            if current_date >= start_date:
                return Manager(
                        start_date=start_date.timestamp(),
                        days=(current_date - start_date).days,
                        name=manager['name'],
                        birthday=parser.parse(manager['birthday']).timestamp() if manager['birthday'] != '-' else 0.0,
                        country=manager['country'],
                    )
    print(team)
    return Manager(
        start_date=0.0,
        days=0,
        name='-',
        birthday=0.0,
        country='-',
    )


class AddManagersStep(AbstractStep):

    @classmethod
    def run(cls, dataset):
        home_names = []
        away_names = []
        home_days = []
        away_days = []
        home_start_dates = []
        away_start_dates = []
        home_birthdays = []
        away_birthdays = []
        home_countries = []
        away_countries = []
        
        home_is_manager_and_league_same_country = []
        away_is_manager_and_league_same_country = []
        
        for index, row in dataset.iterrows():
            home_manager = extract_manager(row['country'], row['home_team'], parser.parse(row['date']))
            away_manager = extract_manager(row['country'], row['away_team'], parser.parse(row['date']))
            home_names.append(home_manager.name)
            away_names.append(away_manager.name)
            home_days.append(home_manager.days)
            away_days.append(away_manager.days)
            home_start_dates.append(home_manager.start_date)
            away_start_dates.append(away_manager.start_date)
            home_birthdays.append(home_manager.birthday)
            away_birthdays.append(away_manager.birthday)
            home_countries.append(home_manager.country)
            away_countries.append(away_manager.country)
        
            home_is_manager_and_league_same_country.append(int(row['country'].lower() == home_countries[index].lower()))
            away_is_manager_and_league_same_country.append(int(row['country'].lower() == away_countries[index].lower()))
        
        dataset['home_manager_working_days'] = home_days
        dataset['away_manager_working_days'] = away_days
        dataset['home_manager_name'] = home_names
        dataset['away_manager_name'] = away_names
        dataset['home_manager_start_date'] = home_start_dates
        dataset['home_manager_birthday'] = home_birthdays
        dataset['home_manager_country'] = home_countries
        dataset['away_manager_start_date'] = away_start_dates
        dataset['away_manager_birthday'] = away_birthdays
        dataset['away_manager_country'] = away_countries
        dataset['home_is_manager_and_league_same_country'] = home_is_manager_and_league_same_country
        dataset['away_is_manager_and_league_same_country'] = away_is_manager_and_league_same_country

        return dataset
