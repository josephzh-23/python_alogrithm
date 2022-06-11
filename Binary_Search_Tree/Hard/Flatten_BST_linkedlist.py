

# validate binary search tree here
from Binary_Search_Tree.BSTNode import Node, insert

'''
    1       1
  2   5       2 
3  4    6       3
                  4
                    5
                      6
    Can use preorder traversal for this 
'''

def flattenBSTIntoLinedlist(root):

    if root is None:
        return None

    s = []
    s.append(root)

    while s:
        cur = s.pop()

        if cur.right:
            s.append(cur.right)

        elif cur.left:
            s.append(cur.left)

        # if the stack not empty
        '''
            this sets 1 to point at 2, because it was pushed in
        last
               1 
                 2 
                   3
                     4  
        '''
        if s:
            cur.right = s[-1]
        cur.left = None

node = Node(4)
insert(node,5 )
insert(node, 6)
insert(node, 7)
insert(node, 8)
flattenBSTIntoLinedlist(node)
print(node)
