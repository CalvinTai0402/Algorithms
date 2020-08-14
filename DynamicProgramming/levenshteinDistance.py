# O(MN) T O(MN) S
def levenshteinDistance(str1, str2):
	matrix = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
	i = 0
	for _ in matrix[0]:
		matrix[0][i] = i
		i += 1
	j = 0
	for _ in matrix:
		matrix[j][0] = j
		j += 1
	for k in range(1, len(str2)+1):
		for j in range(1, len(str1)+1):
			if str2[k-1] == str1[j-1]:
				matrix[k][j] = matrix[k-1][j-1]
			else:
				matrix[k][j] = 1 + min(matrix[k-1][j-1], matrix[k-1][j], matrix[k][j-1])
	return matrix[len(str2)][len(str1)]

# O(MN) T O(min(M,N)) S
def levenshteinDistance2(str1, str2):
	if len(str1) <= len(str2):
		minLength = len(str1)+1
		minString = str1
		maxString = str2
	else:
		minLength = len(str2)+1
		minString = str2
		maxString = str1
	matrix = [[0 for i in range(minLength)] for j in range(2)]
	i = 0
	for _ in matrix[0]:
		matrix[0][i] = i
		i += 1
	j = 0
	for _ in matrix:
		matrix[j][0] = j
		j += 1
	rowLength = 1
	while rowLength <= len(maxString):
		for j in range(1, minLength):
			k = 1
			if maxString[rowLength-1] == minString[j-1]:
				matrix[k][j] = matrix[k-1][j-1]
			else:
				matrix[k][j] = 1 + min(matrix[k-1][j-1], matrix[k-1][j], matrix[k][j-1])
		matrix[0] = matrix[1]
		matrix[1] = [0 for i in range(minLength)]
		matrix[1][0] = rowLength+1
		rowLength += 1
	return matrix[0][minLength-1]
