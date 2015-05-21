#!/bin/python
##code replaces unknown words in the translations with entries of highest score in the dictionary

import sys
import nltk
from nltk.collocations import *
import commands
f=open(sys.argv[1],"r")
#ref=open("test.ref","r")
lexfile1=open("../exp/lex.1.e2f","r")

commands.getstatusoutput("python correctdict.py ../lex.2.e2f")
lexfile2=open("../exp/lex.2.e2f.correct","r")

n=sys.argv[1]+".replace"
new=open(n,"w")
lines=f.readlines()
#print lines
lexicon1=lexfile1.readlines()
lexicon2=lexfile2.readlines()
lex={}

for line in lexicon1:
	w=line.split()
	if len(w)>2:
		if w[0] not in lex:
			lex[w[0]]=[]
		l=[w[1],float(w[2])]
#print l
		lex[w[0]].append(l)

for line in lexicon2:
	w=line.split()
	if len(w)>2:
		if w[0] not in lex:
			lex[w[0]]=[]
		l=[w[1],float(w[2])]
		lex[w[0]].append(l)
#def sortdict(dict):
#	lexicon={}
#print lex[w[0]][1][1]
	
for line in lines:
	words=line.split()
	for word in words:
		word=word.lower()
		if word in lex:
			high=-9999
			for i in range(len(lex[word])):	
				if high<lex[word][i][1]:
					high=lex[word][i][1]
					main=lex[word][i][0]
#			print word,main
#main=main.encode("UTF-8")
#new.write(main)
#			new.write(" ")
			print main,
		else:
			print word,
	
	print ""
#new.write(word)
#			new.write(" ")
#else:
#			new.write(word[0])
##			new.write(" ")'''



##new.write("\n")
