import time

from bs4 import BeautifulSoup


class ByLeagueLinksParser:

    def __init__(self, browser, url):
        self._browser = browser
        self._url = url

    def get_url(self, num_page):
        return f'{self._url}/#/page/{num_page}'

    def get_links(self, filename):
        index = 1
        links = []
        while True:
            url = self.get_url(index)
            self._browser.get(url)
            time.sleep(0.1)
            index += 1
            soup = BeautifulSoup(self._browser.page_source, 'html.parser')

            soup = str(soup)

            if 'no matches can be displayed' in soup:
                break
            data = soup.split('name table-participant')

            for elem in data[1:]:
                if 'soccer/' in elem:
                    link = 'https://www.oddsportal.com/' + elem.split('href=\"/')[1].split('\">')[0]
                    links.append(link)

        with open(filename, 'w') as f:
            f.write('\n'.join(list(set(links))))
