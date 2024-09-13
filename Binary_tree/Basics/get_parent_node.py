

# to get parent node of a node that's passed in
from Binary_tree.BSTNode import TreeNode, insert


# need a par to hold parent node reference
# TC: O(n)
def getParentNode(root, value):
    cur= root

    parent = None
    while cur:
        if cur.val< value:
            parent = cur
            cur = cur.r

        elif cur.val > value:
            parent = cur
            cur = cur.l

        # found
        elif cur.val == value:
            return parent


node = TreeNode(50)
node = insert(node, 30)
node = insert(node, 40)
node = insert(node, 60)
node = insert(node, 70)

# inOrder(node)
print(getParentNode(node, 40).val)


