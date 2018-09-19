class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0
# END OF NODE

class AVLTree(object):
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        return -1 if node is None else node.height
    
    def updateHeight(self, node):
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

    def isUnbalance(self, node):
        return abs(self.getHeight(node.left) - self.getHeight(node.right)) > 1

    def rightRotation(self, node):
        node_right = node
        node = node.left
        node_right.left = node.right
        node.right = node_right

        self.updateHeight(node_right)
        self.updateHeight(node)
        return node

    def leftRotation(self, node):
        node_left = node
        node = node.right
        node_left.right = node.left
        node.left = node_left

        self.updateHeight(node_left)
        self.updateHeight(node)
        return node

    def put(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self.__put(key, self.root)

    def __put(self, key, node):
        if node is None:
            node = Node(key)
        elif key < node.key:
            node.left = self.__put(key, node.left)
            if self.isUnbalance(node):
                if key < node.left.key:
                    node = self.rightRotation(node)
                else:
                    node.left = self.leftRotation(node.left)
                    node = self.rightRotation(node)
        else:
            node.right = self.__put(key, node.right)
            if self.isUnbalance(node):
                if key < node.right.key:
                    node.right = self.rightRotation(node.right)
                    node = self.leftRotation(node)
                else:
                    node = self.leftRotation(node)
                    
        self.updateHeight(node)
        return node

    def printSelf(self, node):
        if node == None:
            return
        s = ""
        s += str(node.key)
        s += " "
        s += str(node.left.key) if node.left else "None"
        s += " "
        s += str(node.right.key) if node.right else "None"
        print(s)
        self.printSelf(node.left)
        self.printSelf(node.right)

if __name__ == '__main__':
    a = [6, 4, 7, 3, 5, 1, 2]
    t = AVLTree()

    for i in a:
        t.put(i)
        print(t.getHeight(t.root))
        t.printSelf(t.root)
        print()

