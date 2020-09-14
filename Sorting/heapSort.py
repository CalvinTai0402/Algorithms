# O(logN) T O(1) S
def heapSort(array):
	buildMaxHeap(array)
	for i in reversed(range(1, len(array))):
		swap(0, i, array)
		siftDown(0, i-1, array)
	return array

# O(N) T O(1) S
def buildMaxHeap(array):
	lastIndex = (len(array)-1)
	lastParentIndex = int((lastIndex-1)/2)
	while lastParentIndex >= 0:
		siftDown(lastParentIndex, len(array)-1, array)
		lastParentIndex -= 1	
	return 
 
# O(logN) T O(1) S 
def siftDown(index, endIndex, array):
	while (2*index+1) <= endIndex:
		currentNode = array[index]
		childOne, i1 = getChildOne(index, endIndex, array)
		childTwo, i2 = getChildTwo(index, endIndex, array)
		if max(childOne, childTwo) == childOne:
			maxChild = childOne
			swapIndex = i1
		else:
			maxChild = childTwo
			swapIndex = i2
		if maxChild > currentNode:
			swap(index, swapIndex, array)
			index = swapIndex
		else:
			break
	return
	
# O(1) T O(1) S
def getChildOne(index, endIndex, array):
	if 2*index+1 <= endIndex:
		return array[2*index+1], 2*index+1
	else:
		return float("-inf"), -1

# O(1) T O(1) S
def getChildTwo(index, endIndex, array):
	if 2*index+2 <= endIndex:
		return array[2*index+2], 2*index+2
	else:
		return float("-inf"), -1
		
# O(1) T O(1) S
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]