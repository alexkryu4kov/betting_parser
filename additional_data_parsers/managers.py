import json

import requests
from bs4 import BeautifulSoup

with open('../data/indices.json', 'r') as f:
    indices = json.load(f)


def url(index):
    return f'https://www.transfermarkt.com/manchester-city/mitarbeiterhistorie/verein/{index}'


managers = []
for k, v in indices.items():
    print(k)
    page = requests.get(url(v), headers={'User-Agent': 'Custom'})

    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_='items')
    table2 = table.find('tbody')
    table3 = table2.find_all('tr')
    for row in table3:
        try:
            d = dict()
            d['Team'] = k
            inline = row.find(class_='inline-table')
            d['Name'] = str(inline).split("title=\"")[1].split("\"/><")[0]
            d['Birthday'] = str(inline).split("</td></tr><tr><td>")[1].split("</td></tr>")[0]
            zentrierts = row.find_all(class_='zentriert')
            d['Country'] = str(zentrierts[0]).split("title=\"")[1].split("\"/><")[0]
            d['Start'] = str(zentrierts[1]).split('">')[1].split('</')[0]
            d['End'] = str(zentrierts[2]).split('">')[1].split('</')[0]
            managers.append(d)
        except Exception:
            continue

with open('../data/managers.json', 'w') as f:
    json.dump(managers, f)
