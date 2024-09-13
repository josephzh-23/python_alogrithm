


'''

https://www.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1

What does it mean when people say isophormic tree?

It means the tree can be flippped to get the other tree here

    1               1
   / \             / \
  2   3           3   2
 /               /
4               4


This is the same as the problem from another leetcode problem here
https://leetcode.com/problems/flip-equivalent-binary-trees/editorial/

One of the following two is true for children of n1 and n2
……a) Left child of n1 is isomorphic to left child of n2 and
     right child of n1 is isomorphic to right child of n2.

……b) Left child of n1 is isomorphic to right child of n2 and
     right child of n1 is isomorphic to left child of n2.
'''
from Binary_tree.BSTNode import TreeNode


# Check if the binary tree is isomorphic or not
def isIsomorphic(n1, n2):
    # Both roots are None, trees isomorphic by definition
    if n1 is None and n2 is None:
        return True

    # Exactly one of the n1 and n2 is None, trees are not
    # isomorphic
    if n1 is None or n2 is None:
        return False

    if n1.data != n2.data:
        return False


    ''' The above is what makes sense in most cases here '''
    # There are two possible cases for n1 and n2 to be isomorphic
    # Case 1: The subtrees rooted at these nodes have NOT
    # been "Flipped".
    # Both of these subtrees have to be isomorphic, hence the &&
    # Case 2: The subtrees rooted at these nodes have
    # been "Flipped"
    return ((isIsomorphic(n1.left, n2.left) and
             isIsomorphic(n1.right, n2.right)) or
            (isIsomorphic(n1.left, n2.right) and
             isIsomorphic(n1.right, n2.left))
            )


