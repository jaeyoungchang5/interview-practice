#!/usr/bin/env python3

'''
Validate Binary Search Tree:
You are given the root of a binary search tree. 
Return true if it is a valid binary search tree, and false otherwise. 
Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.
'''

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    if is_bst_util(root, -100, 100):
        print('Valid BST')
    else:
        print('Invalid BST')

def is_bst_util(root, minimum, maximum):
    if root is None:
        return True
    
    if root.key < minimum or root.key > maximum:
        return False

    return is_bst_util(root.left, minimum, root.key) and is_bst_util(root.right, root.key, maximum)

def main():
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)

    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)
    #    5
    #   / \
    #  3   7
    # / \ /
    #1  4 6

    b = TreeNode(6)
    b.left = TreeNode(3)
    b.right = TreeNode(7)

    b.left.left = TreeNode(1)
    b.left.right = TreeNode(4)
    b.right.left = TreeNode(5)
    #    6
    #   / \
    #  3   7
    # / \ /
    #1  4 5

    is_bst(a)
    is_bst(b)

if __name__ == '__main__':
    main()
