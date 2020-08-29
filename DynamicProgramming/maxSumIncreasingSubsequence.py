# O(N^2) T O(N) S
def maxSumIncreasingSubsequence(array):
    result = [0,[]]
	maxSumSubsequence = array.copy()
	indexArray = [None for i in range(len(array))]
	for i in range(len(array)):
		for j in range(i):
			if array[i] > array[j] and maxSumSubsequence[i] < array[i] + maxSumSubsequence[j]:
				maxSumSubsequence[i] = array[i] + maxSumSubsequence[j]
				indexArray[i] = j
	result[0] = max(maxSumSubsequence)
	ind = maxSumSubsequence.index(max(maxSumSubsequence))
	while ind is not None:
		result[1].insert(0,array[ind])
		ind = indexArray[ind]
	return result