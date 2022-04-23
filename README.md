# betting_parser
Download data about football matches from different sources

Prepare data for model https://github.com/macroslav/bets-model


Последовательность действий:

1) [Скачать ссылки](scripts/links_script.py) на нужную лигу
2) [Скачать данные](main_data_parsers/parser.py) для нужной лиги
3) [Преобразовать их в csv](scripts/saver.py)  
4) [Сматчить названия команд](matchers/matcher.py) с oddsportal в названия команд с transfermarkt  
Предварительно нужно добавить нужные пары в словарь matches
5) [Добавить информацию о командах](pipeline/add_teams.py) в csv  
Предварительно нужно данные о командах [скачать](additional_data_parsers/teams.py)
6) [Добавить информацию о тренерах](pipeline/add_managers.py) в csv  
Предварительно нужно данные о тренерах [скачать](additional_data_parsers/managers.py)  
7) [Добавить информацию о стадионах](pipeline/add_stadiums.py) в csv  
Предварительно нужно данные о стадионах [скачать](additional_data_parsers/stadiums.py)  
После этого [сматчить названия команд](matchers/stadiums_matcher.py) с soccerway в названия команд с transfermarkt
8) [Добавить более подробную информацию о командах](pipeline/add_detailed_teams.py) в csv  
Предварительно нужно данные о командах [скачать](additional_data_parsers/teams_detailed.py)
9) [Добавить информацию о трансферах](pipeline/add_transfers.py) в csv  
Предварительно нужно данные о трансферах [скачать](additional_data_parsers/transfers.py)
10) [Почистить данные о лигах, сезонах и т.д.](pipeline/add_fix_data.py)
11) Опционально - [добавить новые данные к существующему csv](pipeline/merge_data.py)