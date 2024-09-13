'''

Basically in this specific example, we need to see that the smallest kth element
is basically k -1 since it's already a binary search tree up here
'''
from Binary_tree.BSTNode import TreeNode


def findKthSmallestElement(root, k):
    # the other clean way to do this here
    # is through the above way where we have

    array = []
    def inOrder(node):
        if not node:
            return

        inOrder(node.l)
        array.append(node.val)
        inOrder(node.r)
    inOrder(root)

    return array[k -1 ] #as said previously here

    # and those are really good indicators here

s = TreeNode(3)
s.l = TreeNode(1)
s.r = TreeNode(4)
s.l.r = TreeNode(2)
print(findKthSmallestElement(s, 1))






