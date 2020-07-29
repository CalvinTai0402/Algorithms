# O(1) T O(1) S
# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def peekMinMax(self):
        return self.minMaxStack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            newMinMax["min"] = min(newMinMax["min"], self.peekMinMax()["min"])
            newMinMax["max"] = max(newMinMax["max"], self.peekMinMax()["max"])
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.peekMinMax()["min"]

    def getMax(self):
        return self.peekMinMax()["max"]
