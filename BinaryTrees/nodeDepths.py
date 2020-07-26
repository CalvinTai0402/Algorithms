# O(N) T O(h) S where h is the maximum height/depth of the tree. Recall that a function is
# popped off the stack when the other is called
def nodeDepths(root):
    return nodeDepthsR(root, 0)


def nodeDepthsR(node, tempDepth):
    if node.left is None and node.right is None:
        return tempDepth
    elif node.left is not None and node.right is not None:
        return (
            tempDepth
            + nodeDepthsR(node.left, tempDepth + 1)
            + nodeDepthsR(node.right, tempDepth + 1)
        )
    elif node.left is not None and node.right is None:
        return tempDepth + nodeDepthsR(node.left, tempDepth + 1)
    elif node.left is None and node.right is not None:
        return tempDepth + nodeDepthsR(node.right, tempDepth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
