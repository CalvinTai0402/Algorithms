# O(M+N^2) T O(M+N) S
def patternMatcher(pattern, string):
	newPattern, swap = getNewPattern(pattern)
	print(newPattern)
	counts, firstYIndex = getCountsAndFirstYIndex(newPattern)
	xLength = 1
	while xLength < len(string):
		if counts["y"] != 0:
			yLength = (len(string)-(xLength*counts["x"]))/counts["y"]
			yLength = int(yLength)
		else:
			yLength = 0
		if yLength % 1 != 0:
			xLength += 1
			continue
		x = string[0:xLength]
		y = string[firstYIndex*xLength:firstYIndex*xLength+yLength]
		potentiallyMatchingString = "".join(list(map(lambda char: x if char == "x" else y, newPattern)))
		if string == potentiallyMatchingString:
			if swap:
				return [y,x]
			else:	
				return[x,y]
		xLength += 1
	return []

def getNewPattern(pattern):
	swap = False
	if pattern[0] == "x":
		return list(pattern), swap
	newPattern = list(map(lambda letter: "x" if letter == "y" else "y", pattern))
	swap = True
	return newPattern, swap
	
def getCountsAndFirstYIndex(newPattern):
	counts = {"x": 0, "y": 0}
	firstYIndex = 0
	flag = 0
	for index, letter in enumerate(newPattern):
		if letter == "x":
			counts["x"] += 1
		else:
			if flag == 0:
				firstYIndex = index
				flag = 1
			counts["y"] += 1
	return counts, firstYIndex