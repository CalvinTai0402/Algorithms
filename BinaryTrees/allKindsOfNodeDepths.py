# O(NlogN) T O(d) S
def allKindsOfNodeDepths(root):
    if root is None:
		return 0
	return nodeDepth(root) + allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right)

def nodeDepth(root, depth=0):
	if root is None:
		return 0
	return depth + nodeDepth(root.left, depth+1) + nodeDepth(root.right, depth+1)
	
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#========================================Solution 2=============================================


#O(N) T O(d) S 
def allKindsOfNodeDepths(root, depthSum=0, depth=0):
    if root is None:
		return 0
	depthSum += depth
	return (depthSum+
	allKindsOfNodeDepths(root.left, depthSum, depth+1)+
	allKindsOfNodeDepths(root.right, depthSum, depth+1))

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
