# O(N^3+M) T O(N+M) S
def numbersInPi(pi, numbers):
    numbersHashTable = {number: True for number in numbers}
	minSpaces = getMinSpacesR(pi, numbersHashTable, {}, 0)
	return -1 if minSpaces == float("inf") else minSpaces
	
def getMinSpacesR(pi, numbersHashTable, cache, index):
	if index == len(pi):
		return -1
	if index in cache:
		return cache[index]
	minSpaces = float("inf")
	for i in range(index, len(pi)):
		prefix = pi[index: i+1]
		if prefix in numbersHashTable:
			minSuffixSpaces = getMinSpacesR(pi, numbersHashTable, cache, i+1)
			minSpaces = min(minSpaces, minSuffixSpaces + 1)
	cache[index] = minSpaces
	return cache[index]