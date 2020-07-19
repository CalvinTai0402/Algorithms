# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) T O(1) S
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) T O(1) S
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # O(1) T O(1) S, O(1) T because we have a reference to "node"
    def insertBefore(self, node, nodeToInsert):
        # if nodeToInsert == self.head and nodeToInsert == self.tail:
        #     return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) T O(1) S
    def insertAfter(self, node, nodeToInsert):
        # if nodeToInsert == self.head and nodeToInsert == self.tail:
        #     return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(p) T O(1) S, O(p)'s average O(N/2) = O(N)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:  # We assume position starts at 1 not 0
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(node, nodeToInsert)

    # O(N) T O(1) S
    def removeNodesWithValue(self, value):
        tempNode = self.head
        while tempNode is not None:
            potentialNode = tempNode
            tempNode = tempNode.next
            if potentialNode.value == value:
                self.remove(potentialNode)

    # O(1) T O(1) S
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removePointers(node)

    # O(N) T O(1) S
    def containsNodeWithValue(self, value):
        tempNode = self.head
        while tempNode is not None and tempNode.value != value:
            tempNode = tempNode.next
        return tempNode is not None

    # O(1) T O(1) S
    def removePointers(self, node):
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        node.prev = None
        node.next = None
