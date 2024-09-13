

'''
https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
'''
from Binary_tree.BSTNode import TreeNode

'''

# method 1 O (n^2)

For example in {10, 5, 1, 7, 40, 50}, 10 is the first element, 
so we make it root. 

Now we look for the first element greater than 10, we find 40. 

Everything to left of 40 will be on left
Everything to right of 40 will be on right 
So we know the structure of BST is as following. 

             10
           /    \
          /      \
  {5, 1, 7}       {40, 50}
'''


#TC: O (n^2)

# Recursive function to build a BST from a preorder sequence.
def buildBSTreeFromPreorder(array, start, end):


    # base case
    if start > end:
        return None

    # Construct the root node of the subtree formed by keys of the
    # preorder sequence in range `[start, end]`

    node = TreeNode(array[start])

    # search for the 1st element > the root node's value
    i = start
    while i <= end:
        if array[i] > node.key:
            break
        i = i + 1

    # recursively construct the left subtree
    node.l = buildBSTreeFromPreorder(array, start + 1, i - 1)

    # recursively construct the right subtree
    node.r = buildBSTreeFromPreorder(array, i, end)

    # return current node
    return node


# A class to store a binary tree node
class Node:
    def __init__(self, key):
        self.key = key


# Recursive function to perform inorder traversal on a given binary tree
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.key, end=' ')
    inorder(root.right)


if __name__ == '__main__':
    ''' Construct the following BST
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
    '''

    preorder = [15, 10, 8, 12, 20, 16, 25]

    # construct the BST
    root = buildBSTreeFromPreorder(preorder, 0, len(preorder) - 1)

    # print the BST
    print('Inorder traversal of BST is ', end='')

    # inorder on the BST always returns a sorted sequence
    inorder(root)


