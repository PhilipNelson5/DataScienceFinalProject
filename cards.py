#%% imports
import json
import pandas as pd
import numpy as np

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
  df['name'] = df['name'].str.lower()
  return df
  
def get_deck(df, card_names, card_counts):
  deck = df[
    (df['name'].isin(card_names)) &
    (df['isReprint'].isna()) &
    # (df['setIsOnlineOnly'] == False) &
    (df['isPromo'].isna())
  ].drop_duplicates(subset=['name'])

  deck['count'] = np.zeros(len(deck))
  for name, count in zip(card_names, card_counts):
    deck.loc[deck.name == name, 'count'] = count

  return deck