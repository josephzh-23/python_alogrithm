# Recursive function to build a BST from a preorder sequence.
# start from the root node (the first element in a preorder sequence)
# set the root node's range as [-INFINITY, INFINITY]
import sys

from Binary_tree_manipulation.Build.build_tree_from_preOrder_array_bad_approach import inorder


'''
This is an improvement from the previous approach

where improved? 
O (n) 

different approach that doesn’t involve searching for an index that 
separates the left and right subtree keys in a preorder sequence:

The concept:
We know that each node has a key that is greater 
than all keys present in its left subtree, 
but less than the keys present in the right subtree of a BST. 

The idea to pass the information regarding 
the valid range of keys for the current root node and 
its children in the recursion itself.

Where it's improved
'''

def buildBST(preorder, pIndex=0, min=-sys.maxsize, max=sys.maxsize):
    # Base case
    if pIndex == len(preorder):
        return None, pIndex

    # Return if the next element of preorder traversal is not in the valid range
    val = preorder[pIndex]
    if val < min or val > max:
        return None, pIndex

    # Construct the root node and increment `pIndex`
    root = Node(val)
    pIndex = pIndex + 1

    # Since all elements in the left subtree of a BST must be less
    # than the root node's value, set range as `[min, val-1]` and recur
    root.l, pIndex = buildBST(preorder, pIndex, min, val - 1)

    # Since all elements in the right subtree of a BST must be greater
    # than the root node's value, set range as `[val+1…max]` and recur
    root.r, pIndex = buildBST(preorder, pIndex, val + 1, max)

    return root, pIndex


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

    # preorder traversal of BST
    preorder = [15, 10, 8, 12, 20, 16, 25]

    # construct the BST
    root = buildBST(preorder)[0]

    # print the BST
    print('Inorder traversal of BST is:', end=' ')

    # inorder on the BST always returns a sorted sequence
    inorder(root)