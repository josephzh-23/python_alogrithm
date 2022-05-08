'''

'''

# Driver program to test the above functions
# Let us create the following BST
#       50
#    /     \
#   30     70
#  / \     / \
# 20 40  60   80


# Working with tree
from Binary_Search_Tree.BSTNode import search, findMin


class Node:
    def __init__(s, val = None):
        s.left = None
        s.right = None
        s.val = val

"""
For insert, need 2 pointers
 1 parent and 1 current pointer 
 
 - current for traversing; parent for pointing
"""
def insert(root, val):

    if not root:
        return Node(val)


    # compare the left to the right and see what to do there
    cur = root

    # pter to store parent of cur node
    parent = None

    while cur:

        # update parent to cur node
        parent = cur

        if val < cur.val:
            cur = cur.left
        else:
            cur = cur.right

    if val < parent.left:
        parent.left = Node(val)
    else:
        parent.right = Node(val)

    return root


def levelOrder(root):

    q = []

    # will get updated
    cur = root
    q.append(cur)

    while q:
        node = q.pop(0)

        if node.left:
            print(node.left)
            q.append(node.left)
        if node.right:
            print(node.right)
            q.append(node.right)


def findInOrderSuccessor(root, data):
    cur = search(root, data)

    if not cur:
        return None
    #case 1: node has right subtree
    if cur.right:
        return findMin(cur.right)

 # has left
    else:
        successor = None
        par = root

        while cur != par:
            successor = par

            if cur.val < par.val:
                par = par.left
            else:
                par = par.right



def insertRec(root, key):
    if root is None:
        return Node(key)

    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def printLevelOrder(s):
    # 3 4 5, add all to queue
    queue = []

    queue.append(s.root)

    while queue:
        node = queue.pop(0)

        print(queue.pop(0))

        if node.left:
            queue.append(node.left)




def inOrderTraversal(root):
    # 4, 5, 6
    cur = root
    s = []
    while s:
        n = s.pop()

        print(n.val)
        #Check left n
        if n.left:
            s.append(n.left)
        elif n.right:
            s.append(n.right)






node = Node(50)
node =insert(node, 30)
node = insert(node, 70)
node = insert(node, 20)
node = insert(node, 40)


printLevelOrder()


