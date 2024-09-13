'''
The lowest common ancestor of both trees here
'''
from palindrome_linkedlist import ListNode

'''
This is the question where we fell the last time basically 
and the idea is simple 

1. Find depth of each pointer 
2. Move the deeper pointer up until it is at the same level as the other pointer
3. Move each pter level by level until they meet here 

Time Complexity: O(h)
Space Complexity: O(1)

'''


def getDepth(p):
    # helper function to find the depth of the pointer in the tree
    depth = 0
    while p:
        p = p.parent
        depth += 1
    return depth

# the above to find the solution as indiciated above and then below we have the code
def lowestCommonAncestor(p, q):
    # find depth of each pter
    pDepth = getDepth(p)
    qDepth = getDepth(q)
    # this makes sure they are travelling up together at the same time here
    for _ in range(pDepth - qDepth):
        p = p.parent
    for _ in range(qDepth - pDepth):
        q = q.parent

    while p != q:
        p = p.parent
        q = q.parent
    return p

# and that's basically the gist of this problem here

# and then the first part of this equation is basically when you add this
# here in the code and then it becomes sth else
