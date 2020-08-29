# O(N) T O(1) S
def waterArea(heights):
	if len(heights) == 0 or len(heights) == 1:
		return 0
    surfaceArea = 0
	leftPointer = 0
	rightPointer = len(heights)-1
	minVal = min(heights[leftPointer], heights[rightPointer])
	while leftPointer < rightPointer:
		if heights[leftPointer] < heights[rightPointer]:
			leftPointer += 1
			if heights[leftPointer] < minVal:
				surfaceArea += (minVal - heights[leftPointer])
			else:
				minVal = min(heights[leftPointer], heights[rightPointer])
		else:
			rightPointer -= 1
			if heights[rightPointer] < minVal:
				surfaceArea += (minVal - heights[rightPointer])
			else:
				minVal = min(heights[leftPointer], heights[rightPointer])
	return surfaceArea