


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


def inOrderRec(root, res):


    if root:
        # First recur on left child
        inOrderRec(root.l, res)
        res.append(root.val)
        inOrderRec(root.r, res)





# the midd
root = TreeNode(5)
root.l = TreeNode(3)
root.r = TreeNode(7)
root.l.l = TreeNode(2)
root.l.r = TreeNode(4)

root.r.r = TreeNode(8)
root.r.l = TreeNode(6)
res = []

# and then using the code here is a bit different than the one you were looking at before
# here right? and that's why we are using the data in this table to work on this particular problem which
# makes more sense as time goes on here and then this will be even better than what you had
# before
inOrderRec(root, res)
# and these things should be available for uat now
print(res)


