#%%
from cards import *
from scrape import *
from time import sleep
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
cards = make_all_cards_df()


#%%
filepaths = [
    '2019-10-04-2019-10-25.html', '2019-10-25-2019-11-18.html',
    '2019-11-18-202006-01.html', '2020-06-01-2020-08-03.html',
    '2020-08-03-2020-09-17.html', '2020-09-17-2020-09-28.html',
    '2020-09-28-2020-10-12.html', '2020-10-12-20201-04-15.html'
]
matrixs = []
deck_urls = []
for filepath in filepaths:
    matrixs.append(scrape_metagame_matrix_filepath('html/'+filepath))
    deck_urls += [v['link'] for v in matrixs[-1].values()]

#%%
decks = []
prices = []
bad = []
for i, url in enumerate(deck_urls):
    card_names, card_counts, deck_price = scrape_deck_url(url)
    deck = get_deck(cards, card_names, card_counts)
    missing = missing_cards(deck, card_names)
    if len(missing) != 0:
        bad.append(i)
        print(len(missing), url)

    decks.append(deck)
    prices.append(deck_price)
    sleep(1)
    
#%%
print(len(decks) - len(bad))
print(len(decks))

#%%
import pickle
def save(obj, file_name):
    with open(file_name, 'wb') as fp:
        pickle.dump(obj, fp)

def load(file_name):
    with open(file_name, 'rb') as fp:
        obj = pickle.load(fp)
    return obj

save(decks, 'datasets/all_decks.pkl')
save(prices, 'datasets/all_prices.pkl')
save(bad, 'datasets/all_bad.pkl')
save(matrixs, 'datasets/all_matrixs.pkl')

#%%
decks = load('datasets/all_decks.pkl')
prices = load('datasets/all_prices.pkl')
bad = load('datasets/all_bad.pkl')
matrixs = load('datasets/all_matrixs.pkl')