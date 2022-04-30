leagues = [
    'IT1',  # serie a
    'IT2',  # serie b
    'IT3A',  # serie c - a
    'IT3B',  # serie c - b
    'IT3C',  # serie c - c
]

seasons_matcher = {
    'serie-a-2016-2017': 2016,
    'serie-a-2017-2018': 2017,
    'serie-a-2018-2019': 2018,
    'serie-a-2019-2020': 2019,
    'serie-a-2020-2021': 2020,
    'serie-a': 2021,
    'serie-b-2016-2017': 2016,
    'serie-b-2017-2018': 2017,
    'serie-b-2018-2019': 2018,
    'serie-b-2019-2020': 2019,
    'serie-b-2020-2021': 2020,
    'serie-b': 2021,
    'serie-c-group-a-2016-2017': 2016,
    'serie-c-group-a-2017-2018': 2017,
    'serie-c-group-a-2018-2019': 2018,
    'serie-c-group-a-2019-2020': 2019,
    'serie-c-group-a-2020-2021': 2020,
    'serie-c-group-a': 2021,
    'serie-c-group-b-2016-2017': 2016,
    'serie-c-group-b-2017-2018': 2017,
    'serie-c-group-b-2018-2019': 2018,
    'serie-c-group-b-2019-2020': 2019,
    'serie-c-group-b-2020-2021': 2020,
    'serie-c-group-b': 2021,
    'serie-c-group-c-2016-2017': 2016,
    'serie-c-group-c-2017-2018': 2017,
    'serie-c-group-c-2018-2019': 2018,
    'serie-c-group-c-2019-2020': 2019,
    'serie-c-group-c-2020-2021': 2020,
    'serie-c-group-c': 2021,
    'lega-pro-group-a-2016-2017': 2016,
    'lega-pro-group-b-2016-2017': 2016,
    'lega-pro-group-c-2016-2017': 2016,
}

league_matcher = {
    'serie-a-2016-2017': 'serie-a',
    'serie-a-2017-2018': 'serie-a',
    'serie-a-2018-2019': 'serie-a',
    'serie-a-2019-2020': 'serie-a',
    'serie-a-2020-2021': 'serie-a',
    'serie-a': 'serie-a',
    'serie-b-2016-2017': 'serie-b',
    'serie-b-2017-2018': 'serie-b',
    'serie-b-2018-2019': 'serie-b',
    'serie-b-2019-2020': 'serie-b',
    'serie-b-2020-2021': 'serie-b',
    'serie-b': 'serie-b',
    'serie-c-group-a-2016-2017': 'serie-c',
    'serie-c-group-a-2017-2018': 'serie-c',
    'serie-c-group-a-2018-2019': 'serie-c',
    'serie-c-group-a-2019-2020': 'serie-c',
    'serie-c-group-a-2020-2021': 'serie-c',
    'serie-c-group-a': 'serie-c',
    'serie-c-group-b-2016-2017': 'serie-c',
    'serie-c-group-b-2017-2018': 'serie-c',
    'serie-c-group-b-2018-2019': 'serie-c',
    'serie-c-group-b-2019-2020': 'serie-c',
    'serie-c-group-b-2020-2021': 'serie-c',
    'serie-c-group-b': 'serie-c',
    'serie-c-group-c-2016-2017': 'serie-c',
    'serie-c-group-c-2017-2018': 'serie-c',
    'serie-c-group-c-2018-2019': 'serie-c',
    'serie-c-group-c-2019-2020': 'serie-c',
    'serie-c-group-c-2020-2021': 'serie-c',
    'serie-c-group-c': 'serie-c',
    'lega-pro-group-a-2016-2017': 'serie-c',
    'lega-pro-group-b-2016-2017': 'serie-c',
    'lega-pro-group-c-2016-2017': 'serie-c',
}

league_levels = {
    'serie-a': 1,
    'serie-b': 2,
    'serie-c': 3,
}

stadiums_matcher = [
    # serie-a
    {
        2021: 'https://us.soccerway.com/national/italy/serie-a/20212022/regular-season/r63208/venues/',
        2020: 'https://us.soccerway.com/national/italy/serie-a/20202021/regular-season/r59286/venues/',
        2019: 'https://us.soccerway.com/national/italy/serie-a/20192020/regular-season/r54890/venues/',
        2018: 'https://us.soccerway.com/national/italy/serie-a/20182019/regular-season/r48235/venues/',
        2017: 'https://us.soccerway.com/national/italy/serie-a/20172018/regular-season/r42011/venues/',
        2016: 'https://us.soccerway.com/national/italy/serie-a/20162017/regular-season/r36003/venues/',
    },
    # serie-b
    {
        2021: 'https://us.soccerway.com/national/italy/serie-b/20212022/regular-season/r63606/venues/',
        2020: 'https://us.soccerway.com/national/italy/serie-b/20202021/regular-season/r59840/venues/',
        2019: 'https://us.soccerway.com/national/italy/serie-b/20192020/regular-season/r54637/venues/',
        2018: 'https://us.soccerway.com/national/italy/serie-b/20182019/regular-season/r49002/venues/',
        2017: 'https://us.soccerway.com/national/italy/serie-b/20172018/regular-season/r42672/venues/',
        2016: 'https://us.soccerway.com/national/italy/serie-b/20162017/regular-season/r37192/venues/',
    },
    # serie-c-a
    {
        2021: 'https://us.soccerway.com/national/italy/serie-c1/20212022/girone-a/r64430/venues/',
        2020: 'https://us.soccerway.com/national/italy/serie-c1/20202021/girone-a/r60062/venues/',
        2019: 'https://us.soccerway.com/national/italy/serie-c1/20192020/girone-a/r54858/venues/',
        2018: 'https://us.soccerway.com/national/italy/serie-c1/20182019/girone-a/r49267/venues/',
        2017: 'https://us.soccerway.com/national/italy/serie-c1/20172018/girone-a/r42820/venues/',
        2016: 'https://us.soccerway.com/national/italy/serie-c1/20162017/girone-a/r37482/venues/',
    },
    # serie-c-b
    {
        2021: 'https://us.soccerway.com/national/italy/serie-c1/20212022/girone-b/r64431/venues/',
        2020: 'https://us.soccerway.com/national/italy/serie-c1/20202021/girone-b/r60063/venues/',
        2019: 'https://us.soccerway.com/national/italy/serie-c1/20192020/girone-b/r54859/venues/',
        2018: 'https://us.soccerway.com/national/italy/serie-c1/20182019/girone-b/r49268/venues/',
        2017: 'https://us.soccerway.com/national/italy/serie-c1/20172018/girone-b/r42821/venues/',
        2016: 'https://us.soccerway.com/national/italy/serie-c1/20162017/girone-b/r37483/venues/',
    },
    # serie-c-c
    {
        2021: 'https://us.soccerway.com/national/italy/serie-c1/20212022/girone-c/r64432/venues/',
        2020: 'https://us.soccerway.com/national/italy/serie-c1/20202021/girone-c/r60064/venues/',
        2019: 'https://us.soccerway.com/national/italy/serie-c1/20192020/girone-c/r54860/venues/',
        2018: 'https://us.soccerway.com/national/italy/serie-c1/20182019/girone-c/r49269/venues/',
        2017: 'https://us.soccerway.com/national/italy/serie-c1/20172018/girone-c/r42822/venues/',
        2016: 'https://us.soccerway.com/national/italy/serie-c1/20162017/girone-c/r37484/venues/',
    },
]
