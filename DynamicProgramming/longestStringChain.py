# O(NM^2 + NlogN) T O(NM) S
def longestStringChain(strings):
    stringsHashTable = {}
	for string in strings:
		stringsHashTable[string] = {"previousString" : "", "maxChainedLength" : 1}
	sortedStrings = sorted(strings, key=len)
	for string in sortedStrings:
		buildHashTable(string, stringsHashTable)
	return buildLongestStringChain(strings, stringsHashTable)

def buildHashTable(string, stringsHashTable):
	for i in range(len(string)):
		smallerString = getSubstring(string, i)
		if smallerString in stringsHashTable:
			updateHashTable(string, smallerString, stringsHashTable)
			
def updateHashTable(string, smallerString, stringsHashTable):
	stringMaxChainedLength = stringsHashTable[string]["maxChainedLength"]
	smallerStringMaxChainedLength = stringsHashTable[smallerString]["maxChainedLength"]
	if smallerStringMaxChainedLength + 1 > stringMaxChainedLength:
		stringsHashTable[string]["maxChainedLength"] = smallerStringMaxChainedLength + 1
		stringsHashTable[string]["previousString"] = smallerString

def getSubstring(string, i):
	return string[0:i] + string[i+1:]
	
def buildLongestStringChain(strings, stringsHashTable):
	maxChainedLength = 0
	maxChainedString = ""
	for string in strings:
		if stringsHashTable[string]["maxChainedLength"] > maxChainedLength:
			maxChainedLength = stringsHashTable[string]["maxChainedLength"]
			maxChainedString = string
	listOfLongestChainedStrings = []
	currentString = maxChainedString
	while currentString != "":
		listOfLongestChainedStrings.append(currentString)
		currentString = stringsHashTable[currentString]["previousString"]
	return [] if len(listOfLongestChainedStrings) == 1 else listOfLongestChainedStrings