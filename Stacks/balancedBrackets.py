# O(N) T O(N) S
def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = "}])"
    matchingBrackets = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            elif char == matchingBrackets[stack[len(stack) - 1]]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
