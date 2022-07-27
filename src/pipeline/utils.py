from datetime import datetime


def extract_market_value(market_value):
    if market_value == 0.0:
        return 0.0
    if 'bn' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000_000
    if 'm' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000
    elif 'Th' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000
    else:
        return 0.0


def extract_age(age):
    if age == '-':
        return 0.0
    return age


def create_season_year(season: int) -> str:
    return f'{season}-{season+1}'


def extract_season_year(league: str, date: datetime) -> int:
    split_league = league.split('-')
    okay_elems = []
    for elem in split_league:
        if season_year_condition(elem):
            okay_elems.append(elem)
    if len(okay_elems) > 0:
        return int(okay_elems[0])
    if date.month < 6:
        return date.year - 1
    return date.year


def season_year_condition(year: str):
    try:
        int(year)
    except ValueError:
        return False
    return (len(year) == 4) and (int(year)//100 in range(19, 22))
