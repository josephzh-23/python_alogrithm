from Binary_Search_Tree.BSTNode import TreeNode


def pathSum(root, targetSum):
    # Base CAse
    if root is None:
        return

    stack = [(root, targetSum - root.val)]
    while stack:
        node, cursum = stack.pop()


        # the above here is then true
        if not node.right and not node.left and cursum == 0:

            # and now this is done here
            return True
        if node:
            if node.right:
                # print('right val', node.right.val, end=" ")
                stack.append((node.right, cursum - node.right.val))
            if node.left:
                stack.append((node.left, cursum - node.left.val))

    return False
            # if node right here

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
print(pathSum(r, 3))