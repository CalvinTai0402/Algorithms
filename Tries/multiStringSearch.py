# O(b^2+ns) T O(b^2+n) S where b/s is the length of bigString/smallStrings and
# n is the length of the result array
def multiStringSearch(bigString, smallStrings):
    result = []
	suffixTrie = SuffixTrie(bigString)
	for string in smallStrings:
		result.append(suffixTrie.contains(string))
    return result


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

	# O(b^2) T O(b^2) S
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			self.insertToTrie(i, string)

	def insertToTrie(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = True
	
	# O(M) T O(1) S where M is the length of the string to search
    def contains(self, string):
        node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return True

# O(bs+ns) T O(n+ns+n) S == O(ns) S where b/s is the length of bigString/smallStrings and
# n is the length of the result array
def multiStringSearch1(bigString, smallStrings):
	suffixTrie = SuffixTrie()
	for string in smallStrings:
		suffixTrie.insertToTrie(string)
	containedStrings = {}
	for i in range(len(bigString)):
		if bigString[i] not in suffixTrie.root:
			continue
		slicedBigString = bigString[i:]
		suffixTrie.contains(slicedBigString, containedStrings)
    return [string in containedStrings for string in smallStrings]


class SuffixTrie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

	def insertToTrie(self, string):
		node = self.root
		for j in range(len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = string
	
	# O(M) T O(1) S where M is the length of the string to search
    def contains(self, string, containedStrings):
        node = self.root
		for letter in string:
			if letter not in node:
				break
			node = node[letter]
			if self.endSymbol in node:
				containedStrings[node[self.endSymbol]] = 1