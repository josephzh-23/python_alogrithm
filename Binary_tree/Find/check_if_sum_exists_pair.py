

"""
Check the above here and then you can see that
    8
  6   15
2   7

If sum = 21, at each iter
1. Have the set store the each node, and use    val = sum- node.data
to check if this value exists in the set or not

"""
# Check if sum exists

# There are 2 solutions to this
from Binary_tree.BSTNode import TreeNode, insert
from Binary_tree.dfS import inOrderRec

"""
1.  the first one using set here

2. Second one using a list also a good solution
"""




# Using approach 2, this is similar to find Mode in a tree example
# that we did the other day as discussed, as dicussed already

"""
Check the following out 

Answer taken from coding Simplified 
"""
def checkIfPairExists(node, sum):
    list = []

    # we will use the inorder traversal to fill this list
    # with all the values as said (left, center, right)
    inOrder(node, list)
    return checkIfPairExistsUtil(sum, list)


def inOrder(node, list):
    if not node:
        return

    inOrder(node.l, list)
    list.append(node.val)
    inOrder(node.r, list)


# 2, 4 , 5, 8, 10   in order is usually like that before
# we have start and end pter that will then increment + decerment
# to compensate for this
def checkIfPairExistsUtil(sum, list):
    start = 0
    end = len(list)-1

    while(start <end):
        curSum = list[start] + list[end]

        if curSum == sum:
            return True

        #increase the start pter
        elif curSum < sum:
            start+=1
        else:
            end-=1

        # if not found
    return False

node = TreeNode(4)
insert(node,5 )
insert(node, 6)
insert(node, 7)
insert(node, 8)

inOrderRec(node)

val = checkIfPairExists(node, 3)
print(val)







