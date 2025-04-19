'''

The provided solution uses a recursive depth-first search (DFS) strategy for traversing the binary tree,
 which we implement in the dfs helper function. Here's a step-by-step approach to how the algorithm works:

The dfs function is called recursively for each node starting with the root. This function returns two things:


1) The potential LCA node at the current subtree.
The depth of the deepest leaf in the current subtree.
On each call of the dfs function:

We check if the current node is None (base case):
If it is, we return None and a depth of 0.

Otherwise, we recursively call dfs on the left child and right child.
Each recursive call will provide us with:

The potential LCA nodes l and r from the left and right subtrees, respectively.

The depths d1 and d2 representing the maximum depths in those subtrees.
We then compare the depths of the deepest leaves in the left and right subtrees:

If d1 > d2,
    the left subtree is deeper, so we return l (the left child's LCA) and d1 + 1 (the new depth).

If d1 < d2,
    the right subtree is deeper, so we return r (the right child's LCA) and d2 + 1.


If d1 == d2, both left and right subtrees have leaves at the same depth,
hence, the current root node is their LCA, and we return root and either d1 + 1 or d2 + 1 (as they are equal).
At the top level of the recursion, we call dfs(root) and are interested only in the first item of the tuple, which represents the lowest common ancestor of the deepest leaves.


'''
from typing import Optional

from Binary_tree.BSTNode import TreeNode


# Definition for a binary tree node.



def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Helper function to perform a depth-first search on the tree.
    def dfs(node):

        # Base case: if the current node is None, it corresponds to a depth of 0.
        if node is None:
            return None, 0

        # Recursively find the lowest common ancestor and depth of the left subtree.
        left_lca, left_depth = dfs(node.l)

        # Recursively find the lowest common ancestor and depth of the right subtree.
        right_lca, right_depth = dfs(node.r)

        # If the left subtree is deeper, return the left LCA and its depth increased by one.
        if left_depth > right_depth:
            return left_lca, left_depth + 1

        # If the right subtree is deeper, return the right LCA and its depth increased by one.
        if left_depth < right_depth:
            return right_lca, right_depth + 1
        print('left and right depth are', left_depth)
        # If both subtrees have the same depth, then this node is the lowest common ancestor.
        # Return the current node and the depth of the subtree.
        return node, left_depth + 1

    # Call the DFS helper function and return the lowest common ancestor. The second value of the tuple is ignored.
    return dfs(root)[0]


root = TreeNode(3)
root.l = TreeNode(5)
root.r = TreeNode(1)

root.l.l = TreeNode(6)
root.l.r = TreeNode(2)

root.l.r.l = TreeNode(7)
root.l.r.r = TreeNode(4)

root.r.r = TreeNode(0)
root.r.l = TreeNode(8)

print(lcaDeepestLeaves(root).val)