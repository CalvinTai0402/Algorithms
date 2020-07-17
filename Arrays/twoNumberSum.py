# O(NlogN) T O(1) S
def twoNumberSum(array, targetSum):
	array.sort() # O(NlogN) T, hopefully
    left = 0 # left pointer
	right = len(array)-1 # right pointer
	while left < right: # Loop has O(N) T
		if array[left]+array[right] == targetSum:
			return [array[left],array[right]]
		elif array[left]+array[right] < targetSum:
			left+=1
		elif array[left]+array[right] > targetSum:
			right-=1
    return []
