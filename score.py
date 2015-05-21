#!/bin/python

### take bigrams and score them using a language model and extend the hypothesis ####
import sys
import os
import commands
from operator import itemgetter
f=open("bigram","w")
count=0
index=0
def data (list1,list2):
	global index
	global count
	if len(list1)>len(list2):
		lst1=list1
		lst2=list2
	else:
	 	lst1=list2
	 	lst2=list1
	for word1 in list1:
#	count=0
		for word2 in list2:
#	s=word1+" "+word2+"\n"
			s=str(index)+" "+str(count)+" "+word1+" "+word2+"\n"	
			f.write(s)
		count=count+1
	count=0
	index=index+1
list1=["i","me","can"]
list2=["you","u","meow"]
list3=["us","we"]
sentlist=[]
sentlist.append(list1)
sentlist.append(list2)
sentlist.append(list3)
for i in range (len(sentlist)-1):

	data(sentlist[i],sentlist[i+1])
data(sentlist[i],sentlist[i-1])
f.close
	       				
#commands.getstatusoutput(" ~/diksha/rnnlm_with_features/rnnlm -rnnlm /home/karan/diksha/rnnlm_with_features/model_mono -test bigram -nbest 1 > scores.txt")
f2=open("scores.txt","r")
scores=f2.readlines()
del scores[0]
del scores[0]
del scores[0]
del scores[0]
del scores[-1]
del scores[-1]
del scores[-1]
del scores[-1]
f1=open("bigram1","r")
l1=f1.readlines()
scores = map(lambda y: int(y),map(lambda x: x[:-1],scores))
print scores
def top (l1,scores):
	bigram = []
	print l1
	for i in l1:
		bigram.append(i.split())
	print bigram
	k1 = 0
	k2 = 0
	avg = 0
	i = 0
	c = 0
	ans = []
	lexicon = {}
	while i < len(bigram):
		if int(bigram[i][0]) == k1:
			if int(bigram[i][1]) == k2:
				avg += scores[i]
				c += 1
				i += 1
			else:
				avg /= (c * 1.0)
				ans.append([bigram[i-1][2],avg])
#			ans.append([int(bigram[i-1][1]),avg])
				k2 += 1
				c = 0
				avg = 0
		else:
			avg /= (c * 1.0)
#			ans.append([int(bigram[i-1][1]), avg])
			ans.append([bigram[i-1][2],avg])
			lexicon[k1] = ans
			k1 += 1
			k2 = 0
			avg = 0
			c = 0
			ans = []
#ans.append([int(bigram[i-1][1]), avg/(c * 1.0)])
	ans.append([bigram[i-1][2], avg/(c * 1.0)])
	lexicon[k1] = ans
	for k in lexicon:
#		print k
		l = lexicon[k]
		lexicon[k] = [l[-1][0], l[-2][0]]
	print lexicon
	return lexicon
l=top(l1,scores)
print l
