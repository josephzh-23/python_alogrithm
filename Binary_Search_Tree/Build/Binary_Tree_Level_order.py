# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from String.String_Array.findMode import List
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
# level order traversal as said pretty simple here
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