# O(NlogN) T O(1) S
def largestRange(array):
    i = 0
    tempRange = 0
    largestRange = 0
    array.sort()
    firstNum = array[0]
    secondNum = array[0]
    result = [firstNum, secondNum]
    while i < len(array) - 1:
        if array[i] == array[i + 1] - 1:
            tempRange += 1
            secondNum = array[i + 1]
        elif array[i] == array[i + 1]:
            secondNum = array[i + 1]
        else:
            tempRange = 0
            firstNum = array[i + 1]
            secondNum = array[i + 1]
        if tempRange > largestRange:
            largestRange = tempRange
            result[0] = firstNum
            result[1] = secondNum
        i += 1
    return result


# O(N) T O(N) S
def largestRange2(array):
    result = []
    largestRange = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        tempRange = 1
        left = num - 1
        right = num + 1
        while left in nums:
            tempRange += 1
            nums[left] = False
            left -= 1
        while right in nums:
            tempRange += 1
            nums[right] = False
            right += 1
        if tempRange > largestRange:
            largestRange = tempRange
            result = [left + 1, right - 1]
    return result
