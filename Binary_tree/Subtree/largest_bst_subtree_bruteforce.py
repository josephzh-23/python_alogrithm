'''

TC: O(n^2) is the # of nodes in the tree,

O(n) to traverse thru each node in the tree
For validation takes O(n) for each tree here

O(1) is the space requirement here no extra here as you can see

The solution is here and then we will use this accordingly here
and then build a profile here


1. Check if the subtree is a valid bst tree here
2.  Whenever a valid BST is confirmed, the size of that particular subtree is calculated and compared against the
 current maximum subtree size stored. Ultimately, the global maximum BST subtree size is returned.

3.

'''
# the tree here and then


def largestBSTSubtree(root):
    # Function to find the size
    # of the largest BST subtree
    if root is None:
        return 0
    if isValidBST(root, float('-inf'), float('inf')):
        return countNodes(root)
    else:
        left = largestBSTSubtree(root.left)
        right = largestBSTSubtree(root.right)
        return max(left, right)


def countNodes(r):

    if not r:
        return 0
    return 1 + countNodes(r.left) + countNodes(r.right)

def isValidBST(self, root, minVal, maxVal):
    # Function to check if a given root is a valid BST
    if root is None:
        return True
    if not (minVal < root.val < maxVal):
        return False
    return self.isValidBST(root.left, minVal, root.val) and self.isValidBST(root.right, root.val, maxVal)

