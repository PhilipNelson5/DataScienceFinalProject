#%%
from cards import *
from pickle_helper import *
from scrape import *
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

#%%
cards = make_all_cards_df()

decks = load('datasets/all_decks.pkl')
prices = load('datasets/all_prices.pkl')
bad = load('datasets/all_bad.pkl')
matrixs = load('datasets/all_matrixs.pkl')
meta_performance = load('datasets/all_meta_performance.pkl')
deck_urls = load('datasets/all_deck_urls.pkl')
deck_names = load('datasets/all_deck_names.pkl')

#%%
deck_mana_costs = [mana_cost_deck(deck) for deck in decks]
deck_mana_colors = [mana_colors_deck(deck) for deck in decks]

#%%
for i in range(len(decks)):
  if i not in bad:
    print(i, (deck_mana_colors[i]))

#%%
deck_colors = [np.argmax(deck[1:]) for deck in deck_mana_colors]

x = np.zeros(5)
for i in range(len(decks)):
  # if i not in bad:
    x[deck_colors[i]] += 1
    
plt.bar(['white', 'blue', 'black', 'red', 'green'], x)
plt.xlabel('Deck Color')
plt.ylabel('Count')
plt.title('Distribution of Deck Colors')
plt.tight_layout()
# plt.savefig('images/deck-color-distribution.pdf')

#%% which color wins more often
W = 0; U = 1; B = 2; R = 3; G = 4
def get_deck(name):
  i = deck_names.index(name)
  return decks[i]

def get_color(deck):
  colors = mana_colors_deck(deck)
  return np.argmax(colors[1:])
  
wins = np.zeros((5,5))
plays = np.zeros((5,5))

for matrix in matrixs:
  for k, v in matrix.items():
    deck_name = k
    deck_deck = get_deck(deck_name)
    deck_color = get_color(deck_deck)
    deck_total_matches = int(v['matches'])
    for rival in v['rivals']:
      rival_name = rival
      rival_deck = get_deck(rival_name)
      rival_color = get_color(rival_deck)
      if deck_color == rival_color: continue
      meta_performance = v['rivals'][rival]['performance_meta']
      match_count = v['rivals'][rival]['match_count']
      win_count = meta_performance * match_count / 100
      wins[deck_color][rival_color] += win_count
      plays[deck_color][rival_color] += win_count
      plays[rival_color][deck_color] += win_count

#%%
# total = sum(sum(wins))
# win_average = wins / total

# win_average = []
# for i, row in enumerate(wins):
#   win_average.append(row / (np.sum(wins, axis=1)[i]))# + np.sum(wins, axis=1)[i]))

win_average = np.zeros((5,5))
for i, row in enumerate(wins):
  for j, col in enumerate(row):
    win_average[i][j] = col / plays[i][j]

labels = ['white', 'blue', 'black', 'red', 'green']
sns.heatmap( win_average , cmap = 'coolwarm', xticklabels=labels, yticklabels=labels)
plt.title('Deck Color Win Rate (%)\nrow beats column')
plt.tight_layout()
plt.savefig('images/deck-color-win-rate.pdf')

#%%
labels = ['white', 'blue', 'black', 'red', 'green']
sns.heatmap( wins , cmap = 'coolwarm', xticklabels=labels, yticklabels=labels)
plt.title('Deck Color Play Count\nrow beats column')
plt.tight_layout()
plt.savefig('images/deck-color-play-count.pdf')