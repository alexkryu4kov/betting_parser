import json
from dataclasses import dataclass, asdict

import pandas as pd
import requests
from bs4 import BeautifulSoup

from matchers.stadiums_matcher import StadiumsMatcher

DATASET_PATH = '../all_england_v2.8.csv'

matcher = [
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


@dataclass
class StadiumInfo:
    season: int
    name: str
    stadium: str
    city: str
    capacity: str


stadiums = []

for league in matcher:
    for k, v in league.items():
        page = requests.get(v, headers={'User-Agent': 'Custom'})

        soup = BeautifulSoup(page.text, 'html.parser')
        thick = soup.find_all(class_='thick')
        h4 = soup.find_all(class_='right')
        for i, team in enumerate(thick):
            team_name = str(team).split('/">')[1].split('</a')[0]
            stadium_name = str(h4[i]).split('/venue/">')[1].split('</a>')[0]
            dd = str(h4[i]).split('<dd>')
            city = dd[1].split('</')[0]
            capacity = dd[2].split('/dt>')[0].split('</dd>')[0]
            stadiums.append(
                StadiumInfo(
                    season=k,
                    name=team_name,
                    stadium=stadium_name,
                    city=city,
                    capacity=capacity
                )
            )

new_stadiums = []
for index, stadium in enumerate(stadiums):
    try:
        if stadium.name == stadiums[index-1].name and stadium.season == stadiums[index-1].season:
            continue
    except IndexError:
        new_stadiums.append(stadium)
        continue
    new_stadiums.append(stadium)

stadiums_matcher = StadiumsMatcher()
stadiums_matcher.match_stadiums(new_stadiums)

dataset = pd.read_csv(DATASET_PATH)
stadiums_matcher.check_stadiums_match(dataset['home_team'].values)


with open('../data/stadiums.json', 'w') as f:
    json.dump([asdict(stadium) for stadium in new_stadiums], f)
