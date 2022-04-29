import pandas as pd

from config import CURRENT_VERSION, LEAGUE_NAME


all_england = pd.read_csv(f'../all_england_v2.{CURRENT_VERSION}.csv')
new_league = pd.read_csv(f'../{LEAGUE_NAME}_v1.7.csv')

new_league.drop('year', axis=1, inplace=True)

full = pd.concat([all_england, new_league])

full.to_csv(f'../all_england_v2.{CURRENT_VERSION+1}.csv', index=False)

print(f'Saved to ../all_england_v2.{CURRENT_VERSION+1}.csv')
