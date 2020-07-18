# O(N) T O(N) S
def spiralTraverse(array):
    myArray = []
    startRow = 0
    startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1
    while startRow < endRow and startCol < endCol:
        for col in range(startCol, endCol + 1):
            myArray.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            myArray.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)):
            myArray.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow)):
            myArray.append(array[row][startCol])
        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
    # Edge Cases
    if startRow == endRow and startCol != endCol:
        for col in range(startCol, endCol + 1):
            myArray.append(array[startRow][col])
    elif startRow != endRow and startCol == endCol:
        for row in range(startRow, endRow + 1):
            myArray.append(array[row][startCol])
    elif startRow == endRow and startCol == endCol:
        myArray.append(array[startRow][startCol])
    return myArray
