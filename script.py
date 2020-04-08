import requests
from bs4 import BeautifulSoup
import json
import re

base_URL = 'https://ca.wiktionary.org/wiki/'
wordsDict = []
id_ = 1

with open('list.txt', 'r') as f:
    content = f.readlines()
    words = [ line.rstrip('\n') for line in content ]

for word in words: 
    try:       
        page = requests.get(base_URL + word)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            etimology_span = soup.find(text='Etimologia')
            etimology = etimology_span.parent.parent
            etimology = re.sub(r'\[[^()]*\]', '',etimology.text)
            etimology = re.sub(r'.*:', '', etimology).strip()
            #print(etimology)
        except:
            etimology = ''
            print('no etimology for '+word)
            pass
        for dl in soup.find_all("dl"): 
            dl.decompose()
        word_syllabe = soup.find(class_='Latn headword')
        #print(word_syllabe.text)
        word_type_soup = soup.find('h3')
        word_type = word_type_soup.find(class_='mw-headline')
        #print(word_type.text.lower())
        definitions = soup.find('ol')
        definition = definitions.find('li')
        definition = re.sub(r'\([^)]*\)', '',definition.text)
        definition = re.sub(r'\[[^()]*\]', '',definition).strip()
        #print(definition.text)
        #print("\n")
        word_entry = {
            'id': id_,
            'word': word,
            'syllabes': word_syllabe.text,
            'definition': definition,
            'wordtype': word_type.text.lower(),
            'synoyms': '',
            'etimology': etimology
            }
        wordsDict.append(word_entry)
        id_ = id_ + 1
    except:
        print('error '+word)
        pass

to_json = json.dumps(wordsDict)

with open('output.json', 'w',encoding='utf8') as write_file:
    json.dump(wordsDict, write_file, ensure_ascii=False)