#!/usr/bin/python
#util for grouping all words similar to a word, such that in a 
#group every word is similar to every other word
import re
class GroupingUtil:
	
	#sm_dic -> list of words similar to word
	#word	-> input word 
	def findgroup(self,sm_dic,word):
		sets = []
		newlist = []
		sets.append(newlist)
		for w in sm_dic[word]:
			for list in sets:
				# init flag
				flag = 0
				#checking if the value is similar to all the values in the group
				for val in list:
					if w not in sm_dic[val]:
						#flaging it for creating new group
						flag = 1
						break
				if flag == 0:
					if w not in list:
						list.append(w)
						break
			if flag == 1:
				newlist = []
				newlist.append(w)
				sets.append(newlist)
		#appending the input word in every group formed since it is similar to all
		for list in sets:
			if word not in list:
				list.append(word)
		return sets;
