#!/usr/bin/python
import re
import Trie
import sys
from nltk.corpus import wordnet

f = open('alice.txt','r')
words = re.findall('\w+', f.read().lower())
unique = list(set(words))
dict = {}
minlen = 1000
maxlen = 0
for word in unique:
	if len(word) in dict:
		dict[len(word)].append(word)
	else:
		dict[len(word)] = []
		dict[len(word)].append(word)
	if len(word) > maxlen:
		maxlen = len(word)
	if len(word) < minlen:
		minlen = len(word)



synonyms = []
wordToBeLooked = sys.argv[1]
for i,j in enumerate(wordnet.synsets(wordToBeLooked)):
	for word in j.lemma_names:
		if word not in synonyms:
			synonyms.append(word)

trieMap = Trie.TrieMap()
trieMap._init_(dict,min,max)
wordList = trieMap.findSimilar(wordToBeLooked)	


sensibleMatchings = []
for word in wordList:
	if word in synonyms:
		sensibleMatchings.append(word)

print sensibleMatchings
