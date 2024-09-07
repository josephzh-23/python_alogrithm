from Binary_Search_Tree.BSTNode import TreeNode


def longestConsecutiveSequence(root: TreeNode) -> bool:
    if not root:
        return False

    finalRes = 0
    curRunning = 1
    st = [root]
    while st:
        node = st.pop()
        print('value is', node.val)
        if not node.l and not node.r:
            finalRes = max(finalRes, curRunning)
        if node.r:
            if node.r.val == node.val + 1:
                curRunning +=1
                print(curRunning)
            st.append(node.r)
        if node.l:
            if node.l.val == node.val + 1:
                curRunning +=1
                print(curRunning)

            st.append(node.l)
    # and then here we have the code here

    print('final is ', finalRes)
    return False
r = TreeNode(1)
r.r = TreeNode(3)
r.r.l = TreeNode(2)
r.r.r = TreeNode(4)
r.r.r.r = TreeNode(5)
longestConsecutiveSequence(r)

















