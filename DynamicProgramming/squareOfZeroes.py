# O(N^4) T O(1) S
def squareOfZeroes(matrix):
    n = len(matrix)
	for topRow in range(n-1):
		for leftCol in range(n-1):
			squareLength = 2
			while squareLength <= n-topRow and squareLength <= n-leftCol:
				bottomRow = topRow+squareLength-1
				rightCol = leftCol+squareLength-1
				if isSquareOfZeroes(topRow, bottomRow, leftCol, rightCol, matrix):
					return True
				squareLength += 1
	return False
	
def isSquareOfZeroes(r1, r2, c1, c2, matrix):
	for col in range(c1, c2+1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False
	for row in range(r1, r2+1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False
	return True

#===========================================Solution 2==============================================
# O(N^3) T O(N^2) S
def squareOfZeroes(matrix):
	infoMatrix = precomputeMatrix(matrix)
    n = len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n-topRow and squareLength <= n-leftCol:
				bottomRow = topRow+squareLength-1
				rightCol = leftCol+squareLength-1
				if isSquareOfZeroes(topRow, bottomRow, leftCol, rightCol, infoMatrix, squareLength):
					return True
				squareLength += 1
	return False

def precomputeMatrix(matrix):
	infoMatrix = [[col for col in row] for row in matrix]
	n = len(infoMatrix)
	for row in range(n):
		for col in range(n):
			numOfZeroes = 1 if infoMatrix[row][col] == 0 else 0
			infoMatrix[row][col] = {
				"numZeroesRight": numOfZeroes,
				"numZeroesBelow": numOfZeroes
			}
	for row in reversed(range(n)):
		for col in reversed(range(n)):
			if matrix[row][col] == 1:
				continue
			if row < n-1:
				infoMatrix[row][col]["numZeroesBelow"] += infoMatrix[row+1][col]["numZeroesBelow"]
			if col < n-1:
				infoMatrix[row][col]["numZeroesRight"] += infoMatrix[row][col+1]["numZeroesRight"]
	return infoMatrix

	
def isSquareOfZeroes(r1, r2, c1, c2, infoMatrix, squareLength):
	hasLeftBorder = infoMatrix[r1][c1]["numZeroesBelow"] >= squareLength
	hasTopBorder = infoMatrix[r1][c1]["numZeroesRight"] >= squareLength
	hasBottomBorder = infoMatrix[r2][c1]["numZeroesRight"] >= squareLength
	hasRightBorder = infoMatrix[r1][c2]["numZeroesBelow"] >= squareLength
	return hasLeftBorder and hasTopBorder and hasBottomBorder and hasRightBorder