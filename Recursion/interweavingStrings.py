# O(NM) T O(NM) S
def interweavingStrings(one, two, three):
    if len(one) + len(two) != len(three):
		return False
	cache = [[None for j in range(len(two)+1)] for i in range(len(one)+1)] # "+1" because i and j could possibly be len(one)/len(two)
	return interweavingStringsR(one, two, three, 0, 0, cache)
	
def interweavingStringsR(one, two, three, i, j, cache):
	if cache[i][j] is not None:
		return cache[i][j]
	print("hit")
	k = i + j
	if k == len(three): # when k == len(three), i == len(one) and j == len(two), which means all letter have been traversed
		return True
	if i < len(one) and one[i] == three[k]:
		cache[i+1][j] = interweavingStringsR(one, two, three, i+1, j, cache)
		if cache[i+1][j]:
			return True
	if j < len(two) and two[j] == three[k]:
		cache[i][j+1] = interweavingStringsR(one, two, three, i, j+1, cache)
		if cache[i][j+1]:
			return True
	cache[i][j] = False
	return False
