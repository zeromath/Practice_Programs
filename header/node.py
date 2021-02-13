class Node:
    """Node for building tree-type structures

    Attributes:
        val: value for the current node
        children: a list or a dictionary of the descendents
    """
    
    def __init__(self, val=None, initializer=list):
        """Inits Node with val(None) and initializer(list)"""
        self.val = val
        self.children = initializer()

class BinaryTreeNode:
    """Node for building binary tree structures

    Attributes:
        val: value for the current node
        left_child: a BinaryTreeNode pointing to its left child
        right_child: a BinaryTreeNode pointing to its right child
    """
    
    def __init__(self, val=None):
        """Inits BinaryTreeNode with val"""
        self.val = val
        self.left_child = None
        self.right_child = None

    def in_order_traversal(self):
        if self.left_child:
            yield from self.left_child.in_order_traversal()
        yield self.val
        if self.right_child:
            yield from self.right_child.in_order_traversal()

    def post_order_traversal(self):
        if self.left_child:
            yield from self.left_child.in_order_traversal()
        if self.right_child:
            yield from self.right_child.in_order_traversal()
        yield self.val

    def pre_order_traversal(self):
        yield self.val
        if self.left_child:
            yield from self.left_child.in_order_traversal()
        if self.right_child:
            yield from self.right_child.in_order_traversal()


class DoubleLinkedBinaryTreeNode(BinaryTreeNode):
    
    def __init__(self, val=None):
        super().__init__(val=val)
        self.parent = None
