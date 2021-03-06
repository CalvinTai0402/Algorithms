# O(N^2) T O(d) S
def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBsts(arrayOne, arrayTwo, rootOne, rootTwo, minVal, maxVal):
    if rootOne == -1 or rootTwo == -1:
        return rootOne == rootTwo
    if arrayOne[rootOne] != arrayTwo[rootTwo]:
        return False
    leftOne = getLeft(arrayOne, rootOne, minVal)
    leftTwo = getLeft(arrayTwo, rootTwo, minVal)
    rightOne = getRight(arrayOne, rootOne, maxVal)
    rightTwo = getRight(arrayTwo, rootTwo, maxVal)
    currentVal = arrayOne[rootOne]
    left = areSameBsts(arrayOne, arrayTwo, leftOne, leftTwo, minVal, currentVal)
    right = areSameBsts(arrayOne, arrayTwo, rightOne, rightTwo, currentVal, maxVal)
    return left and right


def getLeft(array, root, minVal):
    for i in range(root + 1, len(array)):
        if (
            array[i] < array[root] and array[i] >= minVal
        ):  # 81 needs to be smaller than 94 but bigger than 15
            return i
    return -1


def getRight(array, root, maxVal):
    for i in range(root + 1, len(array)):
        if (
            array[i] >= array[root] and array[i] < maxVal
        ):  # 6 needs to be greater than 5 but less than 8
            return i
    return -1
