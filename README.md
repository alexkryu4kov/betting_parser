# Парсер исторических данных о футбольных матчах

Загрузка данных о футбольных матчах из разных источников:
- [oddsportal](https://www.oddsportal.com/)
- [transfermarkt](https://www.transfermarkt.com/)
- [soccerway](https://us.soccerway.com/)

Готовит данные для [модели](https://github.com/macroslav/bets-model)


Предполагается скачивание данных по странам (команды, тренеры, стадионы, трансферы)
### TODO: надо описать здесь как именно эти данные скачиваются


Что надо сделать чтобы скачать данные по новой стране:
1) [Скачать ссылки](src/scripts/links_by_league_script.py) на нужную лигу
2) [Скачать данные](src/main_data_parsers/matches/parser.py) для нужной лиги
3) [Преобразовать их в csv](src/scripts/saver.py)
4) [Проверить что есть нужные данные для матчинга названий из разных ресурсов](src/pipeline/check_matching.py)   
Если таких данных нет, то их необходимо добавить.   
Руками :-(
5) [Запустить пайплайн](src/pipeline/pipe.py)
   - Матчинг названий
   - Добавятся признаки - сезон, год, месяц и т.д.
   - Добавится информация о командах
   - Добавится информация о тренерах
   - Добавится информация о стадионах
   - Добавится информация о трансферах
