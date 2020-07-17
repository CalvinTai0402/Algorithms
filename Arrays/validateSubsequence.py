# O(N) T O(1) S
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
	return True 
