#%%
from cards import *
from scrape import *
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
cards = make_all_cards_df()


#%%
filepath = "html/metagame.html"
matrix = scrape_metagame_matrix_filepath(filepath)
print(matrix)

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
price_deck(deck) 