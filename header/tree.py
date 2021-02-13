from node import *

class BinaryTree():
    
    INORDER = 0
    PREORDER = -1
    POSTORDER = 1
    NULLSYMBOL = '#'
    
    def __init__(self):
        self.head = None
        self.list_of_depths = []
        self.to_print = []
        self.depth = 0

    def print_traversal(self, order=INORDER):
        if order == BinaryTree.INORDER:
            print(list(self.head.in_order_traversal()))
        elif order == BinaryTree.POSTORDER:
            print(list(self.head.post_order_traversal()))
        elif order == BinaryTree.PREORDER:
            print(list(self.head.pre_order_traversal()))

    def __get_height(self, node):
        if not node:
            return -1
        return max(self.__get_height(node.left_child),
                   self.__get_height(node.right_child)) + 1

    def get_height(self):
        return self.__get_height(self.head)

    def __list_depths(self, node, depth):
        if not node:
            for i in range(self.depth-depth+1):
                self.list_of_depths[depth+i] += [self.NULLSYMBOL
                                                 for _ in range(2**i)]
        else:
            self.__list_depths(node.left_child, depth+1)
            self.list_of_depths[depth].append(node.val)
            self.__list_depths(node.right_child, depth+1)

    def list_depths(self):
        self.depth = self.get_height()+1
        self.list_of_depths = [[] for _ in range(self.depth+1)]
        self.__list_depths(self.head, 0)
        self.list_of_depths.pop()

    def print_tree(self, white_space_replace=False):
        self.list_depths()
        for i in range(self.depth):
            num_space = 2 ** (self.depth-i)
            s = [' '] * (num_space-1)
            num_space *= 2
            for item in self.list_of_depths[i]:
                s.append(str(item))
                s += [' '] * (num_space-1)
            new_s = "".join(s)
            if white_space_replace:
                print(new_s.replace(self.NULLSYMBOL, ' '))
            else:
                print(new_s)

    def __build_from_list(self, data):
        if not data:
            return None
        else:
            l = len(data) // 2
            new_node = BinaryTreeNode(data[l])
            new_node.left_child = self.__build_from_list(data[: l])
            new_node.right_child = self.__build_from_list(data[l+1 :])
        return new_node

    def build_from_list(self, data):
        self.head = self.__build_from_list(data)


def main():
    my_tree = BinaryTree()

    head = BinaryTreeNode(1)
    p = BinaryTreeNode(2)
    q = BinaryTreeNode(3)
    head.left_child = p
    head.right_child = q

    p.left_child = BinaryTreeNode(4)
    p.right_child = BinaryTreeNode(5)
    q.right_child = BinaryTreeNode(6)

    my_tree.head = head

    print("In order traversal")
    my_tree.print_traversal()
    print("Post order traversal")
    my_tree.print_traversal(BinaryTree.POSTORDER)
    print("Pre order traversal")
    my_tree.print_traversal(BinaryTree.PREORDER)

    print()
    print("Height of the tree")
    print(my_tree.get_height())

    print("Depths of each nodes")
    my_tree.list_depths()
    print(my_tree.list_of_depths)
    print(my_tree.depth)

    print("The tree:")
    my_tree.print_tree()
    

if __name__ == "__main__":
    main()
