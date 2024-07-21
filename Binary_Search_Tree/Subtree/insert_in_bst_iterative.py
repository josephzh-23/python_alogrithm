from Binary_Search_Tree.BSTNode import TreeNode


def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    node = root
    while node:



        # Remember use the code here can even use the psedo code here
        if val > node.val:
            # insert right now
            if not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right
        # insert into the left subtree
        else:
            # insert right now
            if not node.left:
                node.left = TreeNode(val)
                return root
            else:
                node = node.left
    return TreeNode(val)