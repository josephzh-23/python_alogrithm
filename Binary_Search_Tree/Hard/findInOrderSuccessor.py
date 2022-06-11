from Binary_Search_Tree.BSTNode import Node, search, findMin, insert

'''
What's in order successor again?

        20 
     8      22
   4   12
    10    14

In this case in-order-successor of 8 is 10, 
in-order-successor of 10 is 12. 

This is a linkedlist problem, tough to solve 
 TC: O (h)      there r 2 cases here 
 
 case 1 : node has right subtree
    - travserse deep to leftmost node in right subtree
    or find min in right subtree 
    
 case 2 : no right subtree 
    - traverse down until we reach cur
    - check if we should go left or go right 
'''


def inOrderSuccessor(root, n):

    # Case 1
    if n.right is not None:
        return findMin(n.right)

    # Case 2
    succ = Node(None)

    while (root):

        #  3  <  4      then keep going to the right
        if (root.data < n.data):
            root = root.right

        #  5 > 3 , then we keep going left until we find
        # 3     start naming the successor up here
        elif (root.data > n.data):
            succ = root
            root = root.left


        else:
            break
    return succ


root = None
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);
root = insert(root, 14);

temp = 10
succ = findInOrderSuccessor(root, temp)
if succ is not None:
    print("\nInorder Successor of % d is % d " % (temp, succ.val))
else:
    print("\nInorder Successor doesn't exist")

















