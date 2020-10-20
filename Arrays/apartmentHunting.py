# O(B^2*R) T O(B) S
def apartmentHunting(blocks, reqs):
    maxDistanceAtBlocks = [float("-inf") for block in blocks]
	for i in range(len(blocks)):
		for req in reqs:
			closestReqDistance = float("inf")
			for j in range(len(blocks)):
				if blocks[j][req]:
					closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
			maxDistanceAtBlocks[i] = max(maxDistanceAtBlocks[i], closestReqDistance)
	return getMinIndex(maxDistanceAtBlocks)

def getMinIndex(maxDistanceAtBlocks):
	currentIndex = 0
	minDist = float("inf")
	for i in range(len(maxDistanceAtBlocks)):
		if maxDistanceAtBlocks[i] < minDist:
			minDist = maxDistanceAtBlocks[i]
			currentIndex = i
	return currentIndex

def distanceBetween(i,j):
	return abs(i-j)


#=========================================================Solution 2================================================================

# O(BR) T O(BR) S
def apartmentHunting(blocks, reqs):
	# reqMinDistancesAtBlocks is a 2D array
	reqMinDistancesAtBlocks = list(map(lambda req: getReqMinDistancesAtBlocks(blocks, req), reqs))
	maxDistanceAtBlocks = getMaxDistanceAtBlocks(reqMinDistancesAtBlocks)
    return getMinIndex(maxDistanceAtBlocks)

def getReqMinDistancesAtBlocks(blocks, req):
	reqMinDistancesAtBlocks = [float("inf") for block in blocks]
	closestReqIndex = float("inf")
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestReqIndex = i
		reqMinDistancesAtBlocks[i] = distanceBetween(i, closestReqIndex)
	closestReqIndex = float("inf")
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestReqIndex = i
		reqMinDistancesAtBlocks[i] = min(reqMinDistancesAtBlocks[i], distanceBetween(i, closestReqIndex))
	return reqMinDistancesAtBlocks

def getMaxDistanceAtBlocks(reqMinDistancesAtBlocks):
	maxDistanceAtBlocks = [float("-inf") for block in range(len(reqMinDistancesAtBlocks[0]))]
	for i in range(len(reqMinDistancesAtBlocks[0])):
		distancesAtBlock = list(map(lambda distance: distance[i], reqMinDistancesAtBlocks))
		maxDistanceAtBlocks[i] = max(distancesAtBlock)
	return maxDistanceAtBlocks

def getMinIndex(maxDistanceAtBlocks):
	currentIndex = 0
	minDist = float("inf")
	for i in range(len(maxDistanceAtBlocks)):
		if maxDistanceAtBlocks[i] < minDist:
			minDist = maxDistanceAtBlocks[i]
			currentIndex = i
	return currentIndex

def distanceBetween(i,j):
	return abs(i-j)