# O(NM) T O(NM) S
def longestCommonSubsequence(str1, str2):
    matrix = [[[None, 0, None, None] for col in range(len(str1)+1)] for row in range(len(str2)+1)]
	for i in range(1, len(str2)+1):
		for j in range(1, len(str1)+1):
			if str1[j-1] == str2[i-1]:
				matrix[i][j] = [str1[j-1], 1+matrix[i-1][j-1][1], i-1, j-1]
			else:	
				if matrix[i-1][j][1] > matrix[i][j-1][1]:
					matrix[i][j] = [None, matrix[i-1][j][1], i-1, j]
				else:
					matrix[i][j] = [None, matrix[i][j-1][1], i, j-1]
	return build(matrix)
	
def build(matrix):
	result = []
	i = len(matrix)-1
	j = len(matrix[0])-1
	while i != 0 and j != 0:
		if matrix[i][j][0] is not None:
			result.insert(0, matrix[i][j][0])
		i, j = matrix[i][j][2], matrix[i][j][3]
	return result
