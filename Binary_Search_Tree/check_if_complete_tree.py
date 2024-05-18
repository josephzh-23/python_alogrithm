'''

Check every level of tree
keep track fo the last node in the tree and make sure that it does not ahave a right
and then here you have the code

'''
from typing import List

from Binary_Search_Tree.BSTNode import TreeNode


# this is the level order traversal here
def levelOrder(self, root) -> List[List[int]]:
    res = []
    q = []
    if root:
        q.append(root)

    while q:
        nodesPerLevel = []

        for i in range(len(q)):
            node = q.popleft()
            nodesPerLevel.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(nodesPerLevel)
    return res

'''
Want to check for the complete tree here 
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
