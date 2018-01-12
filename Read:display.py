from random import *
import re


vFile = open("verb.txt", "r")
ingList = []
for word in vFile.readlines():
	if re.match(".*ing(.|\n)$", word):
		ingList.append(word)
print ingList[randint(1, len(ingList))]

aFile = open("adj.txt", "r")
aList = []
for word in aFile.readlines():
	aList.append(word)
print aList[randint(1, len(aList))]

nFile= open("noun.txt", "r")
nList = []
for word in nFile.readlines():
	nList.append(word)
print nList[randint(1, len(nList))]


nFile.close()
aFile.close()
vFile.close()



