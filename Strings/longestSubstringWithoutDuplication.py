# O(N) T O(A) S where A is the non-duplicate characters
def longestSubstringWithoutDuplication(string):
    longestSubstring = ""
	letterHashTable = {}
	startIndex = 0
	for i in range(len(string)):
		char = string[i]
		if char not in letterHashTable:
			letterHashTable[char] = i
		else:
			startIndex = max(startIndex, letterHashTable[char]+1)
			letterHashTable[char] = i
		substring = string[startIndex:i+1]
		if len(substring) > len(longestSubstring):	
			longestSubstring = substring
	return longestSubstring
