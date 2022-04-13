from selenium import webdriver
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from links import ByLeagueLinksParser
from parser import Parser

GECKODRIVER_PATH = 'geckodriver'

executor = ThreadPoolExecutor(10)


def scrape(url, *, loop):
    loop.run_in_executor(executor, scraper, url)


def scraper(link):
    browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
    parser = Parser(browser, link)
    try:
        match_info = parser.get_match_info()
        print(match_info)
        with open('england_championship_match_data.txt', 'a') as f:
            f.write(str(match_info) + '\n')
    except Exception as e:
        print(e)
    try:
        print(link)
        browser.close()
    except Exception:
        print('браузер уже закрыт')



headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3163.100 Safari/537.36'
}
for key in headers:
    webdriver.DesiredCapabilities.FIREFOX['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]


league_name = 'england/premier-league'
"""
urls = [f'{league_name}-201{i}-201{i+1}' for i in range(6, 9)]
urls.extend([f'{league_name}-2019-2020', f'{league_name}-2020-2021', league_name])
"""
urls = [league_name]

for url in urls:
    full_url = f'https://www.oddsportal.com/soccer/{url}/results'
    league_url = url.replace('/', '-')
    browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
    parser = ByLeagueLinksParser(browser, full_url)
    parser.get_links(f'{league_url}_links.txt')

"""
browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
league_url = 'england-championship'
with open(f'{league_url}_links.txt', 'r') as f:
    links = f.read()

with open(f'{league_url}_match_data.txt', 'a') as f:
    for link in links.split('\n'):
        parser = Parser(browser, link)
        try:
            match_info = parser.get_match_info()
        except Exception as e:
            print(e)
            continue
        print(match_info)
        f.write(str(match_info) + '\n')

try:
    browser.close()
except Exception:
    print('браузер уже закрыт')
league_name = 'test_future'
with open(f'{league_name}_links.txt', 'r') as f:
    links = f.read()

loop = asyncio.get_event_loop()
for link in links.split('\n'):
    scrape(link, loop=loop)
loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
"""
