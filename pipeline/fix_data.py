import pandas as pd
from dateutil import parser

all_england = pd.read_csv('../all_england_v2.8.csv')

with open('../all-england_links.txt', 'r') as f:
    links = f.read()
links = links.split('\n')

parsed_links = all_england['link'].values
print(len(parsed_links))
print(len(links))
not_parsed_links = []

for link in links:
    if link not in parsed_links:
        not_parsed_links.append(link)

with open('../not_parsed_links.txt', 'w') as f:
    f.write('\n'.join(list(set(not_parsed_links))))
