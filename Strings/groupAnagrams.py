# O(WNlogN) T O(WN) S
def groupAnagrams(words):
    dict = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		if dict.get(sortedWord) is None:
			dict[sortedWord] = [word]
		else:
			dict[sortedWord].append(word)
	return list(dict.values())