from Binary_Search_Tree.BSTNode import Node


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
            if n.left:
                q.append(n.left)

            if n.right:
                q.append(n.right)

            i+=1

