'''
I
'''
from typing import Optional, List

from Binary_tree.BSTNode import TreeNode


def pathSum( root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if not root:
        return []

    # dfs function to find path from root to leaf
    def dfs(root, path):
        # to check if node is leaf
        if not root.l and not root.r:

            # if leaf then check if path sum matches target sum
            if targetSum == sum(path + [root.val]):

                # then the result is added here
                # if yes then add path to result array
                return res.append(path + [root.val])

        # recursively cal for left and right nodes till leaf node
        if root.l:
            dfs(root.l, path + [root.val])
        if root.r:
            dfs(root.r, path + [root.val])

    # create a result array
    res = []
    # call the function for root
    dfs(root, [])
    return res

# Driver program to test above function, on the left side here
root = TreeNode(5)
root.l = TreeNode(4)
root.l.l = TreeNode(11)
root.l.l.l = TreeNode(11)
root.l.l.r = TreeNode(2)

root.r = TreeNode(8)
root.r.l = TreeNode(13)
root.r.r = TreeNode(4)
root.r.r.l = TreeNode(5)
root.r.r.r = TreeNode(1)
pathSum(root, 22)

'''
There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22         (and then here) with the code here 
5 + 8 + 4 + 5 = 22

'''