import requests
from bs4 import BeautifulSoup
import json

URL = 'https://ca.wiktionary.org/wiki/atzucac'
wordsDict = []
id_ = 1

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
etimology_span = soup.find(text='Etimologia')
etimology = etimology_span.parent.parent
print(etimology.text)
for dl in soup.find_all("dl"): 
    dl.decompose()
word_syllabe = soup.find(class_='Latn headword')
print(word_syllabe.text)
word_type_soup = soup.find('h3')
word_type = word_type_soup.find(class_='mw-headline')
print(word_type.text.lower())
definitions = soup.find('ol')
definition = definitions.find('li')
print(definition.text)

word_entry = {'id': id_, 'word': word_syllabe.text, 'definition': definition.text, 'wordtype': word_type.text.lower(), 'synoyms': ''}
