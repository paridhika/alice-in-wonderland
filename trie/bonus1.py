#!/usr/bin/python
import re
import collections
import Trie
import makegroups 

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
similarWords = {}
trieMap = Trie.TrieMap()
trieMap._init_(dict,minlen,maxlen)
for key in unique:
	wordList = trieMap.findSimilar(key)	
	similarWords[key] = wordList
groupingUtils = makegroups.GroupingUtil()
groups = []
for w in similarWords.keys():
	set = groupingUtils.findgroup(similarWords,w)
	if set:
		for list in set:
			if list not in groups:
				groups.append(list)
				print(list)

