# O(N) T O(1) S Note: pN, cN and nN are previousNode, currentNode and nextNode respectively
def iterativeInOrderTraversal(tree, callback):
    pN = None
	cN = tree
	while cN is not None:
		if pN is None or cN.parent == pN:
			if cN.left is not None:
				nN = cN.left
			else:
				callback(cN)
				nN = cN.right if cN.right is not None else cN.parent
		elif cN.left == pN:
			callback(cN)
			nN = cN.right if cN.right is not None else cN.parent
		elif cN.right == pN:
			nN = cN.parent
		pN = cN
		cN = nN
