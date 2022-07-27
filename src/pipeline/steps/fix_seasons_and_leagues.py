from dateutil import parser

from data.world.leagues import league_levels, league_matcher
from pipeline.steps.abstract_step import AbstractStep
from pipeline.utils import create_season_year, extract_season_year


class FixSeasonAndLeaguesStep(AbstractStep):

    @classmethod
    def run(cls, dataset):
        weekdays = []
        levels = []
        leagues = []
        seasons = []
        months = []
        years = []
        for i, row in dataset.iterrows():
            parsed_date = parser.parse(row['date'])
            year = extract_season_year(row['league'], parsed_date)
            season = create_season_year(year)
            seasons.append(season)
            years.append(year)
            league = league_matcher.get(row['league'])
            if league:
                leagues.append(league)
            else:
                leagues.append(row['league'])
            levels.append(league_levels.get(league))
            weekdays.append(parsed_date.weekday())
            months.append(parsed_date.month)
        
        dataset['league_level'] = levels
        dataset['season'] = seasons
        dataset['league'] = leagues
        dataset['day_of_week'] = weekdays
        dataset['month'] = months
        dataset['year'] = years

        return dataset
