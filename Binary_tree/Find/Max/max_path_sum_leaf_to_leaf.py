# Python program to find maximum path
# sum between two leaves of a binary tree


'''

The idea is to

To find the maximum path sum between two leaf nodes in a binary tree,

1. traverse each node and

recursively calculate the maximum sum from leaf to root in the left subtree of x (Find the maximum sum leaf to root path in a Binary Tree).

2. Find the maximum sum from leaf to root in the right subtree of x. Add the above two calculated values and x->data compare the sum with the maximum value obtained so far and update the maximum value. Return the overall maximum value. The time complexity of the above solution is O(n2).

And that's the solution above here
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def mxPathSum(root):
    global maxPathSum

    # Base case: If the node is null, return 0
    if root is None:
        return 0

    # Recursively calculate the maximum sum from
    # node to leaf for left and right subtrees
    mxLeft = mxPathSum(root.left)
    mxRight = mxPathSum(root.right)

    # If both left and right children exist,
    # update maxPathSum
    if root.left is not None and root.right is not None:

        # This is the sum of the left path,
        # right path, and the node's data
        maxSumPathViaNode = mxLeft + mxRight + root.data

        # Update the maximum sum path between
        # two leaves
        maxPathSum = max(maxPathSum, maxSumPathViaNode)

        # Return the maximum sum from the current node
        # to a leaf
        return root.data + max(mxLeft, mxRight)

    # If only one child exists, return the sum from the
    # node to leaf
    return root.data + (mxLeft if root.left else mxRight)


def findMaxSum(root):
    global maxPathSum

    # Edge case: If the tree is empty,
    # return 0
    if root is None:
        return 0

    maxPathSum = float('-inf')
    mxPathSum(root)

    return maxPathSum


# Construct a sample binary tree
#
#         1
#       /   \
#     -2     3
#     / \   / \
#    8  -1  4  -5


root = Node(1)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(8)
root.left.right = Node(-1)
root.right.left = Node(4)
root.right.right = Node(-5)

result = findMaxSum(root)
print(result)