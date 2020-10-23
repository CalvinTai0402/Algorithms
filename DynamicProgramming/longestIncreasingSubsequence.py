# O(N^2) T O(N) S
def longestIncreasingSubsequence(array):
    length = [1 for i in array]
	subsequenceIndices = [None for i in array]
	for i in range(len(array)):
		for j in range(i):
			if array[i] > array[j]:
				length[i] = max(length[i], 1+length[j])
				if length[i] == 1+length[j]:
					subsequenceIndices[i] = j
	return buildSubsequence(length, subsequenceIndices, array)
	
def buildSubsequence(length, subsequenceIndices, array):
	subsequence = []
	currentIndex = len(length) - 1 - length[::-1].index(max(length)) # find the last largest number's index
	while currentIndex is not None:
		subsequence.append(array[currentIndex])
		currentIndex = subsequenceIndices[currentIndex]
	return list(reversed(subsequence))


#==========================================Solution2===========================================

# O(NlogN) T O(N) S
def longestIncreasingSubsequence(array):
    subsequenceIndices = [None for i in array]
	indicesLength = [None for i in range(len(array)+1)] # The index represents the length, and the value array[index] represents the ending value of a longestIncreasingSubsequence of that length so far 
	length = 0
	for i, num in enumerate(array):	
		newLength = binarySearch(1, length, array, indicesLength, num)
		indicesLength[newLength] = i
		subsequenceIndices[i] = indicesLength[newLength-1]
		length = max(length, newLength)
	print(subsequenceIndices, indicesLength)
	return buildSubsequence(array[indicesLength[length]], subsequenceIndices, array)
	
def binarySearch(startIndex, endIndex, array, indicesLength, num):
	if startIndex > endIndex:
		return startIndex
	middleIndex = (startIndex + endIndex) // 2
	if array[indicesLength[middleIndex]] < num:
		startIndex = middleIndex + 1
	else:
		endIndex = middleIndex - 1
	return binarySearch(startIndex, endIndex, array, indicesLength, num)

def buildSubsequence(largestValue, subsequenceIndices, array):
	subsequence = []
	currentIndex = len(array) - 1 - array[::-1].index(largestValue)  # find the last largest number's index
	while currentIndex is not None:
		subsequence.append(array[currentIndex])
		currentIndex = subsequenceIndices[currentIndex]
	return list(reversed(subsequence))