# O(N) T O(1) S
def isMonotonic(array):
	increasing = None
	if len(array) >=2:
		for i in range(len(array)-1):
			if array[i] < array[i+1]:
				increasing = True
				break
			if array[i] > array[i+1]:
				increasing = False
				break
		# Takes care of the edge case where all elements are the same
		if increasing is not True and increasing is not False:
			return True
		if increasing:
			for i in range(len(array)-1):
				if array[i] > array[i+1]:
					return False
		else:
			for i in range(len(array)-1):
				if array[i] < array[i+1]:
					return False
		return True
	else:
		return True # If the array contains 0 or 1 element, it will always be monotonic