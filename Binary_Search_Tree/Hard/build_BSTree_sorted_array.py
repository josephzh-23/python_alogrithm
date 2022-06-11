


# Using the recursive solution is faster actually
"""
   Input:  Array_hash {1, 2, 3}  the middle one will be at the top
Output: A Balanced BST
     2
   /  \
  1    3

Input: Array_hash {1, 2, 3, 4}
Output: A Balanced BST
      3
    /  \
   2    4
 /
1
"""
from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.breath_first_search import printLevelOrder
from Binary_Search_Tree.depth_first_search import inOrderRec


def sortedArrayToBST(arr):

    if len(arr) ==0:
        return None

    return buildTreeFromArray(arr, 0, len(arr)-1)



def buildTreeFromArray(arr, left, right):

    if(left > right):
        return None

    mid = left + (right -left) //2

    node = Node(arr[mid])

    node.left = buildTreeFromArray(arr, left, mid-1)
    node.right = buildTreeFromArray(arr, mid+1, right)

    return node

arr = [1, 2, 3, 5, 7]
tree = sortedArrayToBST(arr)
# printLevelOrder(tree)
inOrderRec(tree)

# the midd
