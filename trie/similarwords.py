#!/usr/bin/python
#Solution for getting list of words similar to the given input

import re
import Trie
import sys
import fileutils

#Taking word from command line
wordToBeLooked = sys.argv[1]

#calculating the range of length of possible similar words
minlen = len(wordToBeLooked)-1
maxlen = len(wordToBeLooked)+1

#Getting dictionary for length of word vs word list
#Here key lies in the range of length of possible similar words
dict = fileutils.getDictionary(wordToBeLooked)

#Creating map of wordlength vs trie of words for above dictionary
trieMap = Trie.TrieMap()
trieMap._init_(dict,minlen,maxlen)

#finding similar words by travesing over three tries
wordList = trieMap.findSimilar(wordToBeLooked)
print(wordList)
