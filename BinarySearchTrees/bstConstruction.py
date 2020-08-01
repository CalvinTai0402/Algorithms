# All methods have:
# Average: O(logN) T O(1) S
# Worst: O(N) T O(1) S, worst case when tree is skewed
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        while node is not None:
            if value < node.value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
                    continue
            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right
                    continue
        return self

    def contains(self, value):
        node = self
        while node is not None:
            if value < node.value:
                if node.left is None:
                    return False
                else:
                    node = node.left
                    continue
            elif value > node.value:
                if node.right is None:
                    return False
                else:
                    node = node.right
                    continue
            else:
                return True
        return False

    def remove(self, value):
        node = self
        parentNode = self
        if self.contains(value):
            while node is not None:
                if value < node.value:
                    parentNode = node
                    node = node.left
                    continue
                elif value > node.value:
                    parentNode = node
                    node = node.right
                    continue
                else:
                    if parentNode.right == node:
                        left = False
                        right = True
                    elif parentNode.left == node:
                        left = True
                        right = False
                    elif parentNode == node:  # Only happens when removing root node
                        left = False
                        right = False
                    if node.left is None and node.right is None:
                        if left:
                            parentNode.left = None
                        elif right:
                            parentNode.right = None
                        else:
                            return self  # single Node
                    elif node.left is not None and node.right is None:
                        if left:
                            parentNode.left = node.left
                        elif right:
                            parentNode.right = node.left
                        else:
                            parentNode.value = parentNode.left.value
                            temp = parentNode.left.left
                            parentNode.left.left = None
                            parentNode.left = temp
                    elif node.left is None and node.right is not None:
                        if left:
                            parentNode.left = node.right
                        elif right:
                            parentNode.right = node.right
                        else:
                            parentNode.value = parentNode.right.value
                            temp = parentNode.right.right
                            parentNode.right.right = None
                            parentNode.right = temp
                    elif node.left is not None and node.right is not None:
                        tempParentNode = node.right
                        tempNode = node.right
                        while tempNode.left is not None:
                            tempParentNode = tempNode
                            tempNode = tempNode.left
                        node.value = tempNode.value
                        if tempParentNode.left == tempNode:
                            tempLeft = True
                            tempRight = False
                        else:  # tempParentNode == tempNode
                            tempLeft = False
                            tempRight = False
                        if tempLeft:
                            tempParentNode.left = tempNode.right
                        else:
                            node.right = tempNode.right
                            tempNode.right = None
                    break
        return self
