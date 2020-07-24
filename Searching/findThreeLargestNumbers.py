# O(N) T O(1) S
def findThreeLargestNumbers(array):
    firstThree = [array[i] for i in range(3)]
    first = min(firstThree)
    firstThree.remove(first)
    third = max(firstThree)
    firstThree.remove(third)
    second = firstThree[0]
    for i in range(3, len(array)):
        if array[i] > first:
            if array[i] > second:
                if array[i] > third:
                    first, second, third = second, third, array[i]
                else:
                    second = array[i]
            else:
                first = array[i]
        else:
            continue
    return [first, second, third]

