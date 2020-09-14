# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
		
	# O(N) T O(N) S
    def buildHeap(self, array):
        lastIndex = (len(array)-1)
		lastParentIndex = int((lastIndex-1)/2)
		while lastParentIndex >= 0:
			self.siftDown(lastParentIndex, array)
			lastParentIndex -= 1
		return array
	
	# O(logN) T O(1) S 
    def siftDown(self, index, array):
		while (2*index+1) <= len(array):
			currentNode = array[index]
			childOne, i1 = self.getChildOne(index, array)
			childTwo, i2 = self.getChildTwo(index, array)
			if min(childOne, childTwo) == childOne:
				minChild = childOne
				swapIndex = i1
			else:
				minChild = childTwo
				swapIndex = i2
			if minChild < currentNode:
				self.swap(index, swapIndex, array)
				index = swapIndex
			else:
				break
		return array

	# O(logN) T O(1) S 
    def siftUp(self, index, array):
        while index >= 0:
			parent, swapIndex = self.getParent(index)
			if parent > self.heap[index]:
				self.swap(index, swapIndex, array)
				index = swapIndex
			else:
				break
		return self.heap
	
	# O(1) T O(1) S 
    def peek(self):
        return self.heap[0]
	
	# O(logN) T O(1) S 
    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
		removed = self.heap[-1]
		self.heap = self.heap[:-1]
		self.siftDown(0, self.heap)
		return removed

	# O(logN) T O(1) S 
    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap)-1, self.heap)
	
	# O(1) T O(1) S
	def getChildOne(self, index, array):
		if 2*index+1 <= len(array)-1:
			return array[2*index+1], 2*index+1
		else:
			return float("inf"), -1
	
	# O(1) T O(1) S
	def getChildTwo(self, index, array):
		if 2*index+2 <= len(array)-1:
			return array[2*index+2], 2*index+2
		else:
			return float("inf"), -1
	
	# O(1) T O(1) S	
	def getParent(self, index):
		return self.heap[int((index-1)/2)], int((index-1)/2)
	
	# O(1) T O(1) S	
	def swap(self, index1, index2, array):
		array[index1], array[index2] = array[index2], array[index1]