# Time: O(N), Space: O(N)
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    branchSums = []
    getSums(root, 0, branchSums)
    return branchSums


def getSums(node, sumSoFar, branchSums):
    if node is None:
        return
    sumSoFar = sumSoFar + node.value
    if node.left is None and node.right is None:
        branchSums.append(sumSoFar)
        return
    getSums(node.left, sumSoFar, branchSums)
    getSums(node.right, sumSoFar, branchSums)

