# O(N) T O(d) S
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(root):
	return validateBstR(root, float("-inf"), float("inf"))
	
def validateBstR(root, min, max):
	if root is None:
		return True
	if root.value < min or root.value >= max:
		return False
	return validateBstR(root.left, min, root.value) and validateBstR(root.right, root.value, max)