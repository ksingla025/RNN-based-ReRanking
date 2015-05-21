#### This script convert strings into vectors and finds cosine similarity ####


import sys
import re, math
from collections import Counter
#f1=open(sys.argv[1],"r")
#3f2=open(sys.argv[2],"r")
f3=open("cosinevalue","a")
sline=sys.argv[0]
tline=sys.argv[1]
WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
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
text1 = 'This is a foo bar sentence .'
text2 = 'This sentence is similar to a foo bar sentence .'

vector1 = text_to_vector(sline)
vector2 = text_to_vector(tline)

cosine = get_cosine(vector1, vector2)
s=sys.argv[3]+" "+str(cosine)
f3.write(s)
