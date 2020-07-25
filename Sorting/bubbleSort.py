# O(N^2) T O(1) S
def bubbleSort(array):
    maxIndex = len(array) - 1
    while 0 < maxIndex:
        flag = 0
        for i in range(maxIndex):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = 1
        if flag == 0:
            break
        else:
            maxIndex -= 1
            continue
    return array

