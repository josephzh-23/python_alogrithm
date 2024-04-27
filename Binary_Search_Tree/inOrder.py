#left, root and then right
from Binary_Search_Tree.BSTNode import TreeNode



def inOrderRec(root):

    # the base condition if root doesn't exist it will return
    # must have a base condition
    if root:

        # First recur on left child
        inOrderRec(root.left)
        print(root.val)
        inOrderRec(root.right)

'''
In order means: left, root and right (from smallest to biggest) the 
same as sorting 
'''
def inOrderIter(root):

    stack = []

    cur = root

    #
    # we need to get down to the left most node first
    while cur or stack:
        while cur:
            stack.append(cur)
            print("the left is", cur.val)
            cur = cur.left

        # then traverse the right
        cur = stack.pop()
        print(cur.val)
        cur = cur.right


# Driver program to test above function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# PreorderIter(root)

# inOrderIter(root)