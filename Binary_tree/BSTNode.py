# A binary search tree node here

"""
    1
   / \
  2   3
 /\   /\
4
"""

#

# this is how to implement a bstNode
class TreeNode:
    def __init__(s, val= None, left = None, right = None):
        s.l = None
        s.r = None
        s.val = val


# recursive approach
def insertRec(r, key):


    if r is None:
        return TreeNode(key)
    else:
        if r.val < key:
            r.r = insert(r.r, key)
        else:
            r.l = insert(r.l, key)
    return r

# iterative approach, need 2 pters:
# parent and cur
def insert(root, val=None):
    if not root:
        return TreeNode(val)

    #traverse thru the current value
    cur = root

    # pointer to store the parent of the current node
    parent = None

    '''
    step 1: is to traverse until either the left and 
    right is empty 
    '''
    while cur:

        #update parent to current node
        # and then compare left and right
        parent = cur

        if val < cur.val:
            cur = cur.l
        else:
            cur = cur.r

    # construct a node and assign it to the appropriate parent pointer
    if val < parent.val:
        parent.left = TreeNode(val)
    else:
        parent.right = TreeNode(val)

    return root


# Using binary search tree caller

"""
Diff between recursive search and iterative search
    - recursive version has SC: O (logN)
    
    -iterative has SC: O (1), the better

TC: worst case: O (h), h = height of the tree 
        max height = N - O (N)      N number of nodes 
        min height = log2N + 1      
"""

# this returns the target node with its chidlren nodes
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val ==key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)



# Search in the iteraitve approach
def searchIter(root, key):

    # traverse until root reaches end
    while root:
        # Traverse down until right
        if key > root.val:
            root = root. right
        elif key < root.val:
            root = root.left

        else:
            return True
    return False

'''
Given a non-empty binary
search tree, return the node
with minimum key value  
found in that tree. 

    which is also the leftmost node in that tree (smallest)
'''
def findMin(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.l is not None):
        current = current.l
    return current

"""
    delete: is quite complicated, and has 3 cases 
    1. node to be deleted is the leaf node: simply remove from the tree 
    
    2.  Node to be deleted has only one child: Copy the child to the node 
    and delete the child 

    3. Node to be deleted has two children: Find inorder successor of the node.
     Copy contents of the inorder successor to the node 
     and delete the inorder successor.
     
        Note: in order successor can be obtained by finding the min value in the 
     right child of the node 
"""

# Given a binary search tree and a key, this function
# delete the key and returns the new root

def deleteNode(root, key) -> TreeNode:
    # Base Case
    if root is None:
        return root

    # Case 1: the leaf node
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Case 2
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp


        # Case 3
        # Node with two children:
        # Get the inorder successor
        # (smallest node in the right subtree)
        temp = findMin(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root

node = TreeNode(50)
node = insert(node, 30)
# print("the value found", search(node,30).val)

