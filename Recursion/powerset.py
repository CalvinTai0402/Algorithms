# O(N*2^N) T  O(N*2^N) S 
def powerset(array):
    subsets = [[]]
	for el in array:
		for i in range(len(subsets)):
			subsets.append(subsets[i]+[el])
	return subsets