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

#%%
meta_performance = []
for matrix in matrixs:
    for v in matrix.values():
        meta_performance.append(float(v['confidence_interval'].split(' ')[0].replace('%','')))

x = [meta for i, meta in enumerate(meta_performance) if i not in bad]
y = [price for i, price in enumerate(prices) if i not in bad]

r, p = stats.pearsonr(x,y)
rs = round(r, 2)
ps = "{:.2e}".format(p)
plt.scatter(x,y)
plt.xlabel('Global Meta Performance')
plt.ylabel('Deck Price ($)')
plt.title(f'Deck Price vs Meta Performance\nr={rs}, p={ps}')
plt.tight_layout()
plt.savefig('images/deck-cost-vs-meta-performance.pdf')