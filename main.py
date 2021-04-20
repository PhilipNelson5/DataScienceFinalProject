#%%
from cards import make_all_cards_df
from scrape import *

#%%
cards = make_all_cards_df()
print(cards)

#%%
filepath = "metagame.html"
matrix = scrape_metagame_matrix_filepath(filepath)
print(matrix)

# %%
url = 'https://mtgmeta.io/decks/19010'
deck = scrape_deck_url(url)
print(deck)