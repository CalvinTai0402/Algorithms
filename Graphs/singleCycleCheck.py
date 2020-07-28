# O(N) T O(1) S
def hasSingleCycle(array):
    i = 0
    index = 0
    while i < len(array):
        temp = array[index]
        index += temp
        while index < 0:
            index += len(array)
        while index >= len(array):
            index -= len(array)
        if i == len(array)-1 and index == 0: # If last cycle index is 0, return true
            return True
        elif index == 0: # If not last cycle index is 0, return false
            return False
        i += 1
    return False # index is not 0 when broken out of loop