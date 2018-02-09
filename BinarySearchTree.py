class Node:

    def __init__(self):
        self.right = None
        self.left = None
        self.value = None

    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
    

class Tree:

    def __init__(self, root):
        self.rootNode = root


    def addNode(self, value):
        n = Node()
        n.setValue(value)

        self.insertNode(n, self.rootNode)

    def insertNode(self, node, parent):
        if node.getValue() < parent.getValue():
            if parent.left is not None:
                self.insertNode(node, parent.left)
            else:
                parent.left = node

        if node.getValue() >= parent.getValue():
            if parent.right is not None:
                self.insertNode(node, parent.right)
            else:
                parent.right = node

    def findMin(self):
        if self.rootNode.left is None:
            print(self.rootNode.getValue())

        else: 
            self.findMinRec(self.rootNode.left)
        
    def findMinRec(self, node):
        if (node.left is None): 
            print(node.getValue())
        else:
            self.findMinRec(node.left)

    def printTree(self):
        print 'ROOT'
        print(self.rootNode.getValue())

        self.printChildren(self.rootNode)

    def printChildren(self, node):
        if node.right is not None:
            print 'Left Child of ' + str(node.getValue()) + '--> '
            print node.right.getValue()
        if node.left is not None:
            print 'Right Child of ' + str(node.getValue()) + '--> '
            print node.left.getValue()


        if node.left is not None:
            self.printChildren(node.left)

        if node.right is not None:
            self.printChildren(node.right)


r = Node()
r.setValue(10)
t = Tree(r)
t.findMin()
t.addNode(12)
t.addNode(20)
t.findMin()
t.addNode(2)
t.findMin()
t.addNode(3)
t.findMin()
t.addNode(1)
t.findMin()
t.addNode(200)
t.printTree()