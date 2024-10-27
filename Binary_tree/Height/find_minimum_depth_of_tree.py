'''
Find minimum depth of a tree here
leetcode here

1. `

'''
from Binary_tree.BSTNode import TreeNode


def preorderTraversal(root):
    # Base CAse

    minDepth = 0
    if root is None:
        return

    q = [root]

    while q:
        node = q.pop()

        if node:
            if not node.r and not node.l:
                print(minDepth)
            else:
                minDepth += 1
            if node.r:
                # print('right val', node.right.val, end=" ")
                q.append(node.r)
            if node.l:
                q.append(node.l)


root = TreeNode(3)
root.l = TreeNode(9)
root.r = TreeNode(20)
root.r.l = TreeNode(15)
root.r.r = TreeNode(7)
preorderTraversal(root)
