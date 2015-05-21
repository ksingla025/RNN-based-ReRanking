#!/bin/python
##to convert words in data to its root word usning morph analyzer output

import sys
file_name=sys.argv[1]
f=open(file_name,"r")
newfile=file_name+".root"
f1=open(newfile,"w")

lines=f.readlines()
for line in lines:
	l=line.split()
	if l[0]=="</Sentence>":
		f1.write("\n")
	if l[0] not in ('<Sentence','</Sentence>'):
		if len(l)>4:
			k=l[4].split(",")
	
			m=k[0].split("='")
			if m[1]!='&comma':
				f1.write(m[1])
			else:
				f1.write(l[1])
		else:
			f1.write(l[1])
		f1.write(" ")
f.close
f1.close


