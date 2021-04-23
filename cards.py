#%% imports
import json
import numpy as np
import pandas as pd

#%% functions
def get_json(filepath):
  with open(filepath, encoding='utf-8') as f:
    return json.load(f)


def make_all_cards_df():
  all_json = get_json('datasets/all_cards.json')
  cards = []
  for _, v in all_json.items():
    for card in v['cards']:
      card['releaseDate'] = v['releaseDate']
      card['setName'] = v['name']
      card['setType'] = v['type']
      card['setIsOnlineOnly'] = v['isOnlineOnly']
      card['setBaseSetSize'] = v['baseSetSize']
      card['setTotalSetSize'] = v['totalSetSize']

  for _, v in all_json.items():
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
    deck.loc[deck.name == name, 'count'] = int(count)

  return deck


def missing_cards(deck, card_names):
  missing = []
  for card_name in card_names:
    if len(deck[deck.name == card_name]) == 0:
      missing.append(card_name)
  return missing


# [wild, white, blue, black, red, green]
X = 0; W = 1; U = 2; B = 3; R = 4; G = 5
def mana_cost_card(card):
  s = str(card.manaCost)
  cost = np.zeros(6)
  if s == 'nan': return cost
  for i in range(len(s)):
    c = s[i]
    if c == 'W': cost[W] += 1
    elif c == 'U': cost[U] += 1
    elif c == 'B': cost[B] += 1
    elif c == 'R': cost[R] += 1
    elif c == 'G': cost[G] += 1
    elif c == 'X': pass
    else: 
      try: cost[X] += int(c)
      except: pass
  return cost


def mana_cost_deck(deck):
  cost = np.zeros(6)
  for _, card in deck.iterrows():
    cost += mana_cost_card(card) * card['count']
  return cost


# [wild, white, blue, black, red, green]
def mana_colors_card(card):
  cost = mana_cost_card(card)
  return np.array([1 if x > 0 else 0 for x in cost])


def mana_colors_deck(deck):
  colors = np.zeros(6)
  for _, card in deck.iterrows():
    colors += mana_colors_card(card) * card['count']
  return colors