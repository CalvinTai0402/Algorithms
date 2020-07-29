# O(N+M) T O(1) S
def searchInSortedMatrix(matrix, target):
    rowIndex = 0
    colIndex = len(matrix[0]) - 1
    while rowIndex < len(matrix) and colIndex >= 0:
        if matrix[rowIndex][colIndex] == target:
            return [rowIndex, colIndex]
        elif matrix[rowIndex][colIndex] > target:
            colIndex -= 1
        elif matrix[rowIndex][colIndex] < target:
            rowIndex += 1
    return [-1, -1]
