
from collections import defaultdict
from typing import Optional, List

from Binary_tree.BSTNode import insert
from palindrome_linkedlist import ListNode

'''
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

The idea here is we use a hashmap to store data and then 
[1, 2, null, null, 3, null, null]-> Node (value)

And the above will make perfect sense here 

For example the tree here that we have 

 2 <- 1 -> 3

 in the above will become 

The subtree strign that's stored will become 
 1, 2, N, N, 3 ,N, N 
       L  R     L  R 

the above is how it works mostly here 

The time complexity here would 

'''

class TreeNode:
    def __init__(s, val= None, left = None, right = None):
        s.left = left
        s.right = right
        s.val = val



def findDuplicateSubtrees(root: Optional[ListNode]) -> List[Optional[ListNode]]:
    subtrees = defaultdict(list)

    def dfs(node):

        if not node:
            return "null"

        s = ",".join([str(node.val), dfs(node.l), dfs(node.r)])
        print("s is " , s)
        # we need to test out this part later on here

        # this means a duplicate has come here at this point there is already a duplicate here
        if len(subtrees[s]) == 1:
            res.append(node)
        subtrees[s].append(node)
        return s

    res = []
    dfs(root)
    return res

# feel free to test this out in a real coding environment here

# the below will definitely make sense on so many levels
s = TreeNode(4)
s.left = TreeNode(2)
s.left.left = TreeNode(4)
s.right = TreeNode(3)
s.right.left = TreeNode(2)
s.right.right = TreeNode(4)

answer = findDuplicateSubtrees(s)
print('duplicate is', answer)






    # and that's why it's so important to use the code given to do