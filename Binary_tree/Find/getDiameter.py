
# The diameter of a binary tree
# is the length of the longest path between
# any two nodes in a tree.

"""
diameter formula = lh + rh
Consider followign:
    1           At 1, diameter = 5
  2   3         At 3, the diameter = lh + rh = 6
    4   6
  5       7         At 5 , diameter = 1
9           8

  return max(lheight + rheight, max(ldiameter, rdiameter))

"""

# The brute force approach


# The function Compute the "height" of a tree. Height is the
# number of nodes along the longest path from the root node
# down to the farthest leaf node.
from Binary_tree.BSTNode import TreeNode


def height(node):
    if node is None:
        return 0
    return 1 + max(findDiameter(node.left), findDiameter(node.right))


# Function to get the diameter of a binary tree
'''
TC: O (n^2) here 
'''
def diameterBrute(root):
    # Base Case when tree is empty
    if root is None:
        return 0

    lheight = findDiameter(root.left)
    rheight = findDiameter(root.right)

    # The line here gives O (n2)
    ldiameter = diameterBrute(root.left)
    rdiameter = diameterBrute(root.right)

    return max(lheight + rheight, max(ldiameter, rdiameter))


# Approach 2 here:
'''
This is the better approach, b/c it combines 
finding height with the diameter together

the formula:
     diameter = (left_height + right_height + 1)
     and we keep updating it 
'''

def findDiameter(root, ans):
    if (root == None):
        return 0

    left_height = findDiameter(root.l, ans)

    right_height = findDiameter(root.r, ans)

    # update the answer, because diameter
    # of a tree is nothing but maximum
    # value of (left_height + right_height + 1)
    # for each node
    ans[0] = max(ans[0], 1 + left_height +
                 right_height)

    # this is just how to find a height of a tree
    return 1 + max(left_height,
                   right_height)


# Computes the diameter of binary
# tree with given root.
def diameter(root):
    if (root == None):
        return 0

    # because using array we can store the reference
    # no pointer in python
    ans =  [-999999999999] # This will store
                          # the final answer


    height_of_tree = findDiameter(root, ans)
    return ans


# Driver code
if __name__ == '__main__':
    root = TreeNode(1)
    root.l = TreeNode(2)
    root.r = TreeNode(3)
    root.l.l = TreeNode(4)
    root.l.r = TreeNode(5)

    print("Diameter is", diameter(root))

# This code is contributed by PranchalK

# Driver Code
"""
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# # Function Call
# print(diameterBrute(root))

