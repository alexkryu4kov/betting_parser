leagues = {
    'spain': [
        'ES1',  # laliga
        'ES2',  # laliga2
        'E3G1',  # primera group 1 (since 2021)
        'E3G2',  # primera group 2 (since 2021)
        'ES3A',  # segunda B group 1 (2020 last)
        'ES3B',  # segunda B group 2 (2020 last)
        'ES3C',  # segunda B group 3 (2020 last)
        'ES3D',  # segunda B group 4 (2020 last)
        'ES3E',  # segunda B group 5 (2020 only)
    ],
    'england': [
        'GB1',  # premier-league
        'GB2',  # championship
        'GB3',  # league 1
        'GB4',  # league 2
        'CNAT',  # conference
        'NLS6',  # conference south - only 2021
        'NLN6',  # conference north - only 2021
    ],
    'france': [
        'FR1',  # ligue-1
        'FR2',  # ligue-2
        'FR3',  # national
    ],
    'italy': [
        'IT1',  # serie a
        'IT2',  # serie b
        'IT3A',  # serie c - a
        'IT3B',  # serie c - b
        'IT3C',  # serie c - c
    ],
    'germany': [
        'L1',  # bundesliga
        'L2',  # 2.bundesliga
        'L3',  # 3.bundesliga
    ]
}

league_matcher = {
    'italy': {
        'serie-c-group-a': 'serie-c',
        'serie-c-group-b': 'serie-c',
        'serie-c-group-c': 'serie-c',
        'lega-pro-group-a': 'serie-c',
        'lega-pro-group-b': 'serie-c',
        'lega-pro-group-c': 'serie-c',
    },
    'spain': {
        'segunda-division-b-group-1': 'primera-rfef',
        'segunda-division-b-group-2': 'primera-rfef',
        'segunda-division-b-group-3': 'primera-rfef',
        'segunda-division-b-group-4': 'primera-rfef',
        'segunda-division-b-group-5': 'primera-rfef',
    },
}

league_levels = {
    'england': {
        'premier-league': 1,
        'championship': 2,
        'league-one': 3,
        'league-two': 4,
        'national-league': 5,
        'national-league-south': 6,
        'national-league-north': 6,
    },
    'spain': {
        'laliga': 1,
        'laliga2': 2,
        'primera-rfef': 3,
    },
    'france': {
        'ligue-1': 1,
        'ligue-2': 2,
        'national': 3,
    },
    'germany': {
        'bundesliga': 1,
        '2-bundesliga': 2,
        '3-liga': 3,
    },
    'italy': {
        'serie-a': 1,
        'serie-b': 2,
        'serie-c': 3,
    },
}
