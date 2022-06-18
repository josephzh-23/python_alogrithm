from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.breath_first_search_rec import printLevelOrderIter


def mirror(root):
    if (root == None):
        return

    q = []
    q.append(root)
    while q:

        cur = q[0]
        q.pop(0)

        cur.left, cur.right = cur.right, cur.left

        if (cur.left):
            q.append(cur.left)
        if (cur.right):
            q.append(cur.right)

def swapChildren(r):

    temp = r.left
    r.left = r.right
    r.right = temp


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

""" Print inorder traversal of the input tree """
mirror(root)
print("Inorder traversal of the constructed tree is")
printLevelOrderIter(root)