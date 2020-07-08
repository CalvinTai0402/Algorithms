# Time: O(N), Space: O(1)
def isValidSubsequence(array, sequence):
	arrayPointer = 0
	for i in range(len(sequence)):
		while True:
			if arrayPointer >= len(array):
				return False
			if sequence[i] == array[arrayPointer]:
				arrayPointer = arrayPointer + 1
				break
			else:
				arrayPointer = arrayPointer + 1
	return (i == len(sequence)-1) 