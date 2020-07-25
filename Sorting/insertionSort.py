# O(N^2) T O(1) S
def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0:
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i -= 1
                j -= 1
                continue
            else:
                break
    return array
