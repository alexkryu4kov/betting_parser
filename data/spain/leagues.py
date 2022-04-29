leagues = [
    'ES1',  # laliga
    'ES2',  # laliga2
    'E3G1',  # primera group 1 (since 2021)
    'E3G2',  # primera group 2 (since 2021)
    'ES3A',  # segunda B group 1 (2020 last)
    'ES3B',  # segunda B group 2 (2020 last)
    'ES3C',  # segunda B group 3 (2020 last)
    'ES3D',  # segunda B group 4 (2020 last)
    'ES3E',  # segunda B group 5 (2020 only)
]

seasons_matcher = {
    'laliga-2016-2017': 2016,
    'laliga-2017-2018': 2017,
    'laliga-2018-2019': 2018,
    'laliga-2019-2020': 2019,
    'laliga-2020-2021': 2020,
    'laliga': 2021,
    'laliga2-2016-2017': 2016,
    'laliga2-2017-2018': 2017,
    'laliga2-2018-2019': 2018,
    'laliga2-2019-2020': 2019,
    'laliga2-2020-2021': 2020,
    'laliga2': 2021,
    'segunda-division-b-group-1-2016-2017': 2016,
    'segunda-division-b-group-1-2017-2018': 2017,
    'segunda-division-b-group-1-2018-2019': 2018,
    'segunda-division-b-group-1-2019-2020': 2019,
    'segunda-division-b-group-1-2020-2021': 2020,
    'segunda-division-b-group-2-2016-2017': 2016,
    'segunda-division-b-group-2-2017-2018': 2017,
    'segunda-division-b-group-2-2018-2019': 2018,
    'segunda-division-b-group-2-2019-2020': 2019,
    'segunda-division-b-group-2-2020-2021': 2020,
    'segunda-division-b-group-3-2016-2017': 2016,
    'segunda-division-b-group-3-2017-2018': 2017,
    'segunda-division-b-group-3-2018-2019': 2018,
    'segunda-division-b-group-3-2019-2020': 2019,
    'segunda-division-b-group-3-2020-2021': 2020,
    'segunda-division-b-group-4-2016-2017': 2016,
    'segunda-division-b-group-4-2017-2018': 2017,
    'segunda-division-b-group-4-2018-2019': 2018,
    'segunda-division-b-group-4-2019-2020': 2019,
    'segunda-division-b-group-4-2020-2021': 2020,
    'segunda-division-b-group-5-2020-2021': 2020,
    'primera-rfef-group-1': 2021,
    'primera-rfef-group-2': 2021,
}

league_matcher = {
    'laliga-2016-2017': 'laliga',
    'laliga-2017-2018': 'laliga',
    'laliga-2018-2019': 'laliga',
    'laliga-2019-2020': 'laliga',
    'laliga-2020-2021': 'laliga',
    'laliga': 'laliga',
    'laliga2-2016-2017': 'laliga2',
    'laliga2-2017-2018': 'laliga2',
    'laliga2-2018-2019': 'laliga2',
    'laliga2-2019-2020': 'laliga2',
    'laliga2-2020-2021': 'laliga2',
    'laliga2': 'laliga2',
    'segunda-division-b-group-1-2016-2017': 'primera-rfef',
    'segunda-division-b-group-1-2017-2018': 'primera-rfef',
    'segunda-division-b-group-1-2018-2019': 'primera-rfef',
    'segunda-division-b-group-1-2019-2020': 'primera-rfef',
    'segunda-division-b-group-1-2020-2021': 'primera-rfef',
    'segunda-division-b-group-2-2016-2017': 'primera-rfef',
    'segunda-division-b-group-2-2017-2018': 'primera-rfef',
    'segunda-division-b-group-2-2018-2019': 'primera-rfef',
    'segunda-division-b-group-2-2019-2020': 'primera-rfef',
    'segunda-division-b-group-2-2020-2021': 'primera-rfef',
    'segunda-division-b-group-3-2016-2017': 'primera-rfef',
    'segunda-division-b-group-3-2017-2018': 'primera-rfef',
    'segunda-division-b-group-3-2018-2019': 'primera-rfef',
    'segunda-division-b-group-3-2019-2020': 'primera-rfef',
    'segunda-division-b-group-3-2020-2021': 'primera-rfef',
    'segunda-division-b-group-4-2016-2017': 'primera-rfef',
    'segunda-division-b-group-4-2017-2018': 'primera-rfef',
    'segunda-division-b-group-4-2018-2019': 'primera-rfef',
    'segunda-division-b-group-4-2019-2020': 'primera-rfef',
    'segunda-division-b-group-4-2020-2021': 'primera-rfef',
    'segunda-division-b-group-5-2020-2021': 'primera-rfef',
    'primera-rfef-group-1': 'primera-rfef',
    'primera-rfef-group-2': 'primera-rfef',
}


league_levels = {
    'laliga': 1,
    'laliga2': 2,
    'primera-rfef': 3,
}

stadiums_matcher = [
    # laliga
    {
        2021: 'https://us.soccerway.com/national/spain/primera-division/20212022/regular-season/r63145/venues/',
        2020: 'https://us.soccerway.com/national/spain/primera-division/20202021/regular-season/r59097/venues',
        2019: 'https://us.soccerway.com/national/spain/primera-division/20192020/regular-season/r53502/venues/',
        2018: 'https://us.soccerway.com/national/spain/primera-division/20182019/regular-season/r47983/venues/',
        2017: 'https://us.soccerway.com/national/spain/primera-division/20172018/regular-season/r41509/venues/',
        2016: 'https://us.soccerway.com/national/spain/primera-division/20162017/regular-season/r35880/venues/',
    },
    # laliga2
    {
        2021: 'https://us.soccerway.com/national/spain/segunda-division/20212022/regular-season/r64292/venues/',
        2020: 'https://us.soccerway.com/national/spain/segunda-division/20202021/regular-season/r59744/venues',
        2019: 'https://us.soccerway.com/national/spain/segunda-division/20192020/regular-season/r54950/venues/',
        2018: 'https://us.soccerway.com/national/spain/segunda-division/20182019/regular-season/r49197/venues/',
        2017: 'https://us.soccerway.com/national/spain/segunda-division/20172018/regular-season/r42973/venues/',
        2016: 'https://us.soccerway.com/national/spain/segunda-division/20162017/regular-season/r37748/venues/',
    },
    # primera-a
    {
        2021: 'https://us.soccerway.com/national/spain/segunda-b/20212022/group-1/r63613/venues/',
        2020: 'https://us.soccerway.com/national/spain/segunda-b/20202021/group-1/r59776/venues/',
        2019: 'https://us.soccerway.com/national/spain/segunda-b/20192020/group-1/r55037/venues/',
        2018: 'https://us.soccerway.com/national/spain/segunda-b/20182019/group-1/r49404/venues/',
        2017: 'https://us.soccerway.com/national/spain/segunda-b/20172018/group-1/r42976/venues/',
        2016: 'https://us.soccerway.com/national/spain/segunda-b/20162017/group-1/r38114/venues/',
    },
    # primera-b
    {
        2021: 'https://us.soccerway.com/national/spain/segunda-b/20212022/group-2/r63615/venues/',
        2020: 'https://us.soccerway.com/national/spain/segunda-b/20202021/group-2/r59777/venues/',
        2019: 'https://us.soccerway.com/national/spain/segunda-b/20192020/group-2/r55038/venues/',
        2018: 'https://us.soccerway.com/national/spain/segunda-b/20182019/group-2/r49405/venues/',
        2017: 'https://us.soccerway.com/national/spain/segunda-b/20172018/group-2/r42977/venues/',
        2016: 'https://us.soccerway.com/national/spain/segunda-b/20162017/group-2/r38115/venues/',
    },
    # segunda-group-3
    {
        2020: 'https://us.soccerway.com/national/spain/segunda-b/20202021/group-3/r59778/venues/',
        2019: 'https://us.soccerway.com/national/spain/segunda-b/20192020/group-3/r55039/venues/',
        2018: 'https://us.soccerway.com/national/spain/segunda-b/20182019/group-3/r49406/venues/',
        2017: 'https://us.soccerway.com/national/spain/segunda-b/20172018/group-3/r42978/venues/',
        2016: 'https://us.soccerway.com/national/spain/segunda-b/20162017/group-3/r38116/venues/',
    },
    # segunda-group-4
    {
        2020: 'https://us.soccerway.com/national/spain/segunda-b/20202021/group-4/r59779/venues/',
        2019: 'https://us.soccerway.com/national/spain/segunda-b/20192020/group-4/r55040/venues/',
        2018: 'https://us.soccerway.com/national/spain/segunda-b/20182019/group-4/r49407/venues/',
        2017: 'https://us.soccerway.com/national/spain/segunda-b/20172018/group-4/r42979/venues/',
        2016: 'https://us.soccerway.com/national/spain/segunda-b/20162017/group-4/r38117/venues/',
    },
    # segunda-group-5
    {
        2020: 'https://us.soccerway.com/national/spain/segunda-b/20202021/group-5/r60056/venues/',
    },
]
