from Binary_Search_Tree.BSTNode import TreeNode
from Binary_Search_Tree.Basics.BFS_rec import printLevelOrderIter

# This is using DFS, under here this is using preOrder here

'''
TC: O(n) 
SC: O(h)   : extra space for the call stack

'''
# do not forget to return the root here
def invertTreeRec(r):

    #recursively call this to practice

    if not r:
        return None

    swapChildren(r)
    invertTreeRec(r.left)
    invertTreeRec(r.right)
    return r


def swapChildren(r):
    tmp = r.left
    r.left = r.right
    r.right = tmp







root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
invertTreeRec(root)

printLevelOrderIter(root)