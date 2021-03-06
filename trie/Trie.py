#!/usr/bin/python
#Node for Trie implementation
#value -> char at this node
#branches -> dictionary of children char vs corresponding trieNodes
class TrieNode:
	#constructor
	count = 0
	def _init_(self,value):
		self.value = value
		self.branches = {}
		

	def getValue(self):
		return self.value
	
	def getBranches(self):
		return self.branches
	
	def setAChild(self,char):
		if char not in  self.branches:
			self.branches[char] = TrieNode()
			self.branches[char]._init_(char)

	def getChild(self,char):
		if(char in self.branches):
			return self.branches[char]
	
	#prints all words in the trie, used for debugging
	def _str_(self,tempNode,lists):
		if not tempNode.branches:
			print(lists)
		else:
			for currNode in tempNode.branches.keys():
				lists.append(currNode)
				self._str_(tempNode.branches[currNode],lists)
				lists.remove(currNode)
		return



#Trie implementation
#Implementatin class for Trie. 
#wordsOfSize -> the trie will hold all the words of this size only
class Trie:
	def _init_(self,wordsOfSize,words):
		self.wordsOfSize = wordsOfSize
		self.root = TrieNode()
		self.root._init_("")
		tempNode = self.root
		for word in words:
			for index,charValue  in enumerate(word):
				tempNode.setAChild(charValue)
				tempNode = tempNode.getChild(charValue)
			tempNode = self.root

	def _str_(self):
		self.root._str_(self.root,[])

	def getRoot():
		return self.root


#contains dictionary of length of words vs instance of above Trie class
#This class contains all the methods to find the words similar to a given word

#Algo:
#For a particular word at max three tries have to be travelled:
#1. trie corresponding to similar words of same length which is a result of replacement of a single character
#2. trie corresponding to words which can be obtained by deleting one character from given word
#3. trie corresponding to words which can be obtained by inserting one character in geven word

class TrieMap:
	def _init_(self,sizeVsWordsMap,minlen,maxlen):
		trieMap = {}
		for size in sizeVsWordsMap.keys():
			tempTrie = Trie()
			tempTrie._init_(size,sizeVsWordsMap[size])
			trieMap[size]=tempTrie
		self.trieMap = trieMap
		self.minlen = minlen
		self.maxlen = maxlen

	#method to travel the trie of words of same length and return a list of smilar words
	# word		-> input word
	# level		-> index in word
	# flag		-> to flag the replacement of char
	# tempNode	-> trieNode
	# sameLength	-> list to store similar words, result of this method
	# similarWord	-> characters are appended in this to create the word
	# @returnType	-> list of similar words of same length
	def findSameLength(self,word,level,flag,tempNode,sameLength,similarWord):
		if not tempNode.branches:
			if similarWord not in sameLength:
				sameLength.append(similarWord)
			return sameLength
		elif flag == 1:
			for key in tempNode.branches.keys():
				if key is word[level]:
					sameLength = self.findSameLength(word,level+1, flag, tempNode.branches[key],sameLength,similarWord+key)
		elif flag == 0:
			for key in tempNode.branches.keys():
				if key is not word[level]:
					flag = 1
					sameLength = self.findSameLength(word,level+1,flag,tempNode.branches[key],sameLength,similarWord+key)
					flag = 0
				else:	
					sameLength = self.findSameLength(word,level+1,flag,tempNode.branches[key],sameLength,similarWord+word[level])
		return sameLength

	# method to travel the trie of words of length one more than input and return a list of smilar words
	# word		-> input word
	# level		-> index in word
	# flag		-> to flag the insertion of char
	# tempNode	-> trieNode
	# longer	-> list to store similar words, result of this method
	# similarWord	-> characters are appended in this to create the word
	# @returnType	-> list of similar words of one greater length
	def findLonger(self,word,level,flag,tempNode,longer,similarWord):
		if not tempNode.branches:
			if similarWord not in longer:
				longer.append(similarWord)
			return longer
		elif flag == 1:
			for key in tempNode.branches.keys():
				if key is word[level]:
					longer = self.findLonger(word,level+1, flag, tempNode.branches[key],longer,similarWord+key)
		elif flag == 0:
			for key in tempNode.branches.keys():
		  		if level == len(word):
					flag = 1
					longer = self.findLonger(word,level,flag,tempNode.branches[key],longer,similarWord+key)
					flag = 0
				elif key is not word[level]:
					flag = 1
					longer = self.findLonger(word,level,flag,tempNode.branches[key],longer,similarWord+key)
					flag = 0
				else:	
					longer = self.findLonger(word,level+1,flag,tempNode.branches[key],longer,similarWord+word[level])
		return longer
	
	# method to travel the trie of words of one smaller length and return a list of smilar words
	# word		-> input word
	# level		-> index in word
	# flag		-> to flag the deletion of char
	# tempNode	-> trieNode
	# smaller	-> list to store similar words, result of this method
	# similarWord	-> characters are appended in this to create the word
	# @returnType	-> list of similar words of one smaller length
	def findSmaller(self,word,level,flag,tempNode,smaller,similarWord):
		if not tempNode.branches:
			if similarWord not in smaller:
				smaller.append(similarWord)
			return smaller
		elif flag == 1:
			for key in tempNode.branches.keys():
				if key is word[level]:
					smaller = self.findSmaller(word,level+1, flag, tempNode.branches[key],smaller,similarWord+key)
		elif flag == 0:
			for key in tempNode.branches.keys():
				if key is not word[level]:
					flag = 1
					smaller = self.findSmaller(word,level+1,flag,tempNode,smaller,similarWord)
					flag = 0
				else:	
					smaller = self.findSmaller(word,level+1,flag,tempNode.branches[key],smaller,similarWord+word[level])
		return smaller
		
	#method exposed to find all words similar to a given word
	#@returnType -> list of all similar words
	def findSimilar(self,word):
		sameLength = []
		longer = []
		smaller = []
		l =  len(word)
		sameLength = self.findSameLength(word,0,0,self.trieMap[l].root,sameLength,"")
		if l<self.maxlen:
			longer = self.findLonger(word,0,0,self.trieMap[l+1].root,longer,"")
		if l>self.minlen:
			smaller = self.findSmaller(word,0,0,self.trieMap[l-1].root,smaller,"")
		similar = sameLength + longer + smaller
		return similar


