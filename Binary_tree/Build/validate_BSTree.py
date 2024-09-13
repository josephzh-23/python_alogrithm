import math

from Binary_tree.BSTNode import TreeNode



# Using the recurisve approach
"""
   
"""

def validateRec(root):

    return validate(root, float("-inf"), float("inf"))
    # Validate the left and the right
    # each iteration

def validate(node, left, right):
    print("the left value is ", left)
    if not node:
        return True

    if not (right > node.val > left):
        return False

    # make sure left sub tree valid,
    # node.left always <  node.val
    return validate(node.l, left, node.val) and \
           validate(node.r, node.val, right)

    # make sure right sub tree valid are both valid
    # node.right always > node.val,

    # right and left will always be infinity as well




# ensure left and right exists

#testing this
# root = Node(4)
# root.left = Node(3)
# root.right = Node(5)
# print(isValidBSTRec(root))



#  GeeksForGeeks solution
# Function to check if a binary tree
# this is using in order traversal basically
def checkTreeIsBST(root: TreeNode) -> bool:

    Stack = []

    cur = root
    # Stores previous visited node
    prev = None

    while (Stack or cur):
        while cur:
            Stack.append(root)

            cur = cur.l

        cur = Stack.pop()

        # If root value < left child value
        if (prev and cur.data <= prev.data):
            return False

        prev = cur

        # Traverse right subtree
        # of the tree
        cur = cur.r

    return True


# This approach is good
root = TreeNode(4)
root.l = TreeNode(3)
root.r = TreeNode(6)
root.r.l = TreeNode(5)
root.r.r = TreeNode(7)
# print(isValidBSTIter(root))


print(validateRec(root))

