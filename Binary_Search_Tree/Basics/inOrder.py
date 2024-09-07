from Binary_Search_Tree.BSTNode import TreeNode


#left, root and then right

def inOrderRec(root):

    # the base condition if root doesn't exist it will return
    # must have a base condition
    if root:

        # First recur on left child
        inOrderRec(root.l)
        print(root.val)
        inOrderRec(root.r)

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
            cur = cur.l

        # then traverse the right
        cur = stack.pop()

        #if ther eis a res, then do res.append(cur.value)
        print(cur.val)
        cur = cur.r


# Driver program to test above function
root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)
# PreorderIter(root)

inOrderIter(root)