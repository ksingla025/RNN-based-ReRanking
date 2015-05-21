###extract lines from nbest translations from moses


#!/bin/python
import sys
f=open(sys.argv[1],"r")
o=sys.argv[1]+".sentences"
f1=open(o,"w")

lines=f.readlines()
for line in lines:
	w=line.split(" |||")
	s=w[0]+w[1]+"\n"
	f1.write(s)
