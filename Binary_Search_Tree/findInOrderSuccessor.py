from Binary_Search_Tree.BSTNode import Node, search, findMin, insert

'''
This is a linkedlist problem, tough to solve 
 TC: O (h)      there r 2 cases here 
 
 case 1 : node has right subtree
    - travserse deep to leftmost node in right subtree
    or find min in right subtree 
    
 case 2 : no right subtree 
    - go to nearest ancestor for which given node would
    be in left subtree 
'''

def findInOrderSuccessor(root, data):

    # O(h) operation
    cur = search(root, data)

    if not cur:
        return None

    #case 1: node has right subtree
    if cur.right:
        return findMin(cur.right)

    # case 2: no right subtree
    else:
        successor = None
        parent = root

        # We will walk the tree until we have
        # almost reached the current node
        while parent != cur:
            if cur.val < parent.val:
                successor = parent
                parent = parent.left
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

















