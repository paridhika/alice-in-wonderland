#!/usr/bin/python
import re
import Trie
import sys
from nltk.corpus import wordnet


wordToBeLooked = sys.argv[1]
f = open('alice.txt','r')
words = re.findall('\w+', f.read().lower())
unique = list(set(words))
dict = {}
minlen = len(wordToBeLooked)-1
maxlen = len(wordToBeLooked)+1

for word in unique:
	if len(word) >= minlen and len(word) <= maxlen:
		if len(word) in dict:
			dict[len(word)].append(word)
		else:
			dict[len(word)] = []
			dict[len(word)].append(word)

synonyms = []
for i,j in enumerate(wordnet.synsets(wordToBeLooked)):
	for word in j.lemma_names:
		if word not in synonyms:
			synonyms.append(word)

trieMap = Trie.TrieMap()
trieMap._init_(dict,minlen,maxlen)
wordList = trieMap.findSimilar(wordToBeLooked)	


sensibleMatchings = []
for word in wordList:
	if word in synonyms:
		sensibleMatchings.append(word)

print sensibleMatchings
