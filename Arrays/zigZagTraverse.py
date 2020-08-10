# O(N) T O(N) S
def zigzagTraverse(array):
    firstRow = 0
    lastRow = len(array) - 1
    firstCol = 0
    lastCol = len(array[0]) - 1
    currentRow = 0
    currentCol = 0
    result = []
    downOrUp = 0  # 0 is diagonally down, 1 is diagonally up
    while True:
        result.append(array[currentRow][currentCol])
        if currentRow == lastRow and currentCol == lastCol:
            break
        if downOrUp == 0:
            if currentRow == lastRow:  # trumps elif
                currentCol += 1
                downOrUp = 1
            elif currentCol == firstCol:
                currentRow += 1
                downOrUp = 1
            else:
                currentRow += 1
                currentCol -= 1
        else:
            if currentCol == lastCol:  # trumps elif
                currentRow += 1
                downOrUp = 0
            elif currentRow == firstRow:
                currentCol += 1
                downOrUp = 0
            else:
                currentRow -= 1
                currentCol += 1
    return result
