# O(N) T O(N) S
def inOrderTraverse(tree, array):  # left, mid, right
    if tree is None:
        return
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):  # mid, left, right
    if tree is None:
        return
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):  # left, right, mid
    if tree is None:
        return
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array
