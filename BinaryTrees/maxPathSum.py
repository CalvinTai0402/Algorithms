# O(N) T O(log(N)) S
def maxPathSum(tree):
    _, maxPS = maxPathSumR(tree)
    return maxPS
	
def maxPathSumR(tree):
	if tree is None:
		return(0, float("-inf"))
	LSB, LS = maxPathSumR(tree.left) # leftSumBranch, leftSum
	RSB, RS = maxPathSumR(tree.right) # rightSumBranch, rightSum
	MCSB = max(LSB,RSB) # maxChildSumBranch
	MSB = max(MCSB+tree.value, tree.value) # maxSumBranch
	MST = max(MSB, LSB + tree.value + RSB) # maxSumTriangle
	RMPS = max(LS, RS, MST) # runningMaxPathSum
	return MSB, RMPS
