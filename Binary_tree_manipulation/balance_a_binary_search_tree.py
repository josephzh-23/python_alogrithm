'''
This is quite important here

'''
from Binary_tree.BSTNode import TreeNode


# return the max index
def findMax(arr, start, end):
    maxValue = arr[start]
    maxIndex = start

    # need to iterate the whole thing here
    for i in range(start+1, end+1):
        if arr[i] > maxValue:
            maxValue = arr[i]
            maxIndex = i

    return maxIndex

def buildTree(array, start, end):

    if start > end:
        return None


    maxIndex = findMax(array, start, end)

    root = TreeNode(maxIndex)

    # If this is the only element in
    # inorder[start..end], then return it
    if start == end:
        return root

    root.l = buildTree(array, start, maxIndex - 1)
    root.r = buildTree(array, maxIndex + 1, end)

    return root


# and then here

root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)
root.l.l.l = TreeNode(7)











