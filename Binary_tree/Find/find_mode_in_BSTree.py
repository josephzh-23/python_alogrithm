

# Use a inorder traversal
from Binary_tree.BSTNode import TreeNode, insert

prev = None
count = 0
max = 0

def inOrder(node, list):
    global prev, count, max

    if not node:
        return

    inOrder(node.l, list)
    if prev:
        if node.val == prev.val:
            count+=1
        else:
            count = 1

    # here have to clear the list because then a
    # new mode (single) has been found that exceeeds the previous max
    if count> max:
        list.clear()
        list.append(node)
        max = count

    # case 2: > 1 modes
    elif count==max:
        list.append(node)

    # 1st time, come here prev == null so assign above 
    prev = node
    print('the value of prev is ',prev.val)
    inOrder(node.r, list)

def findMode(root):
    list = []
    inOrder(root, list)

    res = []
    for mode in list:
        res.append(mode)

    return res
node = TreeNode(5)
insert(node,3 )
insert(node,4)
insert(node,5 )
insert(node,6 )
insert(node,7 )
insert(node,7 )

# printLevelOrder(node)
value = findMode(node)
# print(' the mode found is', value[0].val)
# print(' the mode found is', value[1].val)

# inOrderIter(node)
#

# practice, build tree from sorted array