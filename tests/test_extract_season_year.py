from datetime import datetime

import pytest

from pipeline.utils import extract_season_year


@pytest.mark.parametrize(
    ('season', 'date', 'expected'),
    [
        pytest.param(
            'segunda-2017-2018',
            datetime(2018, 1, 1),
            2017,
        ),
        pytest.param(
            'segunda-2017',
            datetime(2018, 1, 1),
            2017,
        ),
        pytest.param(
            'segunda',
            datetime(2018, 1, 1),
            2017,
        ),
        pytest.param(
            '2-segunda',
            datetime(2018, 1, 1),
            2017,
        ),
        pytest.param(
            'north-segunda',
            datetime(2018, 1, 1),
            2017,
        ),
        pytest.param(
            'segunda',
            datetime(2018, 7, 1),
            2018,
        ),
    ]
)
def test_extract_season_year(season, date, expected):
    assert extract_season_year(season, date) == expected
