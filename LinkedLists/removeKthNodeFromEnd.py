# O(N) T O(1) S
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    node = head
    length = 0
    while node is not None:
        node = node.next
        length += 1
    position = length - k + 1  # We assume position starts from 1
    node = head
    prevNode = head
    currentPosition = 1
    while (
        currentPosition != position
    ):  # After this loop, node will be the node to be removed
        prevNode = node
        node = node.next
        currentPosition += 1
    if node == head:
        head.value = node.next.value
        head.next = node.next.next
        node = None
        prevNode = None
    else:
        prevNode.next = node.next
        node.next = None
