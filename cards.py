#%% imports
import json
import pandas as pd

#%% functions
def get_json(filepath):
  with open(filepath, encoding='utf-8') as f:
    return json.load(f)

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