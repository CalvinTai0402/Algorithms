# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(V+E) T O(V) S
    def depthFirstSearch(self, array):
        array.append(self.name)  # O(V)
        for i in range(len(self.children)):  # O(E)
            self.children[i].depthFirstSearch(array)
        return array
