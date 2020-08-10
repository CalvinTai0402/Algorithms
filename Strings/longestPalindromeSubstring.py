# O(N^2) T O(1) S
def longestPalindromicSubstring(string):
    longestPalindromeIndices = [0, 1]
    for i in range(len(string)):
        odd = getLongestPalindrome(string, i - 1, i + 1)
        even = getLongestPalindrome(string, i - 1, i)
        tempLongest = max(odd, even, key=lambda x: x[1] - x[0])
        longestPalindromeIndices = max(
            tempLongest, longestPalindromeIndices, key=lambda x: x[1] - x[0]
        )
    return string[longestPalindromeIndices[0] : longestPalindromeIndices[1]]


def getLongestPalindrome(string, leftPointer, rightPointer):
    while leftPointer >= 0 and rightPointer < len(string):
        if string[leftPointer] != string[rightPointer]:
            break
        leftPointer -= 1
        rightPointer += 1
    return [
        leftPointer + 1,
        rightPointer,
    ]  # No need to -1 for rightPointer since we will be slicing the string

