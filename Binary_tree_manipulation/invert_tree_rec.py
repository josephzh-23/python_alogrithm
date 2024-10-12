from Binary_tree.BSTNode import TreeNode
from Binary_tree.Basics.BFS_rec import printLevelOrderIter

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
    invertTreeRec(r.l)
    invertTreeRec(r.r)
    return r


def swapChildren(r):
    tmp = r.l
    r.l = r.r
    r.r = tmp







root = TreeNode(4)
root.l = TreeNode(2)
root.r = TreeNode(7)
root.l.l = TreeNode(1)
root.l.r = TreeNode(3)
root.r.l = TreeNode(6)
root.r.r = TreeNode(9)
invertTreeRec(root)

printLevelOrderIter(root)