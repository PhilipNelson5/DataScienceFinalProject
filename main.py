#%%
from cards import make_all_cards_df, get_deck
from scrape import *
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
cards = make_all_cards_df()


#%%
filepath = "html/metagame.html"
matrix = scrape_metagame_matrix_filepath(filepath)
print(matrix)

#%%
url = 'https://mtgmeta.io/decks/19010'
url = 'https://mtgmeta.io/decks/1697'
deck = scrape_deck_url(url)
card_names, card_counts = map(list, zip(*deck))

deck = get_deck(cards, card_names, card_counts)
print('df size', len(deck), '| deck size', len(card_names))

for card_name in card_names:
    if len(deck[deck.name == card_name]) == 0:
        print(card_name)

#%%
# [wild, white, blue, black, red, green]
X = 0; W = 1; U = 2; B = 3; R = 4; G = 5
def manaCostCard(card):
    s = str(card.manaCost)
    cost = np.zeros(6)
    if s == 'nan': return cost
    for i in range (1, len(s), 3):
        c = s[i]
        if c == 'W': cost[W] += 1
        elif c == 'U': cost[U] += 1
        elif c == 'B': cost[B] += 1
        elif c == 'R': cost[R] += 1
        elif c == 'G': cost[G] += 1
        elif c == 'X': pass
        else: cost[X] += int(c)
    return cost

def manaCostDeck(deck):
    cost = np.zeros(6)
    for _, card in deck.iterrows():
        cost += manaCostCard(card) * int(card['count'])
    return cost

manaCostDeck(deck)