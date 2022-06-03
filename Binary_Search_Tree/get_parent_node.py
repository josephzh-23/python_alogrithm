

# to get parent node of a node that's passed in
from Binary_Search_Tree.BSTNode import Node, insert
from Binary_Search_Tree.Hard.find_mode_in_BSTree import inOrder


def getParentNode(root, value):
    key = value
    cur= root

    parent = None
    while cur:
        if cur.val< key:
            parent = cur
            cur = cur.right

        elif cur.val > key:
            parent = cur
            cur = cur.left

        # found
        elif cur.val == key:
            return parent


node = Node(50)
node = insert(node, 30)
node = insert(node, 40)
node = insert(node, 60)
node = insert(node, 70)

inOrder(node)
print(getParentNode(node, 40).val)


