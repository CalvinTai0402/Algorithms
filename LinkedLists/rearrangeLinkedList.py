# O(N) T O(1) S
def rearrangeLinkedList(head, k):
    smallerHead = None
	smallerTail = None
	equalHead = None
	equalTail = None
	greaterHead = None
	greaterTail = None
	node = head
	while node is not None:
		if node.value < k:
			smallerHead, smallerTail = growList(smallerHead, smallerTail, node)
		elif node.value > k:
			greaterHead, greaterTail = growList(greaterHead, greaterTail, node)
		else:
			equalHead, equalTail = growList(equalHead, equalTail, node)
		currNode = node
		node = currNode.next
		currNode.next = None
	newHead, newTail = connectHeadTail(smallerHead, smallerTail, equalHead, equalTail)
	newHead, newTail = connectHeadTail(newHead, newTail, greaterHead, greaterTail)
	return newHead

def growList(head, tail, node):
	newHead = head
	newTail = node
	if newHead is None:
		newHead = node
	if tail is not None:
		tail.next = node
	return newHead, newTail
	
# Only four cases: both lists None, first list None, second list None, both lists not None
def connectHeadTail(firstHead, firstTail, secondHead, secondTail):
	newHead = secondHead if firstHead is None else firstHead
	newTail = firstTail if secondTail is None else secondTail
	if firstTail is not None:
		firstTail.next = secondHead
	return newHead, newTail

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
