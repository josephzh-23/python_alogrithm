from Binary_tree.BSTNode import TreeNode

'''
The application of in order is very important 

Wanna convert this into a doubly linkedlist here 

1. Recursively perform an in-order traversal (left node, current node, right node) of the BST.

2. As we visit each node during the traversal, we connect it with the previously visited node (prev) to simulate the linked list's structure:

3. Make prev.right point to the current node (root), and make the current node's left point to prev. This process connects the nodes in a doubly-linked fashion.
4. For the first node, which does not have a prev, we set it as the head of our linked list.
After we have visited all the nodes, we connect the last visited node with the head to make the list circular.

1. It can be used 

'''

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
same as Sort 
'''
def inOrderIter(root):

    stack = []

    cur = root

    #
    # we need to get down to the left most node first
    while cur or stack:
        while cur:
            stack.append(cur)
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