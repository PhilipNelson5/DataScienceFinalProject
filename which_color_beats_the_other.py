#%%
from cards import *
from scrape import *
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
cards = make_all_cards_df()


#%%
filepath = "html/2020-06-01-2020-08-03.html"
matrix = scrape_metagame_matrix_filepath(filepath)
deck_urls = [v['link'] for v in matrix.values()]
decks = [scrape_deck_url(url) for url in deck_urls]
deck_dfs = [
  get_deck(cards, card_names, card_counts)
    for card_names, card_counts, _ in decks
]
#%%
deck_mana_costs = [mana_cost_deck(deck) for deck in deck_dfs]
#%%
deck_mana_costs = []
for i, deck in enumerate(deck_dfs):
  try:
    mana_cost_deck(deck)
  except:
    print(i)

#%%
deck_dfs[0][deck_dfs[0].name == 'expansion'].purchaseUrls.iloc[0]['tcgplayer']


#%%
url = 'https://mtgmeta.io/decks/19010'
url = 'https://mtgmeta.io/decks/1697'
card_names, card_counts, deck_price = scrape_deck_url(url)
print('price', deck_price)

deck = get_deck(cards, card_names, card_counts)
print('df size', len(deck), '| deck size', len(card_names))
print(missing_cards(deck, card_names))

mana_cost_deck(deck)

#%%
cards[cards.name == 'inspiring veteran']

card = cards[cards.name == 'goblin war wagon'].iloc[0]