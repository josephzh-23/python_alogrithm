from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.BFS_rec import printLevelOrderIter

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







root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)
invertTreeRec(root)

printLevelOrderIter(root)