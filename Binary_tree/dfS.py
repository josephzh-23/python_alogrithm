# A function to do inorder tree traversal

'''
Depth first traversal:
    In order traversal, post-order and pre-order are all
depth first traversal, and they all start from the bottom leaves

    1
  2   3
4   5
Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3         -> from the bottom here
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
Breadth-First or Level Order Traversal: 1 2 3 4 5

    if you want to trverse left first, add right to stack first
'''

from collections import deque

from Binary_tree.BSTNode import TreeNode

preOrder = [10, 4, 2, 8, 5, 9, 15, 12, 20]

def buildBSTreeFromPreorder(arr, start, end):

    start = 0
    end = len(arr)-1
    for i in range(len(arr)):
        if arr[i] >arr[start]:
            r = arr[i]
            r.l = buildBSTreeFromPreorder(arr[start:i], start + 1, i)
            r.r = buildBSTreeFromPreorder(arr[i: end], i + 1, end)

    return r














