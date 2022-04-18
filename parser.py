import logging
import time
from dataclasses import asdict

from bs4 import BeautifulSoup

from entity import MatchInfo, ResultMatchInfo


months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}


def decorator(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 0, 0
    return inner


class Parser:

    def __init__(self, browser, url):
        self._url = url
        self._browser = browser
        self._results_url_full = f'{url}#1X2;2'
        self._results_url_first = f'{url}#1X2;3'
        self._results_url_second = f'{url}#1X2;4'
        self._amounts_url_full = f'{url}#over-under;2'
        self._amounts_url_first = f'{url}#over-under;3'
        self._amounts_url_second = f'{url}#over-under;4'
        self._both_url_full = f'{url}#bts;2'
        self._both_url_first = f'{url}#bts;3'
        self._both_url_second = f'{url}#bts;4'
        self._handicap_url_full = f'{url}#ah;2'
        self._handicap_url_first = f'{url}#ah;3'
        self._handicap_url_second = f'{url}#ah;4'
        self._double_chance_url_full = f'{url}#double;2'
        self._double_chance_url_first = f'{url}#double;3'
        self._double_chance_url_second = f'{url}#double;4'
        self._odd_even_url_full = f'{url}#odd-even;2'
        self._odd_even_url_first = f'{url}#odd-even;3'
        self._odd_even_url_second = f'{url}#odd-even;4'
        self._correct_score_url = f'{url}#cs;2'
        self._halfs_url = f'{url}#ht-ft;2'
        self._results_page_full = None
        self._results_page_first = None
        self._results_page_second = None
        self._amounts_page_full = None
        self._amounts_page_first = None
        self._amounts_page_second = None
        self._both_page_full = None
        self._both_page_first = None
        self._both_page_second = None
        self._handicap_page_full = None
        self._handicap_page_first = None
        self._handicap_page_second = None
        self._double_chance_page_full = None
        self._double_chance_page_first = None
        self._double_chance_page_second = None
        self._odd_even_page_full = None
        self._odd_even_page_first = None
        self._odd_even_page_second = None
        self._correct_score_page = None
        self._halfs_page = None

    def get_match_info(self):
        self._get_pages()
        day_of_week, date, t = self._extract_date()
        season = self._extract_season(date)
        country, league = self._extract_country_league()
        team1, team2 = self._extract_teams()
        home, draw, away = self._extract_home_draw_away(self._results_page_full)
        home_first, draw_first, away_first = self._extract_home_draw_away(self._results_page_first)
        home_second, draw_second, away_second = self._extract_home_draw_away(self._results_page_second)
        over_05_first, under_05_first = self._extract_over_under(self._amounts_page_first, 'P-0.50-0-0')
        over_1_first, under_1_first = self._extract_over_under(self._amounts_page_first, 'P-1.00-0-0')
        over_15_first, under_15_first = self._extract_over_under(self._amounts_page_first, 'P-1.50-0-0')
        over_2_first, under_2_first = self._extract_over_under(self._amounts_page_first, 'P-2.00-0-0')
        over_05_second, under_05_second = self._extract_over_under(self._amounts_page_second, 'P-0.50-0-0')
        over_1_second, under_1_second = self._extract_over_under(self._amounts_page_second, 'P-1.00-0-0')
        over_15_second, under_15_second = self._extract_over_under(self._amounts_page_second, 'P-1.50-0-0')
        over_2_second, under_2_second = self._extract_over_under(self._amounts_page_second, 'P-2.00-0-0')
        over_1, under_1 = self._extract_over_under(self._amounts_page_full, 'P-1.00-0-0')
        over_15, under_15 = self._extract_over_under(self._amounts_page_full, 'P-1.50-0-0')
        over_2, under_2 = self._extract_over_under(self._amounts_page_full, 'P-2.00-0-0')
        over_25, under_25 = self._extract_over_under(self._amounts_page_full, 'P-2.50-0-0')
        over_3, under_3 = self._extract_over_under(self._amounts_page_full, 'P-3.00-0-0')
        over_35, under_35 = self._extract_over_under(self._amounts_page_full, 'P-3.50-0-0')
        home_handicap_0, away_handicap_0 = self._extract_handicap(self._handicap_page_full, 'P-0.00-0-0')
        home_handicap_minus_15, away_handicap_minus_15 = self._extract_handicap(self._handicap_page_full, 'P--1.50-0-0')
        home_handicap_minus_1, away_handicap_minus_1 = self._extract_handicap(self._handicap_page_full, 'P--1.00-0-0')
        home_handicap_plus_15, away_handicap_plus_15 = self._extract_handicap(self._handicap_page_full, 'P-1.50-0-0')
        home_handicap_plus_1, away_handicap_plus_1 = self._extract_handicap(self._handicap_page_full, 'P-1.00-0-0')
        home_handicap_0_first, away_handicap_0_first = self._extract_handicap(self._handicap_page_first, 'P-0.00-0-0')
        home_handicap_minus_15_first, away_handicap_minus_15_first = self._extract_handicap(self._handicap_page_first, 'P--1.50-0-0')
        home_handicap_minus_1_first, away_handicap_minus_1_first = self._extract_handicap(self._handicap_page_first, 'P--1.00-0-0')
        home_handicap_plus_15_first, away_handicap_plus_15_first = self._extract_handicap(self._handicap_page_first, 'P-1.50-0-0')
        home_handicap_plus_1_first, away_handicap_plus_1_first = self._extract_handicap(self._handicap_page_first, 'P-1.00-0-0')
        home_handicap_0_second, away_handicap_0_second = self._extract_handicap(self._handicap_page_second, 'P-0.00-0-0')
        home_handicap_minus_15_second, away_handicap_minus_15_second = self._extract_handicap(self._handicap_page_second, 'P--1.50-0-0')
        home_handicap_minus_1_second, away_handicap_minus_1_second = self._extract_handicap(self._handicap_page_second, 'P--1.00-0-0')
        home_handicap_plus_15_second, away_handicap_plus_15_second = self._extract_handicap(self._handicap_page_second, 'P-1.50-0-0')
        home_handicap_plus_1_second, away_handicap_plus_1_second = self._extract_handicap(self._handicap_page_second, 'P-1.00-0-0')
        yes, no = self._extract_both(self._both_page_full)
        yes_first, no_first = self._extract_both(self._both_page_first)
        yes_second, no_second = self._extract_both(self._both_page_second)
        odd, even = self._extract_odd_even(self._odd_even_page_full)
        odd_first, even_first = self._extract_odd_even(self._odd_even_page_first)
        odd_second, even_second = self._extract_odd_even(self._odd_even_page_second)
        home_scored, away_scored, home_first_scored, home_second_scored, away_first_scored, away_second_scored = self._extract_result(self._results_page_full)
        home_double_chance, no_draw, away_double_chance = self._extract_double_chance(self._double_chance_page_full)
        home_double_chance_first, no_draw_first, away_double_chance_first = self._extract_double_chance(
            self._double_chance_page_first,
        )
        home_double_chance_second, no_draw_second, away_double_chance_second = self._extract_double_chance(
            self._double_chance_page_second,
        )
        correct_score10 = self._extract_correct_score(self._correct_score_page, 'P-0.00-2-0')
        correct_score20 = self._extract_correct_score(self._correct_score_page, 'P-0.00-5-0')
        correct_score21 = self._extract_correct_score(self._correct_score_page, 'P-0.00-6-0')
        correct_score30 = self._extract_correct_score(self._correct_score_page, 'P-0.00-10-0')
        correct_score31 = self._extract_correct_score(self._correct_score_page, 'P-0.00-11-0')
        correct_score32 = self._extract_correct_score(self._correct_score_page, 'P-0.00-12-0')
        correct_score40 = self._extract_correct_score(self._correct_score_page, 'P-0.00-18-0')
        correct_score41 = self._extract_correct_score(self._correct_score_page, 'P-0.00-19-0')
        correct_score00 = self._extract_correct_score(self._correct_score_page, 'P-0.00-1-0')
        correct_score11 = self._extract_correct_score(self._correct_score_page, 'P-0.00-3-0')
        correct_score22 = self._extract_correct_score(self._correct_score_page, 'P-0.00-7-0')
        correct_score33 = self._extract_correct_score(self._correct_score_page, 'P-0.00-13-0')
        correct_score01 = self._extract_correct_score(self._correct_score_page, 'P-0.00-4-0')
        correct_score02 = self._extract_correct_score(self._correct_score_page, 'P-0.00-9-0')
        correct_score12 = self._extract_correct_score(self._correct_score_page, 'P-0.00-8-0')
        correct_score03 = self._extract_correct_score(self._correct_score_page, 'P-0.00-16-0')
        correct_score13 = self._extract_correct_score(self._correct_score_page, 'P-0.00-15-0')
        correct_score23 = self._extract_correct_score(self._correct_score_page, 'P-0.00-14-0')
        correct_score04 = self._extract_correct_score(self._correct_score_page, 'P-0.00-25-0')
        correct_score14 = self._extract_correct_score(self._correct_score_page, 'P-0.00-24-0')
        home_home = self._extract_halfs(self._halfs_page, 'P-0.00-27-0')
        home_draw = self._extract_halfs(self._halfs_page, 'P-0.00-30-0')
        home_away = self._extract_halfs(self._halfs_page, 'P-0.00-33-0')
        draw_home = self._extract_halfs(self._halfs_page, 'P-0.00-28-0')
        draw_draw = self._extract_halfs(self._halfs_page, 'P-0.00-31-0')
        draw_away = self._extract_halfs(self._halfs_page, 'P-0.00-34-0')
        away_home = self._extract_halfs(self._halfs_page, 'P-0.00-29-0')
        away_draw = self._extract_halfs(self._halfs_page, 'P-0.00-32-0')
        away_away = self._extract_halfs(self._halfs_page, 'P-0.00-35-0')
        match_info = asdict(
            MatchInfo(
                day_of_week=day_of_week,
                date=date,
                time=t,
                season=season,
                country=country,
                league=league,
                league_level=3,
                home_team=team1,
                away_team=team2,
                home_win_rate=home,
                draw_rate=draw,
                away_win_rate=away,
                home_first_half_win_rate=home_first,
                home_second_half_win_rate=home_second,
                draw_first_half_rate=draw_first,
                draw_second_half_rate=draw_second,
                away_first_half_win_rate=away_first,
                away_second_half_win_rate=away_second,
                total_over_1_rate=over_1,
                total_under_1_rate=under_1,
                total_over_15_rate=over_15,
                total_under_15_rate=under_15,
                total_over_2_rate=over_2,
                total_under_2_rate=under_2,
                total_over_25_rate=over_25,
                total_under_25_rate=under_25,
                total_over_3_rate=over_3,
                total_under_3_rate=under_3,
                total_over_35_rate=over_35,
                total_under_35_rate=under_35,
                total_first_half_over_05_rate=over_05_first,
                total_first_half_under_05_rate=under_05_first,
                total_first_half_over_1_rate=over_1_first,
                total_first_half_under_1_rate=under_1_first,
                total_first_half_over_15_rate=over_15_first,
                total_first_half_under_15_rate=under_15_first,
                total_first_half_over_2_rate=over_2_first,
                total_first_half_under_2_rate=under_2_first,
                total_second_half_over_05_rate=over_05_second,
                total_second_half_under_05_rate=under_05_second,
                total_second_half_over_1_rate=over_1_second,
                total_second_half_under_1_rate=under_1_second,
                total_second_half_over_15_rate=over_15_second,
                total_second_half_under_15_rate=under_15_second,
                total_second_half_over_2_rate=over_2_second,
                total_second_half_under_2_rate=under_2_second,
                both_team_to_score_yes=yes,
                both_team_to_score_no=no,
                both_team_to_score_first_half_yes=yes_first,
                both_team_to_score_first_half_no=no_first,
                both_team_to_score_second_half_yes=yes_second,
                both_team_to_score_second_half_no=no_second,
                home_handicap_0=home_handicap_0,
                away_handicap_0=away_handicap_0,
                home_handicap_minus_15=home_handicap_minus_15,
                home_handicap_minus_1=home_handicap_minus_1,
                home_handicap_plus_15=home_handicap_plus_15,
                home_handicap_plus_1=home_handicap_plus_1,
                away_handicap_minus_15=away_handicap_minus_15,
                away_handicap_minus_1=away_handicap_minus_1,
                away_handicap_plus_15=away_handicap_plus_15,
                away_handicap_plus_1=away_handicap_plus_1,
                home_first_half_handicap_0=home_handicap_0_first,
                away_first_half_handicap_0=away_handicap_0_first,
                home_first_half_handicap_minus_15=home_handicap_minus_15_first,
                home_first_half_handicap_minus_1=home_handicap_minus_1_first,
                home_first_half_handicap_plus_15=home_handicap_plus_15_first,
                home_first_half_handicap_plus_1=home_handicap_plus_1_first,
                away_first_half_handicap_minus_15=away_handicap_minus_15_first,
                away_first_half_handicap_minus_1=away_handicap_minus_1_first,
                away_first_half_handicap_plus_15=away_handicap_plus_15_first,
                away_first_half_handicap_plus_1=away_handicap_plus_1_first,
                home_second_half_handicap_0=home_handicap_0_second,
                away_second_half_handicap_0=away_handicap_0_second,
                home_second_half_handicap_minus_15=home_handicap_minus_15_second,
                home_second_half_handicap_minus_1=home_handicap_minus_1_second,
                home_second_half_handicap_plus_15=home_handicap_plus_15_second,
                home_second_half_handicap_plus_1=home_handicap_plus_1_second,
                away_second_half_handicap_minus_15=away_handicap_minus_15_second,
                away_second_half_handicap_minus_1=away_handicap_minus_1_second,
                away_second_half_handicap_plus_15=away_handicap_plus_15_second,
                away_second_half_handicap_plus_1=away_handicap_plus_1_second,
                home_double_chance_rate=home_double_chance,
                no_draw_rate=no_draw,
                away_double_chance_rate=away_double_chance,
                home_double_chance_first_half_rate=home_double_chance_first,
                home_double_chance_second_half_rate=home_double_chance_second,
                no_draw_first_half_rate=no_draw_first,
                no_draw_second_half_rate=no_draw_second,
                away_double_chance_first_half_rate=away_double_chance_first,
                away_double_chance_second_half_rate=away_double_chance_second,
                odd=odd,
                even=even,
                odd_first=odd_first,
                odd_second=odd_second,
                even_first=even_first,
                even_second=even_second,
                correct_score10=correct_score10,
                correct_score20=correct_score20,
                correct_score21=correct_score21,
                correct_score30=correct_score30,
                correct_score31=correct_score31,
                correct_score32=correct_score32,
                correct_score40=correct_score40,
                correct_score41=correct_score41,
                correct_score00=correct_score00,
                correct_score11=correct_score11,
                correct_score22=correct_score22,
                correct_score33=correct_score33,
                correct_score01=correct_score01,
                correct_score02=correct_score02,
                correct_score12=correct_score12,
                correct_score03=correct_score03,
                correct_score13=correct_score13,
                correct_score23=correct_score23,
                correct_score04=correct_score04,
                correct_score14=correct_score14,
                home_home=home_home,
                home_draw=home_draw,
                home_away=home_away,
                draw_home=draw_home,
                draw_draw=draw_draw,
                draw_away=draw_away,
                away_home=away_home,
                away_draw=away_draw,
                away_away=away_away,
                link=self._url,
            ),
        )
        result = asdict(
            ResultMatchInfo(
                home_scored=home_scored,
                away_scored=away_scored,
                home_first_half_scored=home_first_scored,
                home_second_half_scored=home_second_scored,
                away_first_half_scored=away_first_scored,
                away_second_half_scored=away_second_scored,
            ),
        )
        match_info.update(result)
        return match_info

    def _get_pages(self):
        self._results_page_full = self._get_page(self._results_url_full)
        self._amounts_page_full = self._get_page(self._amounts_url_full)
        self._results_page_first = self._get_page(self._results_url_first)
        self._results_page_second = self._get_page(self._results_url_second)
        self._amounts_page_first = self._get_page(self._amounts_url_first)
        self._amounts_page_second = self._get_page(self._amounts_url_second)
        self._both_page_full = self._get_page(self._both_url_full)
        self._both_page_first = self._get_page(self._both_url_first)
        self._both_page_second = self._get_page(self._both_url_second)
        self._handicap_page_full = self._get_page(self._handicap_url_full)
        self._handicap_page_first = self._get_page(self._handicap_url_first)
        self._handicap_page_second = self._get_page(self._handicap_url_second)
        self._double_chance_page_full = self._get_page(self._double_chance_url_full)
        self._double_chance_page_first = self._get_page(self._double_chance_url_first)
        self._double_chance_page_second = self._get_page(self._double_chance_url_second)
        self._odd_even_page_full = self._get_page(self._odd_even_url_full)
        self._odd_even_page_first = self._get_page(self._odd_even_url_first)
        self._odd_even_page_second = self._get_page(self._odd_even_url_second)
        self._correct_score_page = self._get_page(self._correct_score_url)
        self._halfs_page = self._get_page(self._halfs_url)

    def _get_page(self, url):
        self._browser.get(url)
        time.sleep(0.01)
        self._browser.refresh()
        return BeautifulSoup(self._browser.page_source, 'html.parser')

    def _extract_season(self, date):
        return date.split('.')[-1]

    def _extract_country_league(self) -> tuple:
        split = self._results_url_full.split('/')
        return split[4], split[5]

    def _extract_date(self) -> tuple:
        """Получает дату матча."""
        date_class = str(self._results_page_full.find('p', class_='date'))
        raw_date = date_class.split('>')[1].split('<')[0]
        day_of_week = raw_date.split(',')[0]
        date = raw_date.split(',')[1]
        t = raw_date.split(',')[2].strip()
        date_without_spaces = ' '.join(date.split())
        for key in months.keys():
            if key in date_without_spaces:
                date_without_spaces = date_without_spaces.replace(key, months[key])
        date_without_spaces = date_without_spaces.replace(' ', '.')
        return day_of_week, date_without_spaces, t

    def _extract_teams(self) -> tuple:
        """Получает названия команд."""
        title = str(self._results_page_full.title)
        teams = title.split('e>')[1].split('Bet')[0]
        team_1, team_2 = teams.split('-')
        return team_1.strip(), team_2.strip()

    def _extract_home_draw_away(self, page) -> list:
        """Получает коэффициенты на исходы."""
        aver = page.find('tr', class_='aver')
        coefs = aver.find_all('td', class_='right')
        home_draw_away = []
        for coef in coefs:
            home_draw_away.append(str(coef).split('>')[1].split('<')[0])
        results = []
        for elem in home_draw_away:
            try:
                results.append(float(elem))
            except ValueError:
                logging.warning(home_draw_away)
                results.append(0)
        return results

    def _extract_double_chance(self, page) -> list:
        """Получает коэффициенты на исходы."""
        aver = page.find('tr', class_='aver')
        coefs = aver.find_all('td', class_='right')
        double_chances = []
        for coef in coefs:
            double_chances.append(str(coef).split('>')[1].split('<')[0])
        results = []
        for elem in double_chances:
            try:
                results.append(float(elem))
            except ValueError:
                logging.warning(double_chances)
                results.append(0)
        return results

    @decorator
    def _extract_over_under(self, page, total: str) -> tuple:
        amount = str(page).split(total)[1]
        amount = amount.split('text">')
        return amount[2].split('<')[0], amount[1].split('<')[0]

    @decorator
    def _extract_handicap(self, page, handicap: str) -> tuple:
        amount = str(page).split(handicap)[1]
        amount = amount.split('text">')
        return amount[2].split('<')[0], amount[1].split('<')[0]

    def _extract_correct_score(self, page, correct_score: str) -> float:
        try:
            amount = str(page).split(correct_score)[1]
            amount = amount.split('text~2">')
            return float(amount[1].split('<')[0])
        except IndexError:
            return 0

    def _extract_halfs(self, page, halfs: str) -> float:
        try:
            amount = str(page).split(halfs)[1]
            amount = amount.split('text~2">')
            return float(amount[1].split('<')[0])
        except IndexError:
            return 0

    def _extract_both(self, page) -> list:
        """Получает коэффициенты на обе забьют."""
        aver = page.find('tr', class_='aver')
        coefs = aver.find_all('td', class_='right')
        both = []
        for coef in coefs:
            both.append(str(coef).split('>')[1].split('<')[0])
        results = []
        for elem in both:
            try:
                results.append(float(elem))
            except ValueError:
                logging.warning(both)
                results.append(0)
        return results
    
    def _extract_odd_even(self, page) -> list:
        """Получает коэффициенты на обе забьют."""
        aver = page.find('tr', class_='aver')
        coefs = aver.find_all('td', class_='right')
        both = []
        for coef in coefs:
            both.append(str(coef).split('>')[1].split('<')[0])
        results = []
        for elem in both:
            try:
                results.append(float(elem))
            except ValueError:
                logging.warning(both)
                results.append(0)
        return results

    def _extract_result(self, page):
        """Получает результат матча."""
        raw_result = str(page.find('p', class_='result'))
        full_time_raw_result = raw_result.split('<strong>')[1].split('</strong>')[0].split(':')
        full_time_result = [int(goals) for goals in full_time_raw_result]
        half_times_raw_result = raw_result.split('strong> (')[1].split(')</p>')[0]
        first_time_raw_result, second_time_raw_result = half_times_raw_result.split(', ')
        first_time_result = [int(goals) for goals in first_time_raw_result.split(':')]
        second_time_result = [int(goals) for goals in second_time_raw_result.split(':')]
        return full_time_result[0], full_time_result[1], first_time_result[0], first_time_result[1], second_time_result[0], second_time_result[1]
