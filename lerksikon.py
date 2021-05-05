import requests
import concurrent.futures
from bs4 import BeautifulSoup
from tqdm import tqdm
import re

url = "https://www.makedonski.gov.mk/corpus"

html = requests.get(url).text
soup = BeautifulSoup(html, features="html5lib")
num_pages = soup.find_all('a', string=re.compile('Страна.*'))[0].text.strip().split(' ')[-1]

pages = range(2, num_pages)
vowels = ['а', 'е', 'и', 'о', 'у']

def get_words(page):
    html = requests.get(url + "?page=" + str(page)).text
    soup = BeautifulSoup(html, features="html5lib")

    for a in soup.find_all('strong'): # крв
        word = a.string
        if 'р' in word:
            index = word.find('р')
            if index > 0 and index < len(word) - 1:
                if word[index - 1] not in vowels and word[index + 1] not in vowels:
                    print(word[:index] + "е" + word[index:])

executor = concurrent.futures.ProcessPoolExecutor(2)
futures = [executor.submit(get_words, i) for i in pages]
kwargs = {
    'total': len(futures),
    'unit': 'nap',
    'unit_scale': True,
    'leave': True
}

for f in tqdm(concurrent.futures.as_completed(futures), **kwargs):
    pass
