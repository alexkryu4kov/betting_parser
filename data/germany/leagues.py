leagues = [
    'L1',  # bundesliga
    'L2',  # 2.bundesliga
    'L3',  # 3.bundesliga
]

seasons_matcher = {
    'bundesliga-2016-2017': 2016,
    'bundesliga-2017-2018': 2017,
    'bundesliga-2018-2019': 2018,
    'bundesliga-2019-2020': 2019,
    'bundesliga-2020-2021': 2020,
    'bundesliga': 2021,
    '2-bundesliga-2016-2017': 2016,
    '2-bundesliga-2017-2018': 2017,
    '2-bundesliga-2018-2019': 2018,
    '2-bundesliga-2019-2020': 2019,
    '2-bundesliga-2020-2021': 2020,
    '2-bundesliga': 2021,
    '3-liga-2016-2017': 2016,
    '3-liga-2017-2018': 2017,
    '3-liga-2018-2019': 2018,
    '3-liga-2019-2020': 2019,
    '3-liga-2020-2021': 2020,
    '3-liga': 2021,
}

league_matcher = {
    'bundesliga-2016-2017': 'bundesliga',
    'bundesliga-2017-2018': 'bundesliga',
    'bundesliga-2018-2019': 'bundesliga',
    'bundesliga-2019-2020': 'bundesliga',
    'bundesliga-2020-2021': 'bundesliga',
    'bundesliga': 'bundesliga',
    '2-bundesliga-2016-2017': '2-bundesliga',
    '2-bundesliga-2017-2018': '2-bundesliga',
    '2-bundesliga-2018-2019': '2-bundesliga',
    '2-bundesliga-2019-2020': '2-bundesliga',
    '2-bundesliga-2020-2021': '2-bundesliga',
    '2-bundesliga': '2-bundesliga',
    '3-liga-2016-2017': '3-liga',
    '3-liga-2017-2018': '3-liga',
    '3-liga-2018-2019': '3-liga',
    '3-liga-2019-2020': '3-liga',
    '3-liga-2020-2021': '3-liga',
    '3-liga': '3-liga',
}


league_levels = {
    'bundesliga': 1,
    '2-bundesliga': 2,
    '3-liga': 3,
}


stadiums_matcher = [
    # bundesliga
    {
        2021: 'https://us.soccerway.com/national/germany/bundesliga/20212022/regular-season/r63141/venues/',
        2020: 'https://us.soccerway.com/national/germany/bundesliga/20202021/regular-season/r58871/venues/',
        2019: 'https://us.soccerway.com/national/germany/bundesliga/20192020/regular-season/r53499/venues/',
        2018: 'https://us.soccerway.com/national/germany/bundesliga/20182019/regular-season/r47657/venues/',
        2017: 'https://us.soccerway.com/national/germany/bundesliga/20172018/regular-season/r41485/venues/',
        2016: 'https://us.soccerway.com/national/germany/bundesliga/20162017/regular-season/r35823/venues/',
    },
    # 2.bundesliga
    {
        2021: 'https://us.soccerway.com/national/germany/2-bundesliga/20212022/regular-season/r63189/venues/',
        2020: 'https://us.soccerway.com/national/germany/2-bundesliga/20202021/regular-season/r58870/venues/',
        2019: 'https://us.soccerway.com/national/germany/2-bundesliga/20192020/regular-season/r53500/venues/',
        2018: 'https://us.soccerway.com/national/germany/2-bundesliga/20182019/regular-season/r47658/venues/',
        2017: 'https://us.soccerway.com/national/germany/2-bundesliga/20172018/regular-season/r41486/venues/',
        2016: 'https://us.soccerway.com/national/germany/2-bundesliga/20162017/regular-season/r35824/venues/',
    },
    # 3.bundesliga
    {
        2021: 'https://us.soccerway.com/national/germany/3-liga/20212022/regular-season/r63188/venues/',
        2020: 'https://us.soccerway.com/national/germany/3-liga/20202021/regular-season/r58861/venues/',
        2019: 'https://us.soccerway.com/national/germany/3-liga/20192020/regular-season/r53501/venues/',
        2018: 'https://us.soccerway.com/national/germany/3-liga/20182019/regular-season/r47659/venues/',
        2017: 'https://us.soccerway.com/national/germany/3-liga/20172018/regular-season/r41487/venues/',
        2016: 'https://us.soccerway.com/national/germany/3-liga/20162017/regular-season/r35874/venues/',
    },
]
