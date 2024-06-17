'''
A binary search here and then where this is the bst here
- tree in which all the nodes follow the below-mentioned properties

- 1. The left subtree values < value of their parent (root) node's value.
2. Right subtree values > value of their parent (root) node's value here

3. A subtree must inclde

# and then here we have the correct value here then that's good here

We start with a DFS on the root node (10). We use the dfs function,
which will return the minimum value, maximum value, and node count of the valid BST subtree.
and that's shown as above as discussed here so this is important here

- Call dfs on left and the right child
Node 1 returns (1, 1, 1) b/c it has no children and is a valid BST on its own
Node 8 returns (8, 8, 1) for the same reason


'''
from cmath import inf
from typing import Optional

from Binary_Search_Tree.BSTNode import TreeNode


def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
    # Helper function to perform a DFS on the binary tree.
    def dfs(node):
        # Base case: If the node is None, return a tuple containing infinity,
        # negative infinity, and 0, indicating an empty subtree.
        if node is None:
            return inf, -inf, 0


        # Recursively obtain minimum value, maximum value, and size of the
        # left and right subtrees.
        left_min, left_max, left_size = dfs(node.left)
        right_min, right_max, right_size = dfs(node.right)

        # Use a nonlocal variable to keep track of the largest BST size found so far.
        nonlocal largest_bst_size

        # Check if the current tree rooted at 'node' is a BST by comparing its value
        # with the maximum of the left subtree and the minimum of the right subtree.
        if left_max < node.val < right_min:

            # Update the largest BST size if the current subtree is larger.
            largest_bst_size = max(largest_bst_size, left_size + right_size + 1)
            # Return a tuple with the new minimum, maximum, and size of the current subtree.
            return min(left_min, node.val), max(right_max, node.val), left_size + right_size + 1
        else:
            # If the current subtree is not a BST, return values that convey a violation
            # in the BST property to parent nodes.
            return -inf, inf, 0

    # Initialize the largest BST size to 0.
    largest_bst_size = 0
    # Perform a DFS on the binary tree starting from the root.
    dfs(root)
    # After the DFS is completed, return the largest BST size found.
    return largest_bst_size
