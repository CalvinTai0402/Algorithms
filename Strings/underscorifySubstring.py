# O(N+M) T O(N) S
def underscorifySubstring(string, substring):
    locationMatrix = getLocations(string, substring)
	if locationMatrix == []:
		return string
	collapsedMatrix = collapseLocations(locationMatrix)
	return underscorify(collapsedMatrix, string)

# amortized O(N+M) T O(N) S
def getLocations(string, substring):
	locationMatrix = []
	index = string.find(substring)
	while index != -1:
		locationMatrix.append([index, index+len(substring)])
		index = string.find(substring, index+1)
	return locationMatrix

# O(N) T O(N) S
def collapseLocations(matrix):
	collapsedMatrix = []
	collapsedMatrix.append(matrix[0])
	i = 1
	while i < len(matrix):
		collapsedMatrix.append(matrix[i])
		if matrix[i][0] <= matrix[i-1][1]:
			collapsedMatrix[-2][1] = matrix[i][1]
			collapsedMatrix = collapsedMatrix[:-1]
		i += 1 
	return collapsedMatrix

# O(N) T O(N) S
def underscorify(collapsedMatrix, string):
	indices = [index for subList in collapsedMatrix for index in subList]
	stringList = []
	stringList[:0] = string
	j = 0
	for i in indices:
		stringList.insert(i+j,"_")
		j += 1
	return "".join(stringList)