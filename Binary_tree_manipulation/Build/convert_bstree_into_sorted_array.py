


# Using the recursive solution is faster actually
"""
   Input:  String_Array {1, 2, 3}  the middle one will be at the top
Output: A Balanced BST
     2
   /  \
  1    3

Input: String_Array {1, 2, 3, 4}
Output: A Balanced BST
      3
    /  \
   2    4
 /
1
"""
from Binary_tree.BSTNode import TreeNode
from Binary_tree.dfS import inOrderRec


def sortedArrayToBST(arr):

    if len(arr) ==0:
        return None

    return buildTreeFromArray(arr, 0, len(arr)-1)





arr = [1, 2, 3, 5, 7]
tree = sortedArrayToBST(arr)
# printLevelOrder(tree)
inOrderRec(tree)

# the midd
