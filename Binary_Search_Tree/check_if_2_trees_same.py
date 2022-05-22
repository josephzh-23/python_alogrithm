

'''
Check if 2 trees are the same

Can use BFS to traverse both trees
'''
from Binary_Search_Tree.BSTNode import Node, insert


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
        if n1.left and n2.left:
            q1.append(n1.left)
            q2.append(n2.left)

        # one left child is empty
        elif n1.left or n2.left:
            return False
        if n1.right and n2.right:
            q1.append(n1.right)
            q2.append(n2.right)

        elif n1.right or n2.right:
            return False

    return True

t1 = Node(4)
insert(t1,5 )
insert(t1, 6)

t2 = Node(4)
insert(t2,5 )
insert(t2, 6)

res  = checkIfTwoTreesSame(t1, t2)
print('they are ', res)
