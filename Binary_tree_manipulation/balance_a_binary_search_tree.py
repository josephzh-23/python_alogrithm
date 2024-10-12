from Binary_tree.BSTNode import TreeNode


def balanceBST(root: TreeNode) -> TreeNode:
    # Create a list to store the inorder traversal of the BST
    inorder = []
    inorder_traversal(root, inorder)

    # Construct and return the balanced BST
    return create_balanced_bst(inorder, 0, len(inorder) - 1)


def inorder_traversal( root: TreeNode, inorder: list):
    # Perform an inorder traversal to store the elements in sorted order
    if not root:
        return
    inorder_traversal(root.l, inorder)
    inorder.append(root.val)
    inorder_traversal(root.r, inorder)


def create_balanced_bst(
        self, inorder: list, start: int, end: int
) -> TreeNode:
    # Base case: if the start index is greater than the end index, return None
    if start > end:
        return None

    # Find the middle element of the current range
    mid = start + (end - start) // 2

    # Recursively construct the left and right subtrees
    left_subtree = self.create_balanced_bst(inorder, start, mid - 1)
    right_subtree = self.create_balanced_bst(inorder, mid + 1, end)

    # Create a new node with the middle element and attach the subtrees
    node = TreeNode(inorder[mid], left_subtree, right_subtree)
    return node
