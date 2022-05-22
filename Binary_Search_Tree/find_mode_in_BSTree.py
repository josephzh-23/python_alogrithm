

# Note there could be > 1 modes, and also as we are traversing
from Binary_Search_Tree.BSTNode import Node, insert
from Binary_Search_Tree.breath_first_search import printLevelOrder
from Binary_Search_Tree.depth_first_search import inOrderIter

prev = None
count = 0
max = 0
def inOrder(node, list):
    global prev, count, max

    if not node:
        return

    inOrder(node.left, list)
    if prev:
        if node.val == prev.val:
            count+=1
        else:
            count = 1

    # here have to clear the list because then a
    # new mode (single) has been found
    if count> max:
        list.clear()
        list.append(node)
        max = count

    # case 2: > 1 modes
    elif count==max:
        list.append(node)

    # 1st time, come here prev == null so assign above 
    prev = node
    inOrder(node.right, list)

def findMode(root):
    '''
       - Do an in order traversal
           match cur node with prev node
           1. if it matches, then increase the count
           2. if count == max,  then add node to a list
           3. if count > max, the clear our list,
               then add the new count node to the list
      '''

    # note that after the in order traverse function the
    # list will contain the modes based on the step above
    list = []
    inOrder(root, list)

    res = []
    for mode in list:
        res.append(mode)

    return res
node = Node(5)
insert(node,3 )
insert(node,4)
insert(node,5 )
insert(node,6 )
insert(node,7 )
insert(node,7 )

printLevelOrder(node)
value = findMode(node)
print(' the mode found is', value[0].val)
print(' the mode found is', value[1].val)




