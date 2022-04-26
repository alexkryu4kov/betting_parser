leagues = [
    'GB1',  # premier-league
    'GB2',  # championship
    'GB3',  # league 1
    'GB4',  # league 2
    'CNAT',  # conference
    'NLS6',  # conference south - only 2021
    'NLN6',  # conference north - only 2021
]

seasons_matcher = {
    'premier-league-2016-2017': 2016,
    'premier-league-2017-2018': 2017,
    'premier-league-2018-2019': 2018,
    'premier-league-2019-2020': 2019,
    'premier-league-2020-2021': 2020,
    'premier-league': 2021,
    'championship-2016-2017': 2016,
    'championship-2017-2018': 2017,
    'championship-2018-2019': 2018,
    'championship-2019-2020': 2019,
    'championship-2020-2021': 2020,
    'championship': 2021,
    'league-one-2016-2017': 2016,
    'league-one-2017-2018': 2017,
    'league-one-2018-2019': 2018,
    'league-one-2019-2020': 2019,
    'league-one-2020-2021': 2020,
    'league-one': 2021,
    'league-two-2016-2017': 2016,
    'league-two-2017-2018': 2017,
    'league-two-2018-2019': 2018,
    'league-two-2019-2020': 2019,
    'league-two-2020-2021': 2020,
    'league-two': 2021,
    'national-league-2016-2017': 2016,
    'national-league-2017-2018': 2017,
    'national-league-2018-2019': 2018,
    'national-league-2019-2020': 2019,
    'national-league-2020-2021': 2020,
    'national-league': 2021,
    'national-league-south-2016-2017': 2016,
    'national-league-south-2017-2018': 2017,
    'national-league-south-2018-2019': 2018,
    'national-league-south-2019-2020': 2019,
    'national-league-south-2020-2021': 2020,
    'national-league-south': 2021,
    'national-league-north-2016-2017': 2016,
    'national-league-north-2017-2018': 2017,
    'national-league-north-2018-2019': 2018,
    'national-league-north-2019-2020': 2019,
    'national-league-north-2020-2021': 2020,
    'national-league-north': 2021,
}

league_matcher = {
    'premier-league-2016-2017': 'premier-league',
    'premier-league-2017-2018': 'premier-league',
    'premier-league-2018-2019': 'premier-league',
    'premier-league-2019-2020': 'premier-league',
    'premier-league-2020-2021': 'premier-league',
    'premier-league': 'premier-league',
    'championship-2016-2017': 'championship',
    'championship-2017-2018': 'championship',
    'championship-2018-2019': 'championship',
    'championship-2019-2020': 'championship',
    'championship-2020-2021': 'championship',
    'championship': 'championship',
    'league-one-2016-2017': 'league-one',
    'league-one-2017-2018': 'league-one',
    'league-one-2018-2019': 'league-one',
    'league-one-2019-2020': 'league-one',
    'league-one-2020-2021': 'league-one',
    'league-one': 'league-one',
    'league-two-2016-2017': 'league-two',
    'league-two-2017-2018': 'league-two',
    'league-two-2018-2019': 'league-two',
    'league-two-2019-2020': 'league-two',
    'league-two-2020-2021': 'league-two',
    'league-two': 'league-two',
    'national-league-2016-2017': 'national-league',
    'national-league-2017-2018': 'national-league',
    'national-league-2018-2019': 'national-league',
    'national-league-2019-2020': 'national-league',
    'national-league-2020-2021': 'national-league',
    'national-league': 'national-league',
    'national-league-south-2016-2017': 'national-league-south',
    'national-league-south-2017-2018': 'national-league-south',
    'national-league-south-2018-2019': 'national-league-south',
    'national-league-south-2019-2020': 'national-league-south',
    'national-league-south-2020-2021': 'national-league-south',
    'national-league-south': 'national-league-south',
    'national-league-north-2016-2017': 'national-league-north',
    'national-league-north-2017-2018': 'national-league-north',
    'national-league-north-2018-2019': 'national-league-north',
    'national-league-north-2019-2020': 'national-league-north',
    'national-league-north-2020-2021': 'national-league-north',
    'national-league-north': 'national-league-north',
}

league_levels = {
    'premier-league': 1,
    'championship': 2,
    'league-one': 3,
    'league-two': 4,
    'national-league': 5,
    'national-league-south': 6,
    'national-league-north': 6,
}

stadiums_matcher = [
    # premier-league
    {
        2021: 'https://us.soccerway.com/national/england/premier-league/20212022/regular-season/r63396/venues/',
        2020: 'https://us.soccerway.com/national/england/premier-league/20202021/regular-season/r59136/venues/',
        2019: 'https://us.soccerway.com/national/england/premier-league/20192020/regular-season/r53145/venues/',
        2018: 'https://us.soccerway.com/national/england/premier-league/20182019/regular-season/r48730/venues/',
        2017: 'https://us.soccerway.com/national/england/premier-league/20172018/regular-season/r41547/venues/',
        2016: 'https://us.soccerway.com/national/england/premier-league/20162017/regular-season/r35992/venues/',
    },
    # championship
    {
        2021: 'https://us.soccerway.com/national/england/championship/20212022/regular-season/r63602/venues/',
        2020: 'https://us.soccerway.com/national/england/championship/20202021/regular-season/r59442/venues/',
        2019: 'https://us.soccerway.com/national/england/championship/20192020/regular-season/r53782/venues/',
        2018: 'https://us.soccerway.com/national/england/championship/20182019/regular-season/r48274/venues/',
        2017: 'https://us.soccerway.com/national/england/championship/20172018/regular-season/r42070/venues/',
        2016: 'https://us.soccerway.com/national/england/championship/20162017/regular-season/r36638/venues/',
    },
    # league one
    {
        2021: 'https://us.soccerway.com/national/england/league-one/20212022/regular-season/r63612/venues/',
        2020: 'https://us.soccerway.com/national/england/league-one/20202021/regular-season/r59194/venues/',
        2019: 'https://us.soccerway.com/national/england/league-one/20192020/regular-season/r53677/venues/',
        2018: 'https://us.soccerway.com/national/england/league-one/20182019/regular-season/r48115/venues/',
        2017: 'https://us.soccerway.com/national/england/league-one/20172018/regular-season/r41820/venues/',
        2016: 'https://us.soccerway.com/national/england/league-one/20162017/regular-season/r36641/venues/',
    },
    # league two
    {
        2021: 'https://us.soccerway.com/national/england/league-two/20212022/regular-season/r63679/venues/',
        2020: 'https://us.soccerway.com/national/england/league-two/20202021/regular-season/r59197/venues/',
        2019: 'https://us.soccerway.com/national/england/league-two/20192020/regular-season/r53874/venues/',
        2018: 'https://us.soccerway.com/national/england/league-two/20182019/regular-season/r48450/venues/',
        2017: 'https://us.soccerway.com/national/england/league-two/20172018/regular-season/r42073/venues/',
        2016: 'https://us.soccerway.com/national/england/league-two/20162017/regular-season/r36644/venues/',
    },
    # conference national
    {
        2021: 'https://us.soccerway.com/national/england/conference-national/20212022/regular-season/r64296/venues',
        2020: 'https://us.soccerway.com/national/england/conference-national/20202021/regular-season/r59296/venues',
        2019: 'https://us.soccerway.com/national/england/conference-national/20192020/regular-season/r53131/venues',
        2018: 'https://us.soccerway.com/national/england/conference-national/20182019/regular-season/r48734/venues',
        2017: 'https://us.soccerway.com/national/england/conference-national/20172018/regular-season/r41651/venues',
        2016: 'https://us.soccerway.com/national/england/conference-national/20162017/regular-season/r35949/venues',
    },
    # conference north
    {
        2021: 'https://us.soccerway.com/national/england/conference-n--s/20212022/north/r64064/venues',
        2020: 'https://us.soccerway.com/national/england/conference-n--s/20202021/north/r59388/venues',
        2019: 'https://us.soccerway.com/national/england/conference-n--s/20192020/north/r53161/venues',
        2018: 'https://us.soccerway.com/national/england/conference-n--s/20182019/north/r47691/venues',
        2017: 'https://us.soccerway.com/national/england/conference-n--s/20172018/north/r41337/venues',
        2016: 'https://us.soccerway.com/national/england/conference-n--s/20162017/north/r36273/venues',
    },
    # conference south
    {
        2021: 'https://us.soccerway.com/national/england/conference-n--s/20212022/south/r64065/venues/',
        2020: 'https://us.soccerway.com/national/england/conference-n--s/20202021/south/r59392/venues',
        2019: 'https://us.soccerway.com/national/england/conference-n--s/20192020/south/r53165/venues',
        2018: 'https://us.soccerway.com/national/england/conference-n--s/20182019/south/r47695/venues',
        2017: 'https://us.soccerway.com/national/england/conference-n--s/20172018/south/r41340/venues',
        2016: 'https://us.soccerway.com/national/england/conference-n--s/20162017/south/r36276/venues',
    },
]
