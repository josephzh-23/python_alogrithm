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

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()

        if node:
            if not node.r and not node.l:
                print(minDepth)
            else:
                minDepth +=1
            if node.r:
                # print('right val', node.right.val, end=" ")
                stack.append(node.r)
            if node.l:
                stack.append(node.l)


root = TreeNode(3)
root.l = TreeNode(9)
root.r = TreeNode(20)
root.r.l = TreeNode(15)
root.r.r = TreeNode(7)
preorderTraversal(root)