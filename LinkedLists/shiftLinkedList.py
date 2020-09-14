# O(N) T O(1) S
def shiftLinkedList(head, k):
	k = k % 6
	temp = head
	length = 1
	while temp.next is not None:
		temp = temp.next
		length += 1
	currentTail = temp
	currentHead = head
    if k == 0:
		return head
	elif k > 0:
		newTailIndex = length - k - 1
	else:
		newTailIndex = abs(k) - 1
	tempIndex = 0
	newTail = currentHead
	while tempIndex != newTailIndex:
		newTail = newTail.next
		tempIndex += 1
	head = newTail.next
	currentTail.next = currentHead
	newTail.next = None
	return head

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
