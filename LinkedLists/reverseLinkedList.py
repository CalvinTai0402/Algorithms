# O(N) T O(1) S
def reverseLinkedList(head):
    first = None
	second = head
	third = head.next
	while third is not None:
		second.next = first
		first = second
		second = third
		third = third.next
	second.next = first
	return second