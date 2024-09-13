from typing import Optional

from String.String_Array.findMode import List
from Binary_tree.BSTNode import TreeNode

''' 
Example here: 
Given preorder array 
    3           preorder : [ 3, 9 , 20, 15, 7] 
  9   20        inOrder array: [ 9, 3, 15, 20, 7] 
    15   7 

preorder array: 3 is always the root element. 
We get 3 from preorder array and then find it in inOrder array

-> everything from left of 3 will be on left
-> everything from right will be on right
'''



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # always the 1st elem in
        root = TreeNode(preorder[0])

        # find the preorder root in the inorder array
        mid = inorder.index(preorder[0])

        # For preorder: this is really from 1 to mid (not including mid + 1)
        # For inorder will be from beginning to mid, but not including mid
        root.l = self.buildTree(preorder[1: mid + 1], inorder[:mid])

        # For preorder:
        #
        # For inorder:
        #       from mid to the end
        root.r = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root