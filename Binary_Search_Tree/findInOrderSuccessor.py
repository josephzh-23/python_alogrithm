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

# Need 3 pter: parent, cur and successor
def findInOrderSuccessor(root, data):

    # Return the node that we are searching for
    cur = search(root, data)

    if not cur:
        return None

    #case 1: node has right subtree
    if cur.right:
        return findMin(cur.right)

    # case 2: no right subtree
    else:
        successor = None

        # start at the root position
        parent = root

        # Traverse down until we reach current
        while parent != cur:
            if cur.val < parent.val:
                successor = parent
                parent = parent.left

                # the 4 > 3, then we go to the right
            else:
                parent = parent.right
        return successor

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

















