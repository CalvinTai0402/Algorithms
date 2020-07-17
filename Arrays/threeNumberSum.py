# O(N^2) T, O(N) space
def threeNumberSum(array, targetSum):
    array.sort() # O(NlogN) T, hopefully
	twoDArray = []
    for i in range(len(array)): # O(N)
		mySum = targetSum-array[i]
		leftPointer = i+1
		rightPointer = len(array)-1
		while leftPointer < rightPointer: # O(N)
			if array[leftPointer] + array[rightPointer] == mySum:
				tempList = [array[i],array[leftPointer],array[rightPointer]]
				twoDArray.append(tempList)
			if array[leftPointer] + array[rightPointer] < mySum:
				leftPointer = leftPointer+1
			else:
				rightPointer = rightPointer-1
	return twoDArray