# O(d) T O(1) S
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    if descendantOne is topAncestor or descendantTwo is topAncestor:
        return topAncestor
    decendantOneDepth = 1
    decendantTwoDepth = 1
    descendantOneAncestor = descendantOne.ancestor
    descendantTwoAncestor = descendantTwo.ancestor
    while descendantOneAncestor is not topAncestor:
        descendantOneAncestor = descendantOneAncestor.ancestor
        decendantOneDepth += 1
    while descendantTwoAncestor is not topAncestor:
        descendantTwoAncestor = descendantTwoAncestor.ancestor
        decendantTwoDepth += 1
    depthDifference = abs(decendantOneDepth - decendantTwoDepth)
    descendantOneAncestor = descendantOne.ancestor
    descendantTwoAncestor = descendantTwo.ancestor
    if decendantOneDepth > decendantTwoDepth:
        while depthDifference != 0:
            if descendantOneAncestor is descendantTwo:
                return descendantTwo
            descendantOneAncestor = descendantOneAncestor.ancestor
            depthDifference -= 1
    elif decendantOneDepth < decendantTwoDepth:
        while depthDifference != 0:
            if descendantTwoAncestor is descendantOne:
                return descendantOne
            descendantTwoAncestor = descendantTwoAncestor.ancestor
            depthDifference -= 1
    while descendantOneAncestor is not descendantTwoAncestor:
        descendantOneAncestor = descendantOneAncestor.ancestor
        descendantTwoAncestor = descendantTwoAncestor.ancestor
    return descendantOneAncestor
