# O(B+S) T O(B+S) S
def smallestSubstringContaining(bigString, smallString):
    targetHashMap = getTargetHashMap(smallString)
	subStringBounds = getSubStringBounds(bigString, targetHashMap)
	return getSmallestSubstring(bigString, subStringBounds)

def getSubStringBounds(bigString, targetHashMap):
	subStringHashMap = {}
	subStringBounds = [0, float("inf")]
	leftPointer = 0
	rightPointer = 0
	numUniqueTargetHashMap = len(targetHashMap.keys())
	numUniqueDone = 0
	while rightPointer < len(bigString):
		rightChar = bigString[rightPointer]
		if rightChar not in targetHashMap:
			rightPointer += 1
			continue
		increaseCharCount(rightChar, subStringHashMap)
		if subStringHashMap[rightChar] == targetHashMap[rightChar]:
			numUniqueDone += 1
		while numUniqueDone == numUniqueTargetHashMap and leftPointer <= rightPointer:
			leftChar = bigString[leftPointer]
			if leftChar not in targetHashMap:
				leftPointer += 1
				continue
			if subStringHashMap[leftChar] == targetHashMap[leftChar]:
				numUniqueDone -= 1
			decreaseCharCount(leftChar, subStringHashMap)
			subStringBounds = getSubStringBoundsHelper(leftPointer, rightPointer, subStringBounds)
			leftPointer += 1
		rightPointer += 1
	return subStringBounds
	
def getSubStringBoundsHelper(leftPointer, rightPointer, subStringBounds):
	currentStartBound, currentEndBound = subStringBounds
	return [leftPointer, rightPointer] if rightPointer-leftPointer < currentEndBound-currentStartBound else [currentStartBound, currentEndBound]
	
def getSmallestSubstring(bigString, subStringBounds):
	return "" if subStringBounds[1] == float("inf") else bigString[subStringBounds[0]:subStringBounds[1]+1]

def getTargetHashMap(string):
	targetHashMap = {}
	for char in string:
		increaseCharCount(char, targetHashMap)
	return targetHashMap
	
def increaseCharCount(char, hashMap):
	if char not in hashMap:
		hashMap[char] = 0
	hashMap[char] += 1
	
def decreaseCharCount(char, hashMap):
	if char not in hashMap:
		return
	hashMap[char] -= 1