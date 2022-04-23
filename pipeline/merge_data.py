import pandas as pd

all_england = pd.read_csv('../all_england_v2.6.csv')
league_one = pd.read_csv('../england-league-two_v1.7.csv')

full = pd.concat([all_england, league_one])

full.to_csv('all_england_v2.7.csv', index=False)
