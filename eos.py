#!/bin/python
###removes EOS(%EPS%) tag from the giza output
f=open("bilang.txt","r")
f1=open("eos.txt","w")
lines=f.readlines()
for line in lines:
	words=line.split()
#print words
#	print len(words)
#	print words[len(words)-1]
	fl=[]
	for i in range(len(words)):
		fl.append(0)
#	       	print i, len(words), words[i]
		l=words[i].split("_")
		if l[0]=="%EPS%":
			words[i-1]=words[i-1]+";"+l[1]
			fl[i]=1
##print words[i-1]
	for i in range(len(words)):
	 	if fl[i]==0:
			f1.write(words[i])
			f1.write(" ")
	f1.write("\n")
	
			
