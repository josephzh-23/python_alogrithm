import math

from Binary_Search_Tree.BSTNode import Node



# Using the recurisve approach
"""
    Video by Kevin Naughton
"""

def isValidBSTRec(root):
    # these 2 values are none at the start but then will change
    #
    return validate(root, None, None)


def validateRec(root):

    return validate(root, float("-inf"), float("inf"))
    # Validate the left and the right
    # each iteration

def validate(node, left, right):
    if not node:
        return True

    if not (right > node.val > left):
        return False

    return validate(node.left, left, node.val) and \
           validate(node.right, node.val, right)

# ensure left and right exists

#testing this
# root = Node(4)
# root.left = Node(3)
# root.right = Node(5)
# print(isValidBSTRec(root))



# this is the solution contributed by Eric Programming

'''
Traverse the left side, middle and then right
using inOrder traverse, + with a prev pointer for comparison as said 
'''
def isValidBSTIter(root):
    # make use of recursion
    return inOrder(root)


prev = None

# We need to use a global previous value here, otherwise
# it will keep going to null
def inOrder(cur):

    global prev

    if cur is None:
        return True

    # traverse left side first
    isLeftBST = inOrder(cur.left)
    if not isLeftBST:
        return False

    # 3 cases for prev, if not visited
    if not prev:
        prev = cur.val

        # 5 > 3

    # Using inorder it can't be bigger then
    elif prev >= cur.val:
        return False

    elif prev < cur.val:
        prev = cur.val

    # traverse the right side
    isRightBST = inOrder(cur.right)
    if not isRightBST:
        return False

    # make it to here then return true
    return True


# This approach is good
root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(5)
print(isValidBSTIter(root))


print(validateRec(root))