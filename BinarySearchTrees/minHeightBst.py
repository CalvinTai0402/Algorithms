# O(N) T O(N) S
def minHeightBst(array):
    return constructminHeightBst(array, 0, len(array) - 1)


def constructminHeightBst(array, startIndex, endIndex):
    if endIndex < startIndex:
        return None
    midIndex = (startIndex + endIndex) // 2
    bst = BST(array[midIndex])
    bst.left = constructminHeightBst(array, startIndex, midIndex - 1)
    bst.right = constructminHeightBst(array, midIndex + 1, endIndex)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
