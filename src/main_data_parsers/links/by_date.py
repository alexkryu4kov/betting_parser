import time
from datetime import date

from bs4 import BeautifulSoup


class ByDateLinksParser:

    def __init__(self, browser):
        self._browser = browser

    def get_url(self, day: date):
        str_date = day.strftime('%Y%m%d')
        return f'https://www.oddsportal.com/matches/soccer/{str_date}/'

    def get_links(self, day: date):
        links = []
        url = self.get_url(day)
        self._browser.get(url)
        time.sleep(0.1)
        soup = BeautifulSoup(self._browser.page_source, 'html.parser')

        data = str(soup).split('name table-participant')

        for elem in data[1:]:
            if 'soccer/' in elem:
                link = 'https://www.oddsportal.com/' + elem.split('href=\"/')[1].split('\">')[0]
                links.append(link)

        with open(f'../{day.strftime("%Y%m%d")}_links.txt', 'a') as f:
            f.write('\n'.join(list(set(links))))
