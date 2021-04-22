#%%
from matplotlib import pyplot as plt
import pickle
from scipy import stats

def save(obj, file_name):
    with open(file_name, 'wb') as fp:
        pickle.dump(obj, fp)

def load(file_name):
    with open(file_name, 'rb') as fp:
        obj = pickle.load(fp)
    return obj

#%%
decks = load('datasets/all_decks.pkl')
prices = load('datasets/all_prices.pkl')
bad = load('datasets/all_bad.pkl')
matrixs = load('datasets/all_matrixs.pkl')
meta_performance = load('datasets/all_meta_performance.pkl')

#%%
x = []
for i, deck in enumerate(decks):
    if i in bad: continue
    x.append(0)
    for _, card in deck.iterrows():
        x[-1] += card.convertedManaCost * card['count']

y = [price for i, price in enumerate(prices) if i not in bad]

r, p = stats.pearsonr(x,y)
rs = round(r, 2)
ps = "{:.2e}".format(p)
plt.scatter(x,y)
plt.xlabel('Total Mana Cost (mana)')
plt.ylabel('Deck Price ($)')
plt.title(f'Deck Price vs Total Mana Cost\nr={rs}, p={ps}')
plt.tight_layout()
# plt.savefig('images/deck-cost-vs-mana-cost.pdf')