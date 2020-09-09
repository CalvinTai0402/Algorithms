# O(NlogN) T O(logN)S
def quickSort(array):
	if len(array) <= 1:
		return array
	return quickSortR(array, 0, 1, len(array)-1)
	
def quickSortR(array, pivot, leftPointer, rightPointer):
	if pivot >= rightPointer:
		return
	while leftPointer <= rightPointer:
		if array[leftPointer] > array[pivot] and array[rightPointer] < array[pivot]:
			array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
		elif array[leftPointer] <= array[pivot]:
			leftPointer += 1
		elif array[rightPointer] >= array[pivot]:
			rightPointer -= 1
	array[pivot], array[rightPointer] = array[rightPointer], array[pivot]
	if len(array)-1 - rightPointer+2 < rightPointer-1 - pivot+1:
		quickSortR(array, rightPointer+1, rightPointer+2, len(array)-1)
		quickSortR(array, pivot, pivot+1, rightPointer-1)
	else:
		quickSortR(array, pivot, pivot+1, rightPointer-1)
		quickSortR(array, rightPointer+1, rightPointer+2, len(array)-1)
	return array