from Binary_Search_Tree.BSTNode import Node




# TC: O ( s * t) here
def isSubtree(self, s: Node, t: Node) -> bool:

    # remember t is the subtree, so if it's empty it will return true
    if not t: return True
    if not s: return False

    if self.sameTree(s, t):
        return True
    return (self.isSubtree(s.left, t) or
            self.isSubtree(s.right, t))


def sameTree(self, s, t):

    # then they are the same tree
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return (sameTree(s.left, t.left) and
                sameTree(s.right, t.right))
    return False