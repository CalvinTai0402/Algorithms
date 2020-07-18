# O(N^2) T O(1) S
def moveElementToEnd(array, toMove):
    pointer = 0
    while pointer<len(array): 
		if array[pointer]==toMove:
			for i in range(pointer+1, len(array)):
				if array[i]!=toMove:
					# swap(array, pointer, i)
					array[pointer],array[i] = array[i],array[pointer] #This is the easier swap
		pointer+=1
	return array

# def swap(array, indexOne, indexTwo):
# 	temp = array[indexOne]
# 	array[indexOne] = array[indexTwo]
# 	array[indexTwo] = temp
# 	return array

# O(N) T O(1) S
def moveElementToEnd(array, toMove):
    leftPointer = 0
    rightPointer = len(array)-1
    while leftPointer < rightPointer:
        while array[leftPointer] != toMove and leftPointer < rightPointer:
            leftPointer+=1
        while array[rightPointer] == toMove and leftPointer < rightPointer:
            rightPointer-=1
        array[leftPointer],array[rightPointer] = array[rightPointer],array[leftPointer]
    return array