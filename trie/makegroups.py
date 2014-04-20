#!/usr/bin/python
import re
class GroupingUtil:

	def findgroup(self,sm_dic,word):
		sets = []
		newlist = []
		sets.append(newlist)
		for w in sm_dic[word]:
			for list in sets:
				flag = 0    # init flag
				for val in list:   # chcking if the value is similar to all the values in the group
					if w not in sm_dic[val]:
						flag = 1 # flaging it for creating new group
						break
				if flag == 0:
					if w not in list:
						list.append(w)
						break
			if flag == 1:
				newlist = []
				newlist.append(w)
				sets.append(newlist)
		for list in sets:
			if word not in list:
				list.append(word)
		return sets;
