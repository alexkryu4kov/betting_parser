import pandas as pd
from dateutil import parser
from datetime import datetime
from dataclasses import dataclass

managers = pd.read_csv('../data/managers.csv')
england = pd.read_csv('../all_england_v2.7.csv')


start = parser.parse(managers['Start'].iloc[0])
date = parser.parse(england['date'].iloc[0])


@dataclass
class Manager:
    start_date: float
    days: int
    name: str
    birthday: float
    country: start
    month: int


def extract_manager(home_team, current_date: datetime):
    if home_team in ['Bury AFC', 'Macclesfield FC']:
        return Manager(
            start_date=0.0,
            days=0,
            name='-',
            birthday=0.0,
            country='-',
            month=current_date.month,
        )
    is_manager = 0
    for i, row in managers[managers['Team'] == home_team].iterrows():
        start_date = parser.parse(row['Start'])
        if current_date >= start_date:
            is_manager += 1
            try:
                return Manager(
                    start_date=start_date.timestamp(),
                    days=(current_date - start_date).days,
                    name=row['Name'],
                    birthday=parser.parse(row['Birthday']).timestamp() if row['Birthday'] != '' else 0.0,
                    country=row['Country'],
                    month=current_date.month,
                )
            except Exception:
                pass
    return Manager(
        start_date=0.0,
        days=0,
        name='-',
        birthday=0.0,
        country='-',
        month=current_date.month,
    )


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
months = []
home_is_manager_and_league_same_country = []
away_is_manager_and_league_same_country = []

for index, row in england.iterrows():
    home_manager = extract_manager(row['home_team'], parser.parse(row['date']))
    away_manager = extract_manager(row['away_team'], parser.parse(row['date']))
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
    months.append(home_manager.month)
    home_is_manager_and_league_same_country.append(int(row['country'].lower() == row['home_manager_country'].lower()))
    away_is_manager_and_league_same_country.append(int(row['country'].lower() == row['away_manager_country'].lower()))

england['home_manager_working_days'] = home_days
england['away_manager_working_days'] = away_days
england['home_manager_name'] = home_names
england['away_manager_name'] = away_names
england['home_manager_start_date'] = home_start_dates
england['home_manager_birthday'] = home_birthdays
england['home_manager_country'] = home_countries
england['away_manager_start_date'] = away_start_dates
england['away_manager_birthday'] = away_birthdays
england['away_manager_country'] = away_countries
england['month'] = months
england['home_is_manager_and_league_same_country'] = home_is_manager_and_league_same_country
england['away_is_manager_and_league_same_country'] = away_is_manager_and_league_same_country

england.to_csv('all_england_v2.8.csv', index=False)
