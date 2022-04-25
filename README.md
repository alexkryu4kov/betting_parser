# Парсер исторических данных о футбольных матчах

Загрузка данных о футбольных матчах из разных источников:
- [oddsportal](https://www.oddsportal.com/)
- [transfermarkt](https://www.transfermarkt.com/)
- [soccerway](https://us.soccerway.com/)

Готовит данные для [модели](https://github.com/macroslav/bets-model)


Предполагается скачивание данных по странам

Подготовительная работа
1) Поправить страну в [конфиге](config.py). Также здесь надо поднимать версию общего csv и задавать название конкретной лиги
2) Добавить директорию для страны в [директорию с данными](data)
3) Исправить конфиг для лиг по аналогии с [Англией](data/england/leagues.py)


Что надо сделать чтобы скачать данные по новой стране:
1) [Скачать ссылки](scripts/links_script.py) на нужную лигу
2) [Скачать данные](main_data_parsers/parser.py) для нужной лиги
3) [Преобразовать их в csv](scripts/saver.py)
4) Запустить все [парсеры](additional_data_parsers) по очереди:
- [индексы](additional_data_parsers/indices.py)
- [менеджеры](additional_data_parsers/managers.py)
- [стадионы](additional_data_parsers/stadiums.py)
- [команды](additional_data_parsers/teams.py)
- [детальная информация по командам](additional_data_parsers/teams_detailed.py)
- [трансферы](additional_data_parsers/transfers.py)


Как добавить скачанные данные в основной csv:
1) Запустить [матчер](pipeline/0_matcher.py) в режиме без сохранения в файл!!!  
Сейчас для этого надо закомментировать три последние строки
2) По результатам работы матчера, добавить нужные названия команд по аналогии с [Англией](data/england/matches.py)
3) [Запустить матчер](pipeline/0_matcher.py) в боевом режиме
Для этого надо раскомментировать последние строки
4) Последовательно запустить [этапы пайплайна](pipeline)
- [исправить данные о сезонах, лигах и т.д.](pipeline/1_fix_seasons_and_leagues.py)
- [добавить информацию о командах](pipeline/2_add_teams.py)
- [добавить информацию о тренерах](pipeline/3_add_managers.py)
- [добавить информацию о стадионах](pipeline/4_add_stadiums.py)
- [добавить детальную информацию о командах](pipeline/5_add_detailed_teams.py)
- [добавить информацию о тренерах](pipeline/6_add_transfers.py)
- [слить данные в общий csv](pipeline/7_merge_data.py)