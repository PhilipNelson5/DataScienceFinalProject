#%%
from bs4 import BeautifulSoup
import requests

#%%
def scrape_metagame_matrix_soup(soup):
    id = 'tablestats'
    table = soup.find_all(id=id)[0].find_all('li')
    deck_names = []
    for div in table[0].find_all('div', class_='name'):
        deck_names.append(div.text.lower())

    decks = {}
    for i, row in enumerate(table[1:-1]):
        divs = row.find_all('div')
        row_name = divs[0].find('div', class_='name').text.lower()
        stats = divs[0].find_all('div', class_='stats')
        decks[row_name] = {
            'matches': stats[0].find('span').text,
            'confidence_interval': stats[1].text,
            'link': divs[0].find('a')['href'],
            'rivals': {}
        }
        
        for j, col in enumerate(row.find_all('div', class_='color')):
            if i == j: continue
            col_name = deck_names[j]
            confidence_int2 = col.find('div', class_='dmatchr').text
            performance_meta = col.find('div', class_='dperf').text
            match_count = col.find('div', class_='dmatch').text
            decks[row_name]['rivals'][col_name] = {
                'confidence_interval': confidence_int2,
                'performance_meta': performance_meta,
                'match_count': match_count
            }

    return decks
        
def scrape_metagame_matrix_filepath(filepath):
    with open("metagame.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        return scrape_metagame_matrix_soup(soup)
    

#%%
def scrape_deck_soup(soup):
    lis = soup.find('ul', class_='sampledecklist').find_all('li')
    deck = []
    for li in lis[1:]:
        try:
            if 'sideboard' in li['class']: break
        except: pass

        # if 'sideboard' in li.attrs['class']: break
        if 'data-name' in li.attrs:
            name = li.attrs['data-name'].split('//')[0].strip().lower()
            count = li.attrs['data-qt']
            deck.append((name, count))
    return deck

def scrape_deck_url(url):
    r = requests.get(url)
    r.text
    soup = BeautifulSoup(r.text, 'html.parser')
    return scrape_deck_soup(soup)

#%%
if __name__ == "__main__":
#%%
    filepath = "metagame.html"
    matrix = scrape_metagame_matrix_filepath(filepath)
    print(matrix)

# %%
    url = 'https://mtgmeta.io/decks/19010'
    deck = scrape_deck_url(url)
    print(deck)