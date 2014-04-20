#!/usr/bin/python
#Solution for printing groups of similar words

import re
import collections
import Trie
import makegroups 
import fileutils

#getting dictionary containing word vs list of words similar to key
#internally used trie
similarWords = fileutils.getSimilarWordDictionary()


groupingUtils = makegroups.GroupingUtil()
groups = []
for w in similarWords.keys():
	#getting set containing groups(list) of words all similar to each other
	set = groupingUtils.findgroup(similarWords,w)
	if set:
		for list in set:
			if list not in groups:
				groups.append(list)
				print(list)

