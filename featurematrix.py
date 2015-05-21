#!/bash/python
###to create feature matrix of the data using the morph information
import sys

f=open(sys.argv[1],'r')
f1=open(sys.argv[1]+".featurematrix",'w')
matrix={}
feature=['adv', 'num', 'n', 'psp', 'punc', 'unk', 'pn', 'v', 'avy', 'adj','m','f','sg','pl','1','2','3','d','o']
#print feature

lines=f.readlines()
for line in lines:
	l=line.split()
	if l[0]=="</Sentence>":
		f1.write("\n")
	if l[0] not in ('<Sentence','</Sentence>'):
		if len(l)>4:
			k=l[4].split(",")
			m=k[0].split("='")
			s=m[1]
			if s not in matrix:
				matrix[s]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			for i in range(1,6):
				if k[i] in feature:
					n=feature.index(k[i])
					matrix[s][n]=matrix[s][n]+1
for key in matrix:
	print key+' ',
#	print matrix[key]
	print ' '.join(str(x) for x in matrix[key])
#	k = ''.join(str(matrix[key]))
#	print k


							
#m=k[0].split("='")
#			if m[1]!='&comma':
#				f1.write(m[1])
#			else:
#				f1.write(l[1])
#		else:
