'''

The native solution

1. Check every pth O(n *h) time
The idea is to check of all possible path from root to leaf recursively. So we check for every path that is from root to every leaf and take the sum which path has the maximum sum.
Not good here

The idea is to keep track of
O(n)
curSum and maxSum here
 traversing the tree and update maximum sum if at leaf node current sum > them maximum sum.


Follow the steps below to solve the problem:

If the node is the root, return its data.

If the node is a leaf, Check where current sum > maximum sum, then update maximum sum.
For non-leaf nodes, update current sum and make recursive call on both left and right child.
'''


# Python program to find maximum sum leaf
# to root path in Binary Tree

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# Helper function to find the leaf node that contributes
# to the maximum sum and returns the maximum sum from the
# root to that leaf
def findMaxSum(root, currSum, mxSum):
    if root is None:
        return

    # Add the current node's data to the path sum
    currSum += root.data

    # Check if this node is a leaf node
    if root.left is None and root.right is None:

        # Update the maximum sum if a higher sum is found
        if currSum > mxSum[0]:
            mxSum[0] = currSum

    # Recursively check for the maximum sum
    # in the left and right subtrees
    findMaxSum(root.left, currSum, mxSum)
    findMaxSum(root.right, currSum, mxSum)


# Function to return the maximum sum path
# from root to leaf
def maxPathSum(root):
    # Empty tree has sum 0
    if root is None:
        return 0

    # Initialize max sum as the smallest possible integer
    mxSum = [-float('inf')]

    # Find the target leaf and maximum sum
    findMaxSum(root, 0, mxSum)

    # Return the maximum sum found
    return mxSum[0]


if __name__ == "__main__":
    # Constructing tree:
    #           10
    #         /    \
    #       -2      7
    #      /  \
    #     8   -4
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(-4)

    sum = maxPathSum(root)
    print(sum)