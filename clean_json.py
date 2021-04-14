#%% imports
from datetime import datetime
import json
import pandas as pd

#%% json load/save
def get_json(filepath):
  with open(filepath, encoding='utf-8') as f:
    return json.load(f)

def save_json(data, filepath):
  with open(filepath, 'w') as fp:
    json.dump(data, fp)

# standard_json = get_json('kaggledata/Standard.json')
# standard_cards_json = get_json('kaggledata/StandardCards.json')
all_json = get_json('datasets/all_cards.json')

#%%
# print(all_json['10E']['cards'][0].pop('foreignData', None))
for k in all_json.keys():
  print(all_json[k]['releaseDate'])
  
#%%
l = [datetime.strptime(all_json[k]['releaseDate'], '%Y-%m-%d') for k in all_json.keys()]
l.sort()
l

#%% remove foreign data
all_json = get_json('kaggledata/AllPrintings.json')
for k in all_json.keys():
  print(k)
  for card in all_json[k]['cards']:
    card.pop('foreignData', None)
save_json(all_json, 'datasets/all_cards.json')

#%%
pd.DataFrame.from_dict(standard_cards_json)