# O(N) T O(1) S
def isPalindrome(string):
    if len(string) == 0:
        return False
    elif len(string) == 1:
        return True
    else:
        return isPalindromeR(string, 0, len(string) - 1)


def isPalindromeR(string, leftPointer, rightPointer):
    if leftPointer >= rightPointer:
        return True
    elif string[leftPointer] != string[rightPointer]:
        return False
    else:
        return isPalindromeR(string, leftPointer + 1, rightPointer - 1)


# O(N) T O(1) S
def isPalindrome2(string):
    if len(string) == 0:
        return False
    elif len(string) == 1:
        return True
    else:
        leftPointer = 0
        rightPointer = len(string) - 1
        while leftPointer < rightPointer:
            if string[leftPointer] != string[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
        return True
