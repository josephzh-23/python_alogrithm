from Binary_tree.BSTNode import TreeNode


'''
Traverse the tree T in preorder fashion. 
For every visited node in the traversal, 
see if the sub node is the same as the tree given 

use sameTree(s, t) approach

'''



# Return true if s is a subtree of t
# TC: O ( s * t) here
def isSubtree(self, t, s) -> bool:

    # remember s is the subtree, so if it's empty it will return true
    if not s: return True
    if not t: return False

    if self.sameTree(t, s):
        return True

    # IF the tree with root as current node doesn't match
    # then try left and right subtree one by one
    return (self.isSubtree(t.l, s) or
            self.isSubtree(t.r, s))


def sameTree(self, s, t):

    # then they are the same tree
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return (sameTree(s.l, t.l) and
                sameTree(s.r, t.r))
    return False




