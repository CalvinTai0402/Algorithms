# O(logN) T O(1) S
def findClosestValueInBst(tree, target):
    return findClosestValueInBstR(tree, target, tree.value)


def findClosestValueInBstR(node, target, closestNode):
    while node is not None:
        if abs(node.value - target) < abs(closestNode - target):
            closestNode = node.value
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right
        else:
            break
    return closestNode


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
