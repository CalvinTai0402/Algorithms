# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) T O(1) S
def findLoop(head):
    first = head.next
	second = head.next.next
	while first is not second:
		first = first.next
		second = second.next.next
	first = head
	while first is not second:
		first = first.next
		second = second.next
	return first