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
        return node.height if node else -1
    
    def updateHeight(self, node):
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

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
            if self.getHeight(node.left) - self.getHeight(node.right) == 2:
                if key < node.left.key:
                    node = self.rightRotation(node)
                else:
                    node.left = self.leftRotation(node.left)
                    node = self.rightRotation(node)
        else:
            node.right = self.__put(key, node.right)
            if self.getHeight(node.right) - self.getHeight(node.left) == 2:
                if key < node.right.key:
                    node.right = self.rightRotation(node.right)
                    node = self.leftRotation(node)
                else:
                    node = self.leftRotation(node)
                    
        self.updateHeight(node)
        return node

    def findMin(self, node):
        return node if node.left is None else node.left
        
    def delete(self, key):
        if self.root is None:
            raise Exception("Cannot delete anything from an empty tree")
        else:
            self.root = self.__delete(key, self.root)
            
    def __delete(self, key, node):
        if not node:
            raise Exception("Element not in the tree")

        if key < node.key:
            node.left = self.__delete(key, node.left)
            if self.getHeight(node.right) - self.getHeight(node.left) == 2:
                if self.getHeight(node.right.right) >= self.getHeight(node.right.left):
                    node = self.leftRotation(node)
                else:
                    node.right = self.rightRotation(node.right)
                    node = self.leftRotation(node)
        elif key > node.key:
            node.right = self.__delete(key, node.right)
            if self.getHeight(node.left) - self.getHeight(node.right) == 2:
                if self.getHeight(node.left.left) >= self.getHeight(node.left.right):
                    node = self.rightRotation(node)
                else:
                    node.left = self.leftRotation(node.left)
                    node = self.rightRotation(node)
        else:
            if node.left and node.right:
                min_node = self.findMin(node.right)
                node.key = min_node.key
                node.right = self.__delete(min_node.key, node.right)
            else:
                if node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                else:
                    node = None

        if node:
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
#END OF AVLTREE
        
if __name__ == '__main__':
    a = [6, 4, 7, 3, 5, 1, 2]
    t = AVLTree()

    for i in a:
        t.put(i)
        t.printSelf(t.root)
        print()

    print()
    t.delete(6)
    t.printSelf(t.root)
    print()
    t.delete(4)
    t.printSelf(t.root)

