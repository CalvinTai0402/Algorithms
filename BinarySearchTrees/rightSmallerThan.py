# O(N^2) T O(N) S
def rightSmallerThan(array):
    result = []
    for i in range(len(array)):
        counter = 0
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                counter += 1
        result.append(counter)
    return result
