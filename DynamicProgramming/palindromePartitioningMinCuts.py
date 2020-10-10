# O(N^3) T O(N) T
def palindromePartitioningMinCuts(string):
	palindromes = [[False for j in string] for i in string]
    for i in range(len(string)):
		for j in range(len(string)):
			palindromes[i][j] = isPalindrome(string[i:j+1])
	cuts = [float("inf") for i in string]
	for j in range(len(string)):
		if palindromes[0][j]:
			cuts[j] = 0
		else:
			cuts[j] = cuts[j-1]+1
			for i in range(1,j):
				if palindromes[i][j] and cuts[i-1]+1 < cuts[j]:
					cuts[j] = cuts[i-1]+1
	return cuts[-1]


def isPalindrome(string):
	leftPointer = 0
	rightPointer = len(string)-1
	while leftPointer < rightPointer:
		if string[leftPointer] != string[rightPointer]:
			return False
		leftPointer += 1
		rightPointer -= 1
	return True