
class Tree(object):
    def __init__(self, value):
        self.value = value
        self.left = 0
        self.right = 0

    def insertRight(self, node):
        self.right = node

    def insertLeft(self, node):
        self.left = node

    def binaryInsert(self, node):
        if self.value < node.value:
            if self.right == 0:
                self.right = node
            else:
                self.right.binaryInsert(node)
        if self.value > node.value:
            if self.left == 0:
                self.left = node
            else:
                self.left.binaryInsert(node)

    def binarySearch(self,val):
        if self.value == val:
            return True
        if self.value < val:
            if self.right == 0:
                return False
            return self.right.binarySearch(val)
        if self.left == 0:
            return False
        return self.left.binarySearch(val)