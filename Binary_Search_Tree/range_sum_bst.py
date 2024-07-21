'''
low and high and then find all the inclusive range here



Using dfs here since

node.val < low (then it will be on the outside)

'''

def rangeSumBST(r, low, high):

    ans = 0

    # to start off here
    cur = r
    stack = []


    stack = []
    stack.append(r)

    while stack:
        node = stack.pop()
        if node:

            # do the traversal here

            if node.lef < node.val < node.right:
                ans += node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return ans