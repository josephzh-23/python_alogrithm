'''


Cousin in binary tree here

- and then here
'''
from Binary_tree.BSTNode import TreeNode


def solution(r, x , y):

    '''
    
    Depth speaks to the current depth here 
    '''

    def dfs(r, parent, depth):

        if not r:
            return
        print('come here', r)
        if r.val == x:
            res.append((parent, depth ))
        if r.val == y:
            res.append((parent, depth ))


        dfs(r.l, r, depth + 1)
        dfs(r.r, r, depth + 1)
    res = []

    dfs(r, None, 0)
    print(res)
    t1, t2 = res

    # same height but different parent here
    return( t1[0] != t2[0] and t1[1] == t2[1])
r = TreeNode(1)
r.l = TreeNode(2)
r.r = TreeNode(3)
r.l.r = TreeNode(4)
r.r.r = TreeNode(5)
print(solution(r, 4, 5))