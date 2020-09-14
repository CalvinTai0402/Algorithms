# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N+M) T O(1) S
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
	p2 = headTwo
	pre = None
	while p1 is not None and p2 is not None:
		if p1.value >= p2.value:
			if pre is not None:
				pre.next = p2
			pre = p2
			p2 = p2.next
			pre.next = p1
		else:
			pre = p1
			p1 = p1.next
	if p1 is None:
		pre.next = p2
	return headOne if headOne.value < headTwo.value else headTwo
