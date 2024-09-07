# Python3 program to demonstrate insert operation
# in binary search tree with parent pointer

# A utility function to create a new BST Node
class newNode:
    def __init__(self, item):
        self.key = item
        self.left = self.right = None
        self.parent = None


# A utility function to do inorder
# traversal of BST
def inorder(root):
    if root != None:
        inorder(root.l)
        print("Node :", root.key, ", ", end="")
        if root.parent == None:
            print("Parent : NULL")
        else:
            print("Parent : ", root.parent.key)
        inorder(root.r)


# A utility function to insert a new
# Node with given key in BST

def insert(node, key):
    # If the tree is empty, return a new Node
    if node == None:
        return newNode(key)
        '''
        3   
      5   4
            
        '''
        # Otherwise, recur down the tree
    if key < node.key:
        lchild = insert(node.l, key)
        node.l = lchild

        # Set parent of root of left subtree
        lchild.parent = node



    elif key > node.key:
        rchild = insert(node.r, key)
        node.r = rchild

        # Set parent of root of right subtree
        rchild.parent = node

    # return the (unchanged) Node pointer
    return node


# Driver Code
if __name__ == '__main__':
    # Let us create following BST
    #         50
    #     /     \
    #     30     70
    #     / \ / \
    # 20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # print iNorder traversal of the BST
    inorder(root)

# This code is contributed by PranchalK