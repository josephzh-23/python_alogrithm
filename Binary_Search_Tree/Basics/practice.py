from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.breadth_first_search_iter import printLevelOrderIter

prev = Node(0)


def invertTree(r):

    if r is None:
        return None
    
    # need to swithc between left and right

    temp = r.left
    r.left = r.right
    r.right = temp

    invertTree(r.left)
    invertTree(r.right)
    return r

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

printLevelOrderIter(root)
invertTree(root)
printLevelOrderIter(root)

def getLowestCommonAncestor(r, p, q):

    # p and q