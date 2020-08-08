# O(N) T O(1) S
def subarraySort(array):
    result = [-1, -1]
    truthy = []
    minUnsortedIndex = len(array)
    maxUnsortedIndex = -1
    min = float("inf")
    max = float("-inf")
    for i in range(len(array)):
        truthy.append(0)
    if array[0] > array[1]:
        minUnsortedIndex = 0
    if array[len(array) - 1] < array[len(array) - 2]:
        maxUnsortedIndex = len(array) - 1
    for i in range(1, len(array) - 1):
        if array[i] < array[i - 1] or array[i] > array[i + 1]:
            if minUnsortedIndex == len(array):
                minUnsortedIndex = i
                break
    for i in reversed(range(1, len(array) - 1)):
        if array[i] < array[i - 1] or array[i] > array[i + 1]:
            if maxUnsortedIndex == -1:
                maxUnsortedIndex = i
                break
    for i in range(minUnsortedIndex, maxUnsortedIndex + 1):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    if min < array[0]:
        result[0] = 0
    if max > array[len(array) - 1]:
        result[1] = len(array) - 1
    if result[0] != -1 and result[1] != -1:
        return result
    for i in range(1, len(array) - 1):
        if result[0] != -1:
            break
        if min >= array[i - 1] and min < array[i]:
            result[0] = i
            break
    for i in reversed(range(1, len(array) - 1)):
        if result[1] != -1:
            break
        if max > array[i] and max <= array[i + 1]:
            result[1] = i
            break
    return result
