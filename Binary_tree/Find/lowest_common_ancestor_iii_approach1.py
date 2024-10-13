'''

3 approaches to this problem
you have 3 ways here


Memorize the route
'''

# use a while loop to get the parent pointer

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
def lowestCommonAncestor(p, q):

    seen = set()
    while not p:
        seen.add(p)
        p = p.parent


    while q:
        if q in seen:
            print(q.value)
        q = q.parent



    return None   # this is answer solution #1 here










