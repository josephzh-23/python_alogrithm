from typing import Optional

from Binary_tree.BSTNode import TreeNode


def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
) -> Optional[TreeNode]:
    if not root:
        return None

    stack = []
    current_node = root
    last_right_node = None

    while stack or current_node:
        # Push left nodes to the stack until reaching the leftmost node.
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        # Access the top node on the stack without removing it.
        # This node is the current candidate for processing.
        current_node = stack[-1]

        # Check if the current node has an unexplored right subtree.
        # If so, shift to the right subtree unless it's the subtree we just visited.
        if current_node.right and current_node.right is not last_right_node:
            current_node = current_node.right
            continue  # Continue in the while loop to push this new subtree's leftmost nodes.

        # Remove the node from the stack, since we're about to process it.
        stack.pop()

        # If the node has no right subtree or the right subtree has already been visited,
        # then check if it is a leaf node with the target value.
        if (
                not current_node.right
                and not current_node.left
                and current_node.val == target
        ):
            # If the stack is empty after popping, it means the root was a target leaf node.
            if not stack:
                return None  # The tree becomes empty as the root itself is removed.

            # Identify the parent of the current node.
            parent = stack[-1] if stack else None

            # Disconnect the current node from its parent.
            if parent and parent.left is current_node:
                parent.left = None  # If current is a left child, set the left pointer to null.
            elif parent and parent.right is current_node:
                parent.right = None  # If current is a right child, set the right pointer to null.

        # Mark this node as visited by setting 'last_right_node' to 'current_node' before moving to the next iteration.
        last_right_node = current_node
        # Reset 'current_node' to None to ensure the next node from the stack is processed.
        current_node = None

    return root  # Return the modified tree