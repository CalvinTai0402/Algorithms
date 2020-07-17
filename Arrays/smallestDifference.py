# O(NM) T O(1) S
def smallestDifference(arrayOne, arrayTwo):
	minDif = float("inf")
	for i in range(len(arrayOne)):
		for j in range(len(arrayTwo)):
			if abs(arrayOne[i]-arrayTwo[j]) < minDif:
				minDif = abs(arrayOne[i]-arrayTwo[j])
				RA = [arrayOne[i],arrayTwo[j]]
    return RA

#==============================AlgoExpert's answer====================================
# O(NlogN + MlogM) T O(1) S
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	i = 0
	j = 0
	smallest = float("inf")
	while i < len(arrayOne) and j < len(arrayTwo):
		firstNum = arrayOne[i]
		secondNum = arrayTwo[j]
		current = abs(arrayOne[i] - arrayTwo[j])
		if arrayOne[i] < arrayTwo[j]:
			i+=1
		elif arrayOne[i] > arrayTwo[j]:
			j+=1
		else:	# Two numbers are the same, i.e., closest possible so return straight away
			return [arrayOne[i],arrayTwo[j]]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum,secondNum]
	return smallestPair