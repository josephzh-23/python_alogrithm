# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from String_Array.findMode import List
'''
    If given 
             3
          9     20 
              15   7   
    Then need to return 
    [ [3],  [9, 20] ,  [15, 7] ] and that's it as shown above
    
    O (n)
    O (n) for both TC and SC 
'''

class Solution:
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