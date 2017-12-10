# Search Engine

Implement the simplified Search Engine described in Section 23.5.4 for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.

## directory structure
.
├── InvertedIndex.ipynb -- a dictionery implemented by Trie(runs in Jupyter)
├── InvertedIndex.py -- a dictionery implemented by Trie
├── InvertedIndex.pyc -- python compile file
├── README.md 
├── SearchEngine.ipynb 
├── SearchEngine.py -- main class 
├── SearchEngine.pyc
├── Tries.ipynb
├── Tries.py -- tries structure index
├── Tries.pyc
├── UserInterface.ipynb
├── UserInterface.py -- GUI
├── Zijing -- spider program
├── file_link_map.json -- a mapping of html file and its link
├── input -- the website used to be the input of search engine
├── scrapy.cfg -- spider config 
├── templates -- GUI templates

## dependencies
1. python2.7
2. Scrapy (pip install scrapy)
3. beatifulsoup (pip install beautifulsoup4)
4. nltk (pip install nltk)
5.

## deploying
1. download or check out the project
2. cd ./Zijing(in the 1st level of the directory, which is the same level as input directory); 
3. scrapy crawl Zijing --nolog(You will discover some new files in the input directory) 
4. python UserInterface.py
5. access http://127.0.0.1:8886/


