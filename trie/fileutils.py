#!/usr/bin/python
#util methods to create dictionary, all file reading methods are here
import re
import Trie
import sys

#Return the dictionary of length vs list of words corresponding to that length. 
#wordToBeLooked -> the word for which a dictionary need to be created
#Dictionary typically will have three enrties corresponding to keys, 
#len(wordToBeLooked), len(wordToBeLooked)-1, len(wordToBeLooked)+1
def getDictionary(wordToBeLooked):
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
	return dict

#returns dictionary of word vs list of all the words similar to it
def getSimilarWordDictionary():
	f = open('alice.txt','r')
	words = re.findall('\w+', f.read().lower())
	unique = list(set(words))
	#initializing the dictionary of length vs list of words corresponding to that length. 
	dict = {}
	minlen = 10000
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
	similarWords = {}
	trieMap = Trie.TrieMap()
	trieMap._init_(dict,minlen,maxlen)
	for key in unique:
		#travels in the tries and finds and return list of similar words
		wordList = trieMap.findSimilar(key)
		similarWords[key] = wordList

	return similarWords
