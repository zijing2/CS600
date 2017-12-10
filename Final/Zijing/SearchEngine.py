from bs4 import BeautifulSoup  
import json
import nltk
import re
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
            # remove the words containing punctuation
            words = [i for i in words if all(j not in string.punctuation for j in i)]
            
            for word in words:
                if word.lower() not in stop_words and len(word) > MINIMUM_CHR and word.isdigit()==False:
                        # build compressed trie tree
                        try:
                            # remove the words whcih can't encode to ascII
                            word = word.lower().strip().encode('ascII')
                        except:
#                             print word
                            a = 1
                        else:
                            self.inverted_index.put(word, file_link_map[filename])
#                             print word.lower().strip()
        f.close()
        
    def search(self, key):
        if self.inverted_index.get(key) == None:
            return {}
        else:
            return self.inverted_index.get(key)
    
    def getRecomendKey(self, string):
        return self.inverted_index.getRecommendKey(string) 
        
        
# se = SearchEngine()
# se.buildTries()
# keywords = ["algorithm", "leetcode", "bit"]
# keylist = []
# odict = {}
# for key in keywords:
#     result = se.search(key)
#     if result:
#         result.pop('key', None)
#         keylist.append(result.keys())
#         for r in result:
#             if odict.has_key(r):
#                 odict[r] = odict[r] + result[r]
#             else:
#                 odict[r] = result[r]
#     else:
#         keylist.append(result.keys())
        
# intersetion = None
# for kl in keylist:
#     if intersetion == None:
#         intersetion = set(kl)
#     else:
#         intersetion = set(intersetion) & set(kl)
        
# output = {}

# for sub_intersetion in intersetion:
#     sub = sub_intersetion.encode("utf-8")
#     output[sub] = odict[sub]

# print output
    

