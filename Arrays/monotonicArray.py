# O(N) T O(1) S
def isMonotonic(array):
    isNonDecreasing = True
	isNonIncreasing = True
	for i in range(len(array)-1):
		if array[i] > array[i+1]:
			isNonDecreasing = False
		if array[i] < array[i+1]:
			isNonIncreasing = False
	return isNonDecreasing or isNonIncreasing