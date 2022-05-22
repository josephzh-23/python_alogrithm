

"""
Given   {10, 5, 1, 7, 40, 50}
     10
   /   \
   5     40
 /  \      \
1    7      50

"""


"""
1. Create an empty stack.
2. Make the first value as root. Push it to the stack.
3. Keep on popping while the stack is not empty 
 if next value >  stack’s top value. Make this value as the right child of the last popped node.
  stack.push(newNode)
  
4. If the next value < stack’s top value, make this value 
as the left child of the stack’s top node. 
    stack.push(newNode)
5. Repeat steps 2 and 3 until there are items remaining in pre[]. 

"""


# Python3 program to construct BST
# from given preorder traversal

# A binary tree node
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    # The main function that constructs BST from pre[]
    def constructTree(self, preOrderArray, size):

        # The first element of pre[] is always root
        root = Node(preOrderArray[0])

        s = []

        s.append(root)

        i = 1

        # Iterate through rest of the size-1
        while (i < size):
            temp = None

            # Keep on popping while the next value
            # is greater than stack's top value.
            while (len(s) > 0 and preOrderArray[i] > s[-1].data):
                temp = s.pop()

                print(" the popped value is ", temp.data)

            # Make this greater value as the right child
            # and append it to the stack
            if temp:
                temp.right = Node(preOrderArray[i])
                s.append(temp.right)

            # If the next value is less than the stack's top
            # value, make this value as the left child of the
            # stack's top node. append the new node to stack
            else:
                temp = s[-1]
                temp.left = Node(preOrderArray[i])
                s.append(temp.left)
            i = i + 1

        return root

    # A utility function to print
    # inorder traversal of a Binary Tree
    def printInorder(self, node):
        if (node == None):
            return

        self.printInorder(node.left)
        print(node.data, end=" ")
        self.printInorder(node.right)


    # root, left and right
    def preOrderRec(s, root):
        if root:
            print(root.data),

            s.preOrderRec(root.left)
            s.preOrderRec(root.right)


# Driver code
tree = BinaryTree()
pre = [10, 5, 1, 7, 40, 50]
size = len(pre)
root = tree.constructTree(pre, size)
print("Inorder traversal of the constructed tree is ")

# tree.printInorder(root)
tree.preOrderRec(root)

# This code is contributed by Arnab Kundu