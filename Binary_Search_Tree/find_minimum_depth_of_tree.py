'''
Find minimum depth of a tree here
leetcode here

1. `

'''
from Binary_Search_Tree.BSTNode import TreeNode


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
            if not node.right and not node.left:
                print(minDepth)
            else:
                minDepth +=1
            if node.right:
                # print('right val', node.right.val, end=" ")
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
preorderTraversal(root)