#!/usr/bin/python
#solution for finding correlated words
import re
import Trie
import sys
import fileutils
from nltk.corpus import wordnet


wordToBeLooked = sys.argv[1]
minlen = len(wordToBeLooked)-1
maxlen = len(wordToBeLooked)+1

#Getting dictionary of length vs all words of the length present in the text file
dict = fileutils.getDictionary(wordToBeLooked)
synonyms = []

#finding all synonyms of the input word in wordnet
for i,j in enumerate(wordnet.synsets(wordToBeLooked)):
	for word in j.lemma_names:
		if word not in synonyms:
			synonyms.append(word)

trieMap = Trie.TrieMap()
trieMap._init_(dict,minlen,maxlen)
#Getting list of words similar to the input string
wordList = trieMap.findSimilar(wordToBeLooked)	


sensibleMatchings = []
#Taking intersection of list of synonyms and list of similar words
for word in wordList:
	if word in synonyms:
		sensibleMatchings.append(word)
#printing result
print sensibleMatchings
