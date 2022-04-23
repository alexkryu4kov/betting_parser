import json
import requests
from dataclasses import dataclass, asdict
from bs4 import BeautifulSoup


matcher = {
    2021: 'https://us.soccerway.com/national/england/premier-league/20212022/regular-season/r63396/venues/',
    2020: 'https://us.soccerway.com/national/england/premier-league/20202021/regular-season/r59136/venues/',
    2019: 'https://us.soccerway.com/national/england/premier-league/20192020/regular-season/r53145/venues/',
    2018: 'https://us.soccerway.com/national/england/premier-league/20182019/regular-season/r48730/venues/',
    2017: 'https://us.soccerway.com/national/england/premier-league/20172018/regular-season/r41547/venues/',
    2016: 'https://us.soccerway.com/national/england/premier-league/20162017/regular-season/r35992/venues/',
}

matcher_championship = {
    2021: 'https://us.soccerway.com/national/england/championship/20212022/regular-season/r63602/venues/',
    2020: 'https://us.soccerway.com/national/england/championship/20202021/regular-season/r59442/venues/',
    2019: 'https://us.soccerway.com/national/england/championship/20192020/regular-season/r53782/venues/',
    2018: 'https://us.soccerway.com/national/england/championship/20182019/regular-season/r48274/venues/',
    2017: 'https://us.soccerway.com/national/england/championship/20172018/regular-season/r42070/venues/',
    2016: 'https://us.soccerway.com/national/england/championship/20162017/regular-season/r36638/venues/',
}

matcher_league_one = {
    2021: 'https://us.soccerway.com/national/england/league-one/20212022/regular-season/r63612/venues/',
    2020: 'https://us.soccerway.com/national/england/league-one/20202021/regular-season/r59194/venues/',
    2019: 'https://us.soccerway.com/national/england/league-one/20192020/regular-season/r53677/venues/',
    2018: 'https://us.soccerway.com/national/england/league-one/20182019/regular-season/r48115/venues/',
    2017: 'https://us.soccerway.com/national/england/league-one/20172018/regular-season/r41820/venues/',
    2016: 'https://us.soccerway.com/national/england/league-one/20162017/regular-season/r36641/venues/',
}

matcher_league_two = {
    2021: 'https://us.soccerway.com/national/england/league-two/20212022/regular-season/r63679/venues/',
    2020: 'https://us.soccerway.com/national/england/league-two/20202021/regular-season/r59197/venues/',
    2019: 'https://us.soccerway.com/national/england/league-two/20192020/regular-season/r53874/venues/',
    2018: 'https://us.soccerway.com/national/england/league-two/20182019/regular-season/r48450/venues/',
    2017: 'https://us.soccerway.com/national/england/league-two/20172018/regular-season/r42073/venues/',
    2016: 'https://us.soccerway.com/national/england/league-two/20162017/regular-season/r36644/venues/',
}


@dataclass
class Info:
    season: int
    name: str
    stadium: str
    city: str
    capacity: str


stadiums = []

for k, v in matcher_league_two.items():
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
            Info(
                season=k,
                name=team_name,
                stadium=stadium_name,
                city=city,
                capacity=capacity
            )
        )


with open('../stadiums4.json', 'w') as f:
    json.dump([asdict(stadium) for stadium in stadiums], f)
