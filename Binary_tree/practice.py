from Binary_tree.BSTNode import TreeNode


#build from sorted array
#left, center, right

# root, left, right

# here they both exist
def printLeftSide(root):

    # need to go thru each level
    q = []
    q.append(root)

    while q:
        n = q.pop(0)

        sizeOfCurLevel = len(q)

        for i in range(sizeOfCurLevel):
            if i ==0:
                print(n.val)
            if n.l:
                q.append(n.l)

            if n.r:
                q.append(n.r)

            i+=1

