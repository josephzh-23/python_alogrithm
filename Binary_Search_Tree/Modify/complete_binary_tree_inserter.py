'''



'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node's value
        self.left = left  # Node's left child
        self.right = right  # Node's right child

class CBTInserter:
    def __init__(self, root: TreeNode):
        # Initialize a list to store the nodes of the tree in level order
        #
        self.tree_nodes = []
        # Start with a queue containing the root.
        queue = deque([root])


        # Perform breadth-first search to populate tree_nodes
        while queue:
            node = queue.popleft()
            self.tree_nodes.append(node)
            # Add left child if it exists
            if node.left:
                queue.append(node.left)
            # Add right child if it exists
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:


        # Calculate the parent index for the new node
        parent_index = (len(self.tree_nodes) - 1) // 2

        # Create a new node with the given value
        new_node = TreeNode(val)
        self.tree_nodes.append(new_node)


        # Determine the parent node
        parent_node = self.tree_nodes[parent_index]
        # Decide where to add the new node in the parent
        if not parent_node.left:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        # Return the value of the parent node
        return parent_node.val

    def get_root(self) -> TreeNode:
        # Return the root node of the tree
        return self.tree_nodes[0]