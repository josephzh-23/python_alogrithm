'''
Notice this is not the same as finding the lowest ancestor binary tree here
very different here then what's expected here
-
        20
      /  \
     8    22
    /\
   4  12
      / \
    10   14


          LCA of 6 and 7 is 3 here

      The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in

       T that has both n1
      and n2 as descendants (where we allow a node to be a descendant of itself). The LCA of n1 and n2 in T is
      the shared ancestor of n1 and n2 that is located farthest from the root [i.e., closest to n1 and n2].

      '''

# TC: O (nlogn) here only half of nodes traversed
# TC O (h) where h = the height of the tree
def lowestCommonAncestor(r, p, q):

    # both of them are on the left side
    if p.val < r.val and q.val < r.val:
        return lowestCommonAncestor(r.l, p, q)

    # both of them are on the right side
    elif p.val > r.val and q.val > r.val:
        return lowestCommonAncestor(r.r, p, q)

    #       6
    #    2    8
    else:
        return r
  

