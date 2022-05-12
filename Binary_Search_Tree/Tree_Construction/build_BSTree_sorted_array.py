


# Using the recursive solution is faster actually
"""
    [-10, -5, -3, 0, 5, 8, 9]
           0
       -5     8
    -10 -3   5  9
"""
from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.breath_first_search import printLevelOrder


def sortedArrayToBST(arr):

    if len(arr) ==0:
        return None

    return buildTreeFromArray(arr, 0, len(arr)-1)



def buildTreeFromArray(arr, left, right):

    if(left > right):
        return None

    mid = left + (right -left) //2

    node = Node(arr[mid])

    # Will target -5 on 2nd iter
    node.left = buildTreeFromArray(arr, left, mid-1)

    # target 8 on 2nd iteration
    node.right = buildTreeFromArray(arr, mid+1, right)

    return node

arr = [1, 2, 3, 5, 7]
tree = sortedArrayToBST(arr)
printLevelOrder(tree)


