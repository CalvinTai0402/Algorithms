# O(N) T O(1) S
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first, second = second, current
    return second
