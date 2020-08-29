# O(IJ) T O(IJ) S
def knapsackProblem(items, capacity):
	itemIndices = []
	returnItems = []
	matrix = [[0 for j in range(capacity+1)] for i in range(len(items)+1)]
	for i in range(1, len(matrix)):
		for j in range(len(matrix[0])):
			itemVal = items[i-1][0]
			itemWeight = items[i-1][1]
			if itemWeight > j:
				matrix[i][j] = matrix[i-1][j]
			else:
				matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-itemWeight]+itemVal)
	backtrackI = len(matrix)-1
	backtrackJ = len(matrix[0])-1
	while backtrackI != 0 and backtrackJ != 0:
		if matrix[backtrackI][backtrackJ] == matrix[backtrackI-1][backtrackJ]:
			backtrackI -= 1
		else:
			returnItems.append(items[backtrackI-1])
			backtrackJ -= items[backtrackI-1][1]
			backtrackI -= 1
	for item in returnItems:
		itemIndices.append(items.index(item))
	return[matrix[len(matrix)-1][len(matrix[0])-1], itemIndices]