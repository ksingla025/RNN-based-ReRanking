#!/bin/python
###this code finds the most similar sentence out of the n best translations

### THis is used to find the oracle sentence
import os
import sys
import commands
import re, math
from collections import Counter
f=open(sys.argv[1],"r")
reference=open(sys.argv[2],"r")
flag=int(sys.argv[3])
if flag==2:
	f3=open("cosinevalue","w")
hypo=open("hypothesis.txt","w")
lines=f.readlines()
ref=reference.readlines()
WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):##find cosine similarity
	intersection = set(vec1.keys()) & set(vec2.keys())
	numerator = sum([vec1[x] * vec2[x] for x in intersection])
	sum1 = sum([vec1[x]**2 for x in vec1.keys()])
	sum2 = sum([vec2[x]**2 for x in vec2.keys()])
	denominator = math.sqrt(sum1) * math.sqrt(sum2)

	if not denominator:
		return 0.0
	else:
		return float(numerator) / denominator

def text_to_vector(text):
	words = WORD.findall(text)
	return Counter(words)

for line in lines:#get lines
	w=line.split("|||")
	rfline=ref[int(w[0])]
	hyline=w[1]
	if flag==1:
		commands.getstatusoutput("g++ ~/WMT_emb/new.c")
		h="~/WMT_emb/./a.out ~/word2vec/scripts/data_vector "+rfline+" "+hyline+" "+w[0]
		print h
		commands.getstatusoutput(h)

#text1 = 'This is a foo bar sentence .'
#text2 = 'This sentence is similar to a foo bar sentence .'
	if flag==2:
		vector1 = text_to_vector(rfline)
		vector2 = text_to_vector(hyline)
		cosine = get_cosine(vector1, vector2)
		s=w[0]+" "+str(cosine)
		f3.write(s)
		f3.write("\n")

if flag==1:
	f=open("~/WMT_emb/newcosine","r")
	value=f.readlines()
if flag==2:
	f3.close()

	f=open("cosinevalue","r")
	value=f.readlines()
k=-1
index=-1
for i in range(len(value)):##find most similar sentence
	w=value[i].split()
	if int(w[0])!=k:
		k=int(w[0])
		high=float(w[1])
		if k!=-1:
			m=lines[index].split("|||")
			hypo.write(m[1])
			hypo.write("\n")
		index=i
	else:
		if float(w[1])>high:
			high=float(w[1])
			index=i

m=lines[index].split("|||")
hypo.write(m[1])
hypo.write("\n")
