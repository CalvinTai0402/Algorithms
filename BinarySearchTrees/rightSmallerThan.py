# O(N^2) T O(N) S
def rightSmallerThan(array):
    result = []
    for i in range(len(array)):
        counter = 0
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                counter += 1
        result.append(counter)
    return result


#========================================Solution 2=======================================

# O(NlogN) T O(N) S
def rightSmallerThan(array):
	if len(array)==0:
		return []
    rightSmallerThan = array[:]
	rightSmallerThan[-1] = 0
	bst = RSTBST(array[len(array)-1])
	for i in reversed(range(len(array)-1)):
		bst.insert(array[i], i, rightSmallerThan)
	return rightSmallerThan

class RSTBST:
	def __init__(self, value):
		self.value = value
		self.leftSubTreeSize = 0
		self.left = None
		self.right = None
	
	def insert(self, value, index, rightSmallerThan, numSmallerThan=0):
		if value < self.value:
			self.leftSubTreeSize += 1
			if self.left is None:
				self.left = RSTBST(value)
				rightSmallerThan[index] = numSmallerThan
			else:
				self.left.insert(value, index, rightSmallerThan, numSmallerThan)
		else:
			numSmallerThan += self.leftSubTreeSize
			if value > self.value:
				numSmallerThan += 1
			if self.right is None:
				self.right = RSTBST(value)
				rightSmallerThan[index] = numSmallerThan
			else:
				self.right.insert(value, index, rightSmallerThan, numSmallerThan)