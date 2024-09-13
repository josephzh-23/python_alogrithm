'''

This is the optimal solution approach here

More better solution
keep traversing the tree and check if it's a bst here

Use bottom up to traverse tree

1) The tree's strucutre needs changed to the following:
minNode`: minimum value of the subtree
`maxNode`: maximum value of the subtree.
`maxSize`: maximum size of the BST encountered so far



'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# this is a key structure here
class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize

class Solution:
    # Helper function to find the
    # largest BST subtree recursively
    def largestBSTSubtreeHelper(self, root):
        if not root:
            return NodeValue(float('inf'), float('-inf'), 0)

        # Get values from left and right
        # subtrees of the current tree.
        left = self.largestBSTSubtreeHelper(root.left)
        right = self.largestBSTSubtreeHelper(root.right)



        # Check if the current tree is a BST based
        # on its left and right subtrees' properties
        if left.maxNode < root.val < right.minNode:


            # It is a BST, update the values for the current tree
            return NodeValue(min(root.val, left.minNode),
                             max(root.val, right.maxNode),
                             left.maxSize + right.maxSize + 1)

        # If the current tree is not a BST,
        # return values indicating invalid tree properties
        return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

    # Function to find the size
    # of the largest BST subtree
    def largestBSTSubtree(self, root):
        return self.largestBSTSubtreeHelper(root).maxSize
def insert(root, val):
    # Utility function to insert nodes into the BST
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

r =None
r = insert(r, 10)
insert(r, 5)
insert(r, 15)
insert(r, 1)
insert(r, 8)
insert(r, 7)

s = Solution()

print('the answer is', s.largestBSTSubtree(r))

