from bs4 import BeautifulSoup  
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from InvertedIndex import InvertedIndex
from Tries import Tries

MINIMUM_CHR = 2
MAP_PATH = "file_link_map.json"
class SearchEngine(object):
    inverted_index = InvertedIndex()

    def buildTries(self):
        f = open(MAP_PATH, "r") 
        file_link_map = json.loads(f.readlines()[0]) 

        # filter stopword and punctuation
        stop_words = set(stopwords.words('english'))
        stop_words.update(string.punctuation)

        for filename in file_link_map:
            f = open(filename)
            soup = BeautifulSoup(f.read(), 'html.parser')
            [script.extract() for script in soup.findAll('script')]
            [style.extract() for style in soup.findAll('style')]
#             print file_link_map[filename]
            words = word_tokenize(soup.get_text())
            for word in words:
                if word.lower() not in stop_words and len(word) > MINIMUM_CHR and word.isdigit()==False:
                        # build compressed trie tree
                        word = word.lower().strip()
                        self.inverted_index.put(word, file_link_map[filename])
#                         print word.lower().strip()
        f.close()
        
    def search(self, key):
        return self.inverted_index.get(key)
        
        
# se = SearchEngine()
# se.buildTries()
# print se.inverted_index.get("algorithm")

