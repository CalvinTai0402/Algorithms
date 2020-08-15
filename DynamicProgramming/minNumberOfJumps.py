# O(N) T O(1) S
def minNumberOfJumps(array):
	if len(array) == 1:	
		return 0
    maxReach, steps = array[0], array[0]
	jumps = 0
	for i in range(1,len(array)-1):
		maxReach = max(maxReach, array[i]+i)
		steps -= 1
		if steps == 0:
			steps = maxReach - i
			jumps += 1
	return jumps + 1