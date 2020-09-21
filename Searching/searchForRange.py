# O(logN) T O(1) S
def searchForRange(array, target):
	leftIndex = searchForRangeL(array, target, 0, len(array)-1)
	rightIndex = searchForRangeR(array, target, 0, len(array)-1)
	return [leftIndex, rightIndex]

# Searches for the left extremity
def searchForRangeL(array, target, leftPointer, rightPointer):
	if leftPointer > rightPointer:
		return -1
	midPointer = (leftPointer+rightPointer) // 2
	if target == array[midPointer]:
		if midPointer == 0 or array[midPointer-1] != target:
			return midPointer
		else:
			return searchForRangeL(array, target, leftPointer, midPointer-1)
	elif target < array[midPointer]:
		return searchForRangeL(array, target, leftPointer, midPointer-1)
	else:
		return searchForRangeL(array, target, midPointer+1, rightPointer)

# Searches for the right extremity
def searchForRangeR(array, target, leftPointer, rightPointer):
	if leftPointer > rightPointer:	
		return -1
	midPointer = (leftPointer+rightPointer) // 2
	if target == array[midPointer]:
		if midPointer == len(array)-1 or array[midPointer+1] != target:
			return midPointer
		else:
			return searchForRangeR(array, target, midPointer+1, rightPointer)
	elif target < array[midPointer]:
		return searchForRangeR(array, target, leftPointer, midPointer-1)
	else:
		return searchForRangeR(array, target, midPointer+1, rightPointer)