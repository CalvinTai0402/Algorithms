# O(N^2) T O(N) S
def fourNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):
            leftPointer = j + 1
            rightPointer = len(array) - 1
            while leftPointer < rightPointer:
                if (
                    array[i] + array[j] + array[leftPointer] + array[rightPointer]
                    == targetSum
                ):
                    result.append(
                        [array[i], array[j], array[leftPointer], array[rightPointer]]
                    )
                    leftPointer += 1
                    rightPointer -= 1
                elif (
                    array[i] + array[j] + array[leftPointer] + array[rightPointer]
                    < targetSum
                ):
                    leftPointer += 1
                else:
                    rightPointer -= 1
    return result
