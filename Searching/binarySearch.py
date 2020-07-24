# O(logn) T O(1) S
def binarySearch(array, target):
    if len(array) == 0:
        return -1
    else:
        return binarySearchR(array, target, 0, len(array) - 1)


def binarySearchR(array, target, leftPointer, rightPointer):
    if leftPointer > rightPointer:
        return -1
    else:
        midPointer = (leftPointer + rightPointer) // 2
        if target == array[midPointer]:
            return midPointer
        elif target < array[midPointer]:
            return binarySearchR(array, target, leftPointer, midPointer - 1)
        else:
            return binarySearchR(array, target, midPointer + 1, rightPointer)

