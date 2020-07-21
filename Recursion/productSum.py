# O(N) T O(d) S
# N is the total number of elements, including sub-elements
# d is the greatest depth of all the special array, because at once we are using that many recursive calls on the call stack
def productSum(array, multiplier=1):
    sum = 0
    for item in array:
        if type(item) is not list:
            sum += item
        else:
            sum += productSum(item, multiplier + 1)
    return multiplier * sum

