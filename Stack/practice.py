from Binary_Search_Tree.BSTNode import insert, Node
from Binary_Search_Tree.breath_first_search import printLevelOrder


def flattenTree(root):

    # Base CAse
    if root is None:
        return

    # create an empty stack and push root to it
    stack = []
    stack.append(root)

    while stack:
        cur = stack.pop()

        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)

        if stack:
            cur.right = stack[-1]
        cur.left = None


node = Node(4)
insert(node,5 )
insert(node, 6)
insert(node, 7)
insert(node, 8)
flattenTree(node)
