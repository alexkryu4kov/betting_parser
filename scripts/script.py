from selenium import webdriver
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from main_data_parsers.parser import Parser

GECKODRIVER_PATH = '../geckodriver'

executor = ThreadPoolExecutor(10)


def scrape(url, league, *, loop):
    loop.run_in_executor(executor, scraper, url, league)


def scraper(link, league):
    browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
    parser = Parser(browser, link)
    try:
        match_info = parser.get_match_info()
        print(match_info)
        with open(f'../{league}_match_data.txt', 'a') as f:
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


league_name = 'italy-serie-a'
with open(f'../{league_name}_links.txt', 'r') as f:
    links = f.read()

loop = asyncio.get_event_loop()
for link in links.split('\n'):
    scrape(link, league_name, loop=loop)
loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
