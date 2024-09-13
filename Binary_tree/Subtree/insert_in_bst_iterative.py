from Binary_tree.BSTNode import TreeNode


def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    node = root
    while node:



        # Remember use the code here can even use the psedo code here
        if val > node.val:
            # insert right now
            if not node.r:
                node.r = TreeNode(val)
                return root
            else:
                node = node.r
        # insert into the left subtree
        else:
            # insert right now
            if not node.l:
                node.l = TreeNode(val)
                return root
            else:
                node = node.l
    return TreeNode(val)