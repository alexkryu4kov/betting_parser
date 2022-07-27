from datetime import date

from selenium import webdriver

from src.main_data_parsers.links.by_date import ByDateLinksParser

GECKODRIVER_PATH = '../../geckodriver'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3163.100 Safari/537.36'
}
for key in headers:
    webdriver.DesiredCapabilities.FIREFOX['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]

browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
parser = ByDateLinksParser(browser)
parser.get_links(date(2022, 7, 27))
try:
    browser.close()
except Exception:
    print('браузер уже закрыт')
