

# this is provided by Coding Simplified

'''
  [10   4   2  8   5   9   15   12   20]
start                      i         end
logic:
    find i, the val > arr[start]
    root.left = arr[start: i]       from start to i
    root.right = arr[i : end]       from i to end

2nd iteration
    [4   2   8   5  9]
    start    i          and then we repeat for this forever

'''
from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.breath_first_search import printLevelOrder
from Binary_Search_Tree.depth_first_search import inOrderRec, preOrderRec


def createBST(arr, start, end):

    if start > end:
        return None

    node = Node(arr[start])

    # find the i step 2, very crucial here
    i = start + 1

    while i<= end:
        if(arr[i] > node.val):
            break
        i+=1

    node.left =createBST(arr, start + 1, i-1)
    node.right = createBST(arr, i, end)

    return node


#driver for this
preOrder = [10, 4, 2, 8, 5, 9, 15, 12, 20]
root = createBST(preOrder,0, len(preOrder ) - 1)

# we did it it was a success
preOrderRec(root)