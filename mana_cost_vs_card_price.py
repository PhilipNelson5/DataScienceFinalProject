#%%
from cards import *
from matplotlib import pyplot as plt
from scipy import stats

pd.set_option('display.max_columns', None)
cards = make_all_cards_df()

#%%
df = cards[
    (cards['isReprint'].isna()) &
    (cards['isPromo'].isna())
  ].drop_duplicates(subset=['name']).dropna(subset=['prices'])
x = []
y = []
for _, card in df.iterrows():
    try:
        y.append(list(card.prices['mtgo'].values())[0])
        x.append(card.convertedManaCost)
    except: pass


#%%
r, p = stats.pearsonr(x,y)
rs = round(r, 2)
ps = "{:.2e}".format(p)
plt.scatter(x,y)
plt.xlabel('Total Mana Cost (mana)')
plt.ylabel('Card Price ($)')
plt.title(f'Card Price vs Total Mana Cost\nr={rs}, p={ps}')
plt.tight_layout()
plt.savefig('images/card-cost-vs-mana-cost.pdf')