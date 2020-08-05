# O(N^2) T, O(N) space
def threeNumberSum(array, targetSum):
    array.sort()
    twoDArray = []
    for i in range(len(array) - 2):
        leftPointer = i + 1
        rightPointer = len(array) - 1
        while leftPointer < rightPointer:
            if array[i] + array[leftPointer] + array[rightPointer] == targetSum:
                tempList = [array[i], array[leftPointer], array[rightPointer]]
                twoDArray.append(tempList)
                leftPointer += 1
                rightPointer -= 1
            elif array[i] + array[leftPointer] + array[rightPointer] < targetSum:
                leftPointer += 1
            else:
                rightPointer -= 1
    return twoDArray
