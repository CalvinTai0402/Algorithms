# O(NlogN) T O(N) S
def mergeSort(array):
    if len(array) <= 1:
        return array
    auxArray = array[:]
    mergeSortR(array, auxArray, 0, len(array) - 1)
	return array


def mergeSortR(array, auxArray, startIdx, endIdx):
    if startIdx == endIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    mergeSortR(auxArray, array, startIdx, midIdx)
    mergeSortR(auxArray, array, midIdx + 1, endIdx)
    merge(array, auxArray, startIdx, midIdx, endIdx)


def merge(array, auxArray, startIdx, midIdx, endIdx):
    i = k = startIdx
    j = midIdx + 1
    while i <= midIdx and j <= endIdx:
        if auxArray[i] <= auxArray[j]:
            array[k] = auxArray[i]
            i += 1
        else:
            array[k] = auxArray[j]
            j += 1
        k += 1
    while i <= midIdx:
        array[k] = auxArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        array[k] = auxArray[j]
        j += 1
        k += 1
