# O(N^2) T O(1) S
def selectionSort(array):
    for index in range(len(array)):
		smallest = array[index]
		swapIndex = index
		for j in range(index,len(array)):
			if array[j] < smallest:
				smallest = array[j]
				swapIndex = j
		array[index],array[swapIndex] = array[swapIndex],array[index]
	return array