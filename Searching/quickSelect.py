# W: O(N^2) T O(N) S
# A: O(N) T O(logN) S
# B: O(N) T O(logN) S
def quickselect(array, k):
	return quickselectR(array, 0, 1, len(array)-1, k-1)
	
def quickselectR(array, pivot, leftPointer, rightPointer, wantedIndex):
	if pivot >= rightPointer:
		return array[rightPointer]
	nextRightPointer = rightPointer
	while leftPointer <= rightPointer:
		if array[leftPointer] > array[pivot] and array[rightPointer] < array[pivot]:
			array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
		elif array[leftPointer] <= array[pivot]:
			leftPointer += 1
		elif array[rightPointer] >= array[pivot]:
			rightPointer -= 1
	array[pivot], array[rightPointer] = array[rightPointer], array[pivot]
	if rightPointer == wantedIndex:
		return array[rightPointer]
	elif rightPointer < wantedIndex:
		return quickselectR(array, rightPointer+1, rightPointer+2, nextRightPointer, wantedIndex)
	else:
		return quickselectR(array, pivot, pivot+1, rightPointer-1, wantedIndex)

# W: O(N^2) T O(1) S
# A: O(N) T O(1) S
# B: O(N) T O(1) S
def quickselect2(array, k):
	return quickselectR2(array, 0, 1, len(array)-1, k-1)
	
def quickselectR2(array, pivot, leftPointer, rightPointer, wantedIndex):
	while True:
		nextRightPointer = rightPointer
		while leftPointer <= rightPointer:
			if array[leftPointer] > array[pivot] and array[rightPointer] < array[pivot]:
				array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
			elif array[leftPointer] <= array[pivot]:
				leftPointer += 1
			elif array[rightPointer] >= array[pivot]:
				rightPointer -= 1
		array[pivot], array[rightPointer] = array[rightPointer], array[pivot]
		if rightPointer == wantedIndex:
			return array[rightPointer]
		elif rightPointer < wantedIndex:
			pivot = rightPointer+1
			leftPointer = rightPointer+2
			rightPointer = nextRightPointer
		else:
			leftPointer = pivot+1
			rightPointer = rightPointer-1