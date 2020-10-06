# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N) T O(N) S
def flattenBinaryTree(root):
	inOrderNodes = inOrderTraverse(root, [])
	for i in range(len(inOrderNodes)-1):
		leftNode = inOrderNodes[i]
		rightNode = inOrderNodes[i+1]
		leftNode.right = rightNode
		rightNode.left = leftNode
    return inOrderNodes[0]

# O(N) T O(d) S
def inOrderTraverse(node, array):
	if node is None:
		return
	inOrderTraverse(node.left, array)
	array.append(node)
	inOrderTraverse(node.right, array)
	return array

#======================================Solution 2==============================================

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N) T O(d) S
def flattenBinaryTree(root):
    leftMost, _ = flattenBinaryTreeR(root)
	return leftMost
	
def flattenBinaryTreeR(node):
	if node.left is None:
		leftMost = node
	else:
		leftTreeLeftMost, leftTreeRightMost = flattenBinaryTreeR(node.left)
		connectTwo(leftTreeRightMost, node)
		leftMost = leftTreeLeftMost
	if node.right is None:
		rightMost = node
	else:
		rightTreeLeftMost, rightTreeRightMost = flattenBinaryTreeR(node.right)
		connectTwo(node, rightTreeLeftMost)
		rightMost = rightTreeRightMost
	return [leftMost, rightMost]
	
def connectTwo(left, right):
	left.right = right
	right.left = left