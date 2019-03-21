import wikipedia as wiki
import random
from nltk import sent_tokenize
paragraphs = open('data.txt').read().splitlines()
lines=[]
while 1:
	for p in paragraphs:
		line=sent_tokenize(p)
		if line!=[]:
			lines.append(random.choice(line))
	url1=[]
	for l in lines:
		try:
			url1.append(wiki.page(l).url)
		except:
			pass
	if url1!=[]:
		break
res = max(set(url1), key = url1.count)
print(res)