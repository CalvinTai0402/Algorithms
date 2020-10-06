# O(logN) T O(1) S
def shiftedBinarySearch(array, target):
    if len(array) == 0:
		return -1
	return shiftedBinarySearchH(array, target, 0, len(array)-1)
 
def shiftedBinarySearchH(array, target, leftPointer, rightPointer):
	while leftPointer <= rightPointer:
		middlePointer = (leftPointer + rightPointer)//2
		if target == array[middlePointer]:
			return middlePointer
		elif array[leftPointer] <= array[middlePointer]:
			if target >= array[leftPointer] and target < array[middlePointer]:
				rightPointer = middlePointer-1
			else:
				leftPointer = middlePointer+1
		else:
			if target <= array[rightPointer] and target > array[middlePointer]:
				leftPointer = middlePointer+1
			else:
				 rightPointer = middlePointer-1			
	return -1