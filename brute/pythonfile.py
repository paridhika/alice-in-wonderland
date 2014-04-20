#!/usr/bin/python
import re
import collections
import csv
def findsamelength(dic,word,lis):
	l = len(word)
	for w in dic[l]:
		flag = 0
		for i,c in enumerate(word):
			if flag == 1:
				break
			if word[i] != w[i]:
				flag = 1
				if i == l-1:
			  		lis.append(w)
				else:
					if re.match(w[i+1:],word[i+1:]):
						lis.append(w)
				
	return

#new code with optimisation
def findlonger(dic,word,lis):
	l = len(word)+1
	for w in dic[l]:
		flag = 0
		for i,c in enumerate(word):
			if flag == 1:
				break
			if word[i] != w[i]:
				flag = 1
				if re.match(w[i+1:],word[i:]):
					lis.append(w)
		if flag ==0:
			lis.append(w)
	return




#optimized
def findsmaller(dic,word,lis):
	l = len(word)-1
	for w in dic[l]:
		flag = 0
		for i,c in enumerate(w):
			if flag == 1:
				break
			if word[i] != w[i]:
				flag = 1
				if re.match(w[i:],word[i+1:]):
					lis.append(w)
		if flag == 0:
			lis.append(w)
	return



def findsimilar(dic,word):
	similar = []
	l = len(word)
	if l == 1:
		return dic[l]
	samelength = []
	longer = []
	smaller = []
	findsamelength(dic,word,samelength)
	findlonger(dic,word,longer)
	findsmaller(dic,word,smaller)
	similar = samelength + smaller + longer
	return similar

def findgroup(sm_dic,word):
	sets = []
	newlist = []
	sets.append(newlist)
	if word not in sm_dic:
		return sets
	for w in sm_dic[word]:
		flag = 0
		for list in sets:
			for val in list:
				if w not in sm_dic[val]:
					flag = 1
				if flag == 1:
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


f = open('alice.txt','r')
words = re.findall('\w+', f.read().lower())
unique = list(set(words))
dict = {}
MAX = 0
MIN = 1212
for word in unique:
	if len(word) > MAX:
		MAX = len(word)
	if len(word) < MIN:
		MIN = len(word)
	if len(word) in dict:
		dict[len(word)].append(word)
	else:
		dict[len(word)] = []
		dict[len(word)].append(word)
dict[MAX+1] = []
dict[MIN-1] = []

similar_dict={}

#for word in unique:
#	similar = []
#	similar = findsimilar(dict,word)
#	if similar:
#		similar_dict[word]=similar
#
print(similar_dict)
#with open ('dictionary.txt', 'w') as fp:
#    for p in similar_dict.items():
#            fp.write("%s:%s\n" % p)

