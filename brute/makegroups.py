#!/usr/bin/python
import re
def findgroup(sm_dic,word):
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


with open ('dictionary.txt', 'r') as fp:
	d = {}
	l = fp.read().split('\n')      # Split using \n
	for i in l:
		if ':' in i:
			values = i.split(':')   # Split using ':'
			words = re.findall('\w+',values[1])
			d[values[0]] = words
fp.close()
groups = []
for w in d.keys():
	set = findgroup(d,w)
	if set:
		for list in set:
			if list not in groups:
				groups.append(list)
				print(list)

#with open ('groups.txt', 'w') as fp:
#    for p in groups:
#                fp.write("%s\n" % p)



