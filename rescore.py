#!/bin/python

import os
import sys
import commands

f=open(sys.argv[1],"r") #input file format 0 ||| rAm kelA KAtA he ||| 
f1=open("nbest","w")
o=sys.argv[1]+".rnnlmbest"
f3=open("best.rnnlm","w")
#n=int(sys.argv[2])
flag=int(sys.argv[2])#mode
print flag
#flag=0
lines=f.readlines()
for line in lines:
	w=line.split("|||")
#	w=line.split(" ")
#print w
	s=w[0]+" "+w[1]+"\n"
	f1.write(s)
alpha=2.5
beta=2.5
gamma=2.5
delta=1-alpha-beta-gamma
f.close()
f1.close()
if flag==1:
	commands.getstatusoutput("./rnnlm -rnnlm model_mono -test nbest -nbest 1 > scores.txt")
if flag==2:
	commands.getstatusoutput("./rnnlm -rnnlm model_lemma -test nbest -nbest 1 > scores.txt")
elif flag==3:
	commands.getstatusoutput("./rnnlm -rnnlm model_pos -test nbest -nbest 1 > scores.txt")
elif flag==4:
	commands.getstatusoutput("./rnnlm -rnnlm model_others -test nbest -nbest 1 > scores.txt")
elif flag==5:
	commands.getstatusoutput("./rnnlm -rnnlm model_mono -test nbest -nbest 1 > scores1.txt")
	commands.getstatusoutput("./rnnlm -rnnlm model_lemma -test nbest -nbest 1 > scores2.txt")
	commands.getstatusoutput("./rnnlm -rnnlm model_pos -test nbest -nbest 1 > scores3.txt")
	commands.getstatusoutput("./rnnlm -rnnlm model_others -test nbest -nbest 1 > scores4.txt")


if flag!=5:
	
	f2=open("scores.txt","r")
	score=f2.readlines()
	del score[0]
	del score[0]
	del score[0]
	del score[-1]
	del score[-1]
	del score[-1]
	del score[-1]
	f2.close()
if flag==5:
	
	f2=open("scores1.txt","r")
	score1=f2.readlines()
	del score1[0]
	del score1[0]
	del score1[0]
	del score1[-1]
	del score1[-1]
	del score1[-1]
	del score1[-1]
	f2.close
	f2=open("scores2.txt","r")
	score2=f2.readlines()
	del score2[0]
	del score2[0]
	del score2[0]
	del score2[-1]
	del score2[-1]
	del score2[-1]
	del score2[-1]
	f2.close()
	f2=open("scores3.txt","r")
	score3=f2.readlines()
	del score3[0]
	del score3[0]
	del score3[0]
	del score3[-1]
	del score3[-1]
	del score3[-1]
	del score3[-1]
	f2.close()
	f2=open("scores4.txt","r")
	score4=f2.readlines()
	del score4[0]
	del score4[0]
	del score4[0]
	del score4[-1]
	del score4[-1]
	del score4[-1]
	del score4[-1]
	f2.close()
	for i in len(score1):
		score[i]=alpha*float(score1[i])+beta*float(score2[i])+gamma*float(score3[i])+delta*float(score4)
#print score
k=0
index=-1
maximum=-99999999
count=0
#print len(lines)
#print len(score)
for i in range(len(score)):
	count=count+1
	#for j in range(0,n):
	print i
	w=lines[i].split("|||")
#print i
	
	f=float(score[i])
	print int(w[0]),w[1]
	if k!=int(w[0]):##count==n+1:
		k=int(w[0])
		maximum=f
		l=lines[index].split("|||")
		f3.write(l[1])
		f3.write(" \n")
		index=i
		count=1
	if float(score[i])>maximum:
	
		index=i
		maximum=float(score[i])
l=lines[index].split("|||")
f3.write(l[1])
f3.write("\n")
			
f3.close()











#		print float(score[i])
'''	if count==n:
			maximum=-99999999
			count=0
		if int(w[0])!=k:
			print "index",int(w[0])
			k=int(w[0])
			l=lines[index].split("|||")
			f3.write(l[1])
			f3.write("\n")
			
			maximum=float(score[i])
			index=i
		else:
		f=float(score[i])
		if float(score[i])>maximum:
	
			index=i
			maximum=float(score[i])
			
		if j==n-1:
			print maximum
			print index
			maximum=-999999999
			print lines[index]
			l=lines[index].split("|||")
			f3.write(l[1])
			f3.write("\n")
			index=-1
	j=0'''


		
