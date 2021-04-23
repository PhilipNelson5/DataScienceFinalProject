#%% imports
from datetime import datetime
import json
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

#%% functions
def get_json(filepath):
  with open(filepath, encoding='utf-8') as f:
    return json.load(f)

def save_json(data, filepath):
  with open(filepath, 'w') as fp:
    json.dump(data, fp)

def make_all_cards_df():
  all_json = get_json('datasets/all_cards.json')
  cards = []
  for k,v in all_json.items():
    for card in v['cards']:
      card['releaseDate'] = v['releaseDate']
      card['setName'] = v['name']
      card['setType'] = v['type']
      card['setIsOnlineOnly'] = v['isOnlineOnly']
      card['setBaseSetSize'] = v['baseSetSize']
      card['setTotalSetSize'] = v['totalSetSize']

  for k,v in all_json.items():
    cards.extend(v['cards'])

  df = pd.DataFrame.from_dict(cards)
  df['releaseDate'] = pd.to_datetime(df['releaseDate'], format='%Y-%m-%d')
  return df

# standard_json = get_json('kaggledata/Standard.json')
# standard_cards_json = get_json('kaggledata/StandardCards.json')
# all_json = get_json('datasets/all_cards.json')

#%%
df = make_all_cards_df()
# df[(df['isReprint'].isna()) & (df['setIsOnlineOnly'] == False) & (df['type'].str.contains('Land'))]

#%%
df[(df['isReprint'].isna()) & (df['name'] == 'Castle Vantress')]

#%% list all types
types = set()
for k in all_json.keys():
  types.add(all_json[k]['type'])
print(types)

#%%
standard = ['KLD', 'ZEN', 'TBTH']
# print(all_json['10E']['cards'][0].pop('foreignData', None))
for k,v in all_json['KLD'].items():
  display(k, v)

#%%
l = [datetime.strptime(all_json[k]['releaseDate'], '%Y-%m-%d') for k in all_json.keys()]
l.sort()
l

#%% remove foreign data
all_json = get_json('kaggledata/AllPrintings.json')

#%%
for k in all_json.keys():
  print(k)


#%%
for k in all_json.keys():
  print(k)
  for card in all_json[k]['cards']:
    card.pop('foreignData', None)
save_json(all_json, 'datasets/all_cards.json')

#%%
