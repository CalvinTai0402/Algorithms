# O(N*2^N) T  O(N*2^N) S
# We have 2^N leaves (end points) because it's a power set, and each takes N steps to get to
def powerset(array):
    result = []
    result.append([])
    subArray = []
    if len(array) == 0:
        return result
    else:
        result.append(array)
        powersetRecursive(array, subArray, result)
        return result


def powersetRecursive(array, subArray, result):
    if len(array) == 0:
        return
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1 :]
            if newArray not in result:
                result.append(newArray)
            powersetRecursive(newArray, subArray, result)
