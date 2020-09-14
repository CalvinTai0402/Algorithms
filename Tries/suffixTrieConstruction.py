# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

	# O(N^2) T O(N^2) S
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
		return self.endSymbol in node
