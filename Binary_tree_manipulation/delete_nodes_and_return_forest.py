'''
Delete node and return a forest here


A dfs approach should be faster here given the situation so that's why we went with it here

And this makes more sense given the situation in the longer time frame here



'''
from typing import Optional

from Binary_tree.BSTNode import TreeNode


def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    # Set to store the values that need to be deleted
    to_delete_set = set(to_delete)
    # List to accumulate the resulting forest nodes
    forest = []

    # Helper function performing a DFS on the tree
    def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return None
        # Recursively call on left and right children
        node.left = dfs(node.left)
        node.right = dfs(node.right)



        '''
        Here comes the part for deleting a node here, node in the s then has to be deleted 
        1.  As it is the node to be deleted here 
        
        2. Return none as this is the node to be deleted and then 
        
        '''
        # If current node's value is in the 'to_delete' set
        if node.val in to_delete_set:
            # Append children to forest if they are not None
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)
            # Returning None, as this node gets deleted
            return None
        # If the node isn't getting deleted, return it
        return node

    # Starting the DFS from the root; if the root isn't deleted, append to forest
    if dfs(root):
        forest.append(root)

    return forest
