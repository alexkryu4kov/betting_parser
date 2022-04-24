import json

import pandas as pd

from pipeline.config import LEAGUE_NAME


def save_to_csv(filename):
    with open(f'../{filename}_match_data.txt', 'r') as f:
        data = f.read()

    new_data = []
    for elem in data.split('\n'):
        string = elem.replace("'", "\"")
        try:
            new_data.append(json.loads(string))
        except Exception:
            pass

    dataframe = pd.DataFrame(new_data)
    dataframe.to_csv(f'../{filename}.csv', index=False)


save_to_csv(LEAGUE_NAME)
