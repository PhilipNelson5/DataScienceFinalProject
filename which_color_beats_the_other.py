#%%
from cards import *
from pickle_helper import *
from scrape import *
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
cards = make_all_cards_df()

#%%
filepaths = [
  'html/2020-06-01-2020-08-03.html', 'html/2020-08-03-2020-09-17.html',
  'html/2020-09-17-2020-09-28.html', 'html/2020-09-28-2020-10-12.html',
  'html/2020-10-12-20201-04-15.html'
]
filepath = filepaths[0]
matrix = scrape_metagame_matrix_filepath(filepath)
deck_urls = [v['link'] for v in matrix.values()]
decks = [scrape_deck_url(url) for url in deck_urls]
deck_dfs = [
  get_deck(cards, card_names, card_counts)
    for card_names, card_counts, _ in decks
]
deck_mana_costs = [mana_cost_deck(deck) for deck in deck_dfs]

#%%
deck_mana_costs


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