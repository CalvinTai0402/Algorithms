# O(N^2) T O(1) S
def longestPeak(array):
    longestPeakLength = 0
    if len(array) > 2:
        for i in range(1, len(array) - 1):
            currentPeakLength = 0
            isPeak = False
            if array[i] > array[i - 1] and array[i] > array[i + 1]:
                isPeak = True
            if isPeak:
                currentPeakLength = 1
                j = i
                k = i
                while j >= 1 and array[j - 1] < array[j]:
                    j -= 1
                    currentPeakLength += 1
                while k < len(array) - 1 and array[k + 1] < array[k]:
                    k += 1
                    currentPeakLength += 1
            if currentPeakLength > longestPeakLength:
                longestPeakLength = currentPeakLength
    return longestPeakLength


# O(N) T O(1) S
def longestPeak2(array):
    longestPeakLength = 0
    if len(array) > 2:
        i = 1
        while i < len(array) - 1:
            currentPeakLength = 0
            if array[i] > array[i - 1] and array[i] > array[i + 1]:  # if isPeak
                currentPeakLength = 1
                j = i
                k = i
                while j >= 1 and array[j - 1] < array[j]:
                    j -= 1
                    currentPeakLength += 1
                while k < len(array) - 1 and array[k + 1] < array[k]:
                    k += 1
                    currentPeakLength += 1
                i = k
            if currentPeakLength > longestPeakLength:
                longestPeakLength = currentPeakLength
            i += 1
    return longestPeakLength
