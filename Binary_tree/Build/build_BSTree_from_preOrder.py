

# this is provided by Coding Simplified

# preOrder is left right pare
'''
  [10   4   2  8   5   9   15   12   20]
start                      i         end
logic:
    find i, the val > arr[start]
    root.left = arr[start: i]       from start to i
    root.right = arr[i : end]       from i to end

2nd iteration
    [4   2   8   5  9]
start        i              and then we repeat for this forever

'''
from Binary_tree.BSTNode import TreeNode
from Binary_tree.Basics.preOrder import preOrderRec

r = None
def buildBSTreeFromPreorder(arr, start, end):

    global r
    start = 0
    end = len(arr)-1
    for i in range(len(arr)):
        if arr[i] >arr[start]:
            r = TreeNode(arr[i])
            r.l = buildBSTreeFromPreorder(arr[start:i], start + 1, i)
            r.r = buildBSTreeFromPreorder(arr[i: end], i + 1, end)

    return r
#driver for this
preOrder = [10, 4, 2, 8, 5, 9, 15, 12, 20]
root = buildBSTreeFromPreorder(preOrder,0, len(preOrder ) - 1)

# we did it it was a success
preOrderRec(root)