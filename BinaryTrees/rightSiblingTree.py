# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N) T O(d) S
def rightSiblingTree(root):
    mutate(root, None, False)
	return root
	
def mutate(node, parent, isLeftChild):
	if node is None:
		return
	left, right = node.left, node.right
	mutate(left, node, True)
	if parent is None:
		node.right = None
	elif isLeftChild:
		node.right = parent.right
	elif not isLeftChild:
		if parent.right is None:
			node.right = None
		else:
			node.right = parent.right.left
	mutate(right, node, False)
