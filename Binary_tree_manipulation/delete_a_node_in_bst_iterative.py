'''
Case 1:
Node to be deleted is a leaf node. Directly delete the node from the tree.

Case 2:  Node to be deleted is an internal node with two children

Copy the contents of the inorder successor of the node to be deleted and delete the inorder successor.
The inorder successor is the minimum element in the right subtree of the node.


Case 3:
Node to be deleted is an internal node with one child.
For this case, delete the node and move its child up to take its place.


Using dfs for this is extremely important here, very good for deletion problems like below

1.
'''


'''

The above is the solution here, and then we will keep going here 

'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

# Iterative approach to
# delete 'key' from the BST.
def del_iterative(root, key):
    curr = root
    prev = None

    # First check if the key is
    # actually present in the BST.
    # the variable prev points to the
    # parent of the key to be deleted
    while (curr != None and curr.key != key):
        prev = curr
        if curr.key < key:
            curr = curr.right
        else:
            curr = curr.left

    if curr == None:
        return root

    # Check if the node to be
    # deleted has atmost one child
    if curr.left == None or\
            curr.right == None:

        # newCurr will replace
        # the node to be deleted.
        newCurr = None

        # if the left child does not exist.
        if curr.left == None:
            newCurr = curr.right
        else:
            newCurr = curr.left

        # check if the node to
        # be deleted is the root.
        if prev == None:
            return newCurr

        # Check if the node to be
        # deleted is prev's left or
        # right child and then
        # replace this with newCurr
        if curr == prev.left:
            prev.left = newCurr
        else:
            prev.right = newCurr

        curr = None

    # node to be deleted
    # has two children.
    else:
        p = None
        temp = None

        # Compute the inorder
        # successor of curr.
        temp = curr.right
        while(temp.left != None):
            p = temp
            temp = temp.left

        # check if the parent of the
        # inorder successor is the root or not.
        # if it isn't, then make the left
        # child of its parent equal to the
        # inorder successor's right child.
        if p != None:
            p.left = temp.right

        else:

            # if the inorder successor was
            # the root, then make the right child
            # of the node to be deleted equal
            # to the right child of the inorder
            # successor.
            curr.right = temp.right

        curr.data = temp.key

    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    x = 15

    root = del_iterative(root, x)
    inorder(root)