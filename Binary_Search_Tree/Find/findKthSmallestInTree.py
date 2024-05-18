'''

Basically in this specific example, we need to see that the smallest kth element
is basically k -1 since it's already a binary search tree up here
'''
from Binary_Search_Tree.BSTNode import TreeNode


def findKthSmallestElement(root, k):
    # the other clean way to do this here
    # is through the above way where we have

    array = []
    def inOrder(node):
        if not node:
            return

        inOrder(node.left)
        array.append(node.val)
        inOrder(node.right)
    inOrder(root)

    return array[k -1 ] #as said previously here

    # and those are really good indicators here

s = TreeNode(3)
s.left = TreeNode(1)
s.right = TreeNode(4)
s.left.right = TreeNode(2)
print(findKthSmallestElement(s, 1))






