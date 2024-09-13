

'''
Check if 2 trees are the same

Can use BFS to traverse both trees
'''
from Binary_tree.BSTNode import TreeNode, insert


def checkIfTwoTreesSame(t1, t2):

    #regular bfs
    q1 = []
    q2 = []

    q1.append(t1)
    q2.append(t2)

# make sure both are not empty
    while q1 and q2:

        n1 = q1[0]
        n2 = q2[0]

        # Remember they are simply pointers with data value
        if n1.val != n2.val:
            return False

        # pop right here
        q1.pop(0), q2.pop(0)
        if n1.l and n2.l:
            q1.append(n1.l)
            q2.append(n2.l)

        # one left child is empty
        elif n1.l or n2.l:
            return False

        if n1.r and n2.r:
            q1.append(n1.r)
            q2.append(n2.r)

        # 1 right child is empty here
        elif n1.r or n2.r:
            return False

    return True

t1 = TreeNode(4)
insert(t1,5 )
insert(t1, 6)

t2 = TreeNode(4)
insert(t2,5 )
insert(t2, 6)

res  = checkIfTwoTreesSame(t1, t2)
print('they are ', res)
