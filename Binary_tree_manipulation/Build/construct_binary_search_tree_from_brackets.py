r

'''

Input : "1(2)(3)"
Output : 1 2 3
Explanation :
           1
          / \
         2   3


If you want to save this to a file here and then more

Important for saving a tree to a file here

1. Main thing to note:

Everything in between is everything incldued between a pair of matching
bracket is a tree here:

4 (2 (3 (1 )) (6 (5 ))

2 3 1 is a tree
                4
3 <- 2 -> 1         5 <- 6
 2 is the root here


 Steps:

 1. An opening bracket === start of a new tree, when we see a '
whenever we encounter a new opening bracket, we make a new recursion call

2. When do we stop here?
->getNumber : returns current integer number that the cur tree node has
We iterate until we no longer encounter a digit
or we reach the end of the string.

3. Next function:
st2TreeInternal: input: string and index of cur char as inputs
return : returns a pair of the TreeNode representation of the current
subtree and also the index of the next character to be processed in the string.

Why index? B/c don't want to parse the string twice here


1. First get value of root node and the startign index here
(4

2. Then, we check for an opening bracket (make sure to check for the end of string conditions always).
 If there is one, we make a recursive call and use the node returned as the left child of the current node.
(4 (2, this is checking for the open bracket

Check again for open bracket
 3.If we see new oepning brecket -> another right child
 simply make another recursive call to construct the subtree
'''
from Binary_tree.Basics.BFS_rec import Node


def str2Internal(s: str, index: int)-> (Node, int):
    if index == len(s):
        return None, index

    # Start of the tree will always contain a number representing
    # the root of the tree. So we calculate that first.
    value, index = getNumber(s, index)
    node = Node(value)

    # Next, if there is any data left, we check for the first subtree
    # which according to the problem statement will always be the left child.
    if index < len(s) and s[index] == '(':
        node.left, index = str2Internal(s, index + 1)

        # Indicates a right child
    if node.left and index < len(s) and s[index] == '(':
        node.right, index = str2Internal(s, index + 1)

    return node, index + 1 if index < len(s) and s[index] == ')' else index

'''
Like we said returning the number and the index here 
'''
def getNumber(s: str, index: int) -> (int, int):
    is_negative = False

    # A negative number
    if s[index] == '-':
        is_negative = True
        index = index + 1

    number = 0

    while index < len(s) and s[index].isdigit():
        number = number * 10 + int(s[index])
        index += 1

    return number if not is_negative else -number, index

# part of the equation here

























