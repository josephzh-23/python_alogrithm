'''

Check every level of tree
keep track fo the last node in the tree and make sure that it does not ahave a right
and then here you have the code

'''
from typing import List

from Binary_tree.BSTNode import TreeNode


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
            if node.l:
                q.append(node.l)
            if node.r:
                q.append(node.r)
        res.append(nodesPerLevel)
    return res

'''
Want to check for the complete tree here 
'''
root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)
