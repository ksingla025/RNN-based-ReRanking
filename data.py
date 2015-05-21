#!/bin/python
###This code is to divide the data into training,testing and validating. 
###Training and valid data are represented in the format of a separate word(normal data),root word of the data, pos tag of each word, and other morph feature of the words

### converts the morph output of ILMT morph analyzer to make data ready for RNNLM training

import sys
f=open(sys.argv[1],'r') #input morph out
f1=open("train.words","w")
f2=open("train.lemma","w")
f3=open("train.pos","w")
f4=open("train.others","w")
f5=open("test.words","w")
f6=open("valid.words","w")
f7=open("valid.lemma","w")
f8=open("valid.pos","w")
f9=open("valid.others","w")
f10=open("test.lemma","w")
f11=open("test.pos","w")
f12=open("test.others","w")
count=0
X=0
lines=f.readlines()
if X<291042:
	for line in lines:
		l=line.split()
		if l[0]=="</Sentence>":
			count=count+1
			if count<291042:
				f1.write("\n")
				f2.write("\n")
				f3.write("\n")
				f4.write("\n")
			if 291042<=count<292042:
				f5.write("\n")
				f11.write("\n")
				f12.write("\n")
				f10.write("\n")
			if 292042<=count<293042:
				f6.write("\n")
				f7.write("\n")
				f8.write("\n")
				f9.write("\n")
		if l[0] not in ('<Sentence','</Sentence>'):
			if len(l)>4:
				k=l[4].split(",")
				m=k[0].split("='")
				s=m[1] #s is the lemma word
				if count<291042:
					if l[1] != "'":
						f1.write(l[1]) # original word for .words
						f1.write(" ") 
					
						if len(l)>4:
#	k=l[4].split(",")	
							if s:
								f3.write(k[1])
								f3.write(" ") #check if pos is PUNC and word is not a punc
								#o=k[2]
								o=""
								for a in range (2,7):
									if k[a]!="":
										o=o+k[a]+"_"
									else:
										o=o+"E_"
	
								if k[-1][0]=="'":
									o=o+"E"
								else :
									o=o+k[-1][0]
							 	f4.write(o)
				       				f4.write(" ")		
#m=k[0].split("='")
								if m[1]!="&comma":
									f2.write(m[1])
								else:
									f2.write(l[1])
								f2.write(" ")
							else:
								f2.write(l[1])
								f2.write(" ")
				if 291042<=count<292042: 		#test files banana (not minion wala :P )
					print count
					if l[1] != "'":
						f5.write(l[1])
						f5.write(" ")
						if len(l)>4:
#	k=l[4].split(",")	
							if s:
								f11.write(k[1])
								f11.write(" ") #check if pos is PUNC and word is not a punc
								#o=k[2]
								o=""
								for a in range (2,7):
									if k[a]!="":
										o=o+k[a]+"_"
									else:
										o=o+"E_"
	
								if k[-1][0]=="'":
									o=o+"E"
								else :
									o=o+k[-1][0]
							 	f12.write(o)
				       				f12.write(" ")		
#m=k[0].split("='")
						#k=l[4].split(",")
						#m=k[0].split("='")
								if m[1]!='&comma':
									f10.write(m[1])
								else:
									f10.write(l[1])
								f10.write(" ")
						else:
							f10.write(l[1])
							f10.write(" ")
				if 292042<=count<293042: # valid files banana (:D)
					print count	
					if l[1] != "'":
						f6.write(l[1])
						f6.write(" ")
					
						if len(l)>4:
#							k=l[4].split(",")
							if s:
								f8.write(k[1])
								f8.write(" ")
								o=""
								for a in range (2,7):
									if k[a]!="":
										o=o+k[a]+"_"
									else:
										o=o+"E_"

								if k[-1][0]=="'":
									o=o+"E"
								else :
									o=o+k[-1][0]
						 		f9.write(o)
				       				f9.write(" ")		
#m=k[0].split("='")
#m=k[0].split("='")
							if m[1]!='&comma':
								f7.write(m[1])
							else:
								f7.write(l[1])
							f7.write(" ")
						else:
							if l[1]!="'":		
								f7.write(l[1])
								f7.write(" ")
f.close()

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
