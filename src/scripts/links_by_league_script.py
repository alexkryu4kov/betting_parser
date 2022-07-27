from selenium import webdriver

from src.main_data_parsers.links.by_league import ByLeagueLinksParser

GECKODRIVER_PATH = '../../geckodriver'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3163.100 Safari/537.36'
}
for key in headers:
    webdriver.DesiredCapabilities.FIREFOX['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]


league_name = 'france/national'
urls = [f'{league_name}-201{i}-201{i+1}' for i in range(6, 9)]
urls.extend([f'{league_name}-2019-2020', f'{league_name}-2020-2021', league_name])

for url in urls:
    full_url = f'https://www.oddsportal.com/soccer/{url}/results'
    name = league_name.replace('/', '-')
    browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
    parser = ByLeagueLinksParser(browser, full_url)
    parser.get_links(f'{name}_links.txt')
    try:
        print(url)
        browser.close()
    except Exception:
        print('браузер уже закрыт')
