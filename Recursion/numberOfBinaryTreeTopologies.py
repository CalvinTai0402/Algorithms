# O(N^2) T O(N) S, stack call never exceeds N
def numberOfBinaryTreeTopologies(n, cache = {0: 1}):
    if n in cache:
		return cache[n]
	totalNumTrees = 0
	for left in range(n):
		right = n-1-left
		numOfLeftTrees = numberOfBinaryTreeTopologies(left, cache)
		numOfRightTrees = numberOfBinaryTreeTopologies(right, cache)
		totalNumTrees += numOfLeftTrees*numOfRightTrees
	cache[n] = totalNumTrees
	return cache[n]