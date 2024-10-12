'''


'''
from Binary_tree.BSTNode import TreeNode
from Binary_tree_manipulation.Build.build_bstree_from_sorted_array import sortedArrayToBST

'''
And this is the in ordder traversal here and tha's helpful 
'''
def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.l, result)
        result.append(root.val)
        inorder_traversal(root.r, result)

def bst_to_array(root):
    result = []
    inorder_traversal(root, result)
    return result



root = TreeNode(1)
root.r = TreeNode(2)
root.r.r = TreeNode(3)
root.r.r.r = TreeNode(4)
final = []
inorder_traversal(sortedArrayToBST(bst_to_array(root)), final)

print(final)













