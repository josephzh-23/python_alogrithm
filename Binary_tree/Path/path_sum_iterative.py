from Binary_tree.BSTNode import TreeNode


def pathSum(root, targetSum):
    # Base CAse
    if root is None:
        return

    stack = [(root, targetSum - root.val)]
    while stack:
        node, cursum = stack.pop()


        # the above here is then true
        if not node.r and not node.l and cursum == 0:

            # and now this is done here
            return True
        if node:
            if node.r:
                # print('right val', node.right.val, end=" ")
                stack.append((node.r, cursum - node.r.val))
            if node.l:
                stack.append((node.l, cursum - node.l.val))

    return False
            # if node right here

r = TreeNode(1)
r.l = TreeNode(2)
r.r = TreeNode(3)
print(pathSum(r, 3))