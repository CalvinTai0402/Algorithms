# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# O(N*N!) T O(N*N!) S, O(N*N!) S because we have N! permutations and each has a length of N
def getPermutations(array):
    result = []
    endIndex = len(array) - 1
    if len(array) == 0:
        return []
    else:
        getPermutationsRecursively(array, result, 0, endIndex)
        return result


def getPermutationsRecursively(array, result, startIndex, endIndex):
    if startIndex == endIndex:
        result.append(
            array.copy()
        )  # Will be hit N! times because that's how many permutations we have, copy is O(N). So, O(N!*N) here
    else:
        for i in range(
            startIndex, endIndex + 1
        ):  # O(N) here, compared to O(N*N!) this is insignificant
            array[startIndex], array[i] = array[i], array[startIndex]  # O(1)
            getPermutationsRecursively(array, result, startIndex + 1, endIndex)
            array[startIndex], array[i] = array[i], array[startIndex]  # O(1)

