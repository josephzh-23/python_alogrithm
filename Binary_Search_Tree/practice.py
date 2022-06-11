from Binary_Search_Tree.BSTNode import Node


def sortedArrayToBST(arr):

    if len(arr) ==0:
        return None
    return buildTreeFromArray(arr, 0, len(arr)-1)


def buildTreeFromArray(arr, left, right):

    if(left < right):
        return None

    mid = (left + right) //2

    root = Node(arr[mid])
    root.left = buildTreeFromArray(arr, 0, mid -1)
    root.right = buildTreeFromArray(arr, mid + 1, right)

    return root

prev = None

def inOrder(cur):

    global prev

    if cur is None:
        return True

    isLeftBST =  inOrder(cur.left)
    if not isLeftBST:
        return False
    if not prev:
        prev = cur
    elif prev >=cur:
        return False
    elif prev <cur:
        prev = cur

    isRightBST = inOrder(cur.left)
    if not isRightBST:
        return False

    return True


def getParentNode(cur, key):

    while cur:

        # 5 > 4
        if cur.val > key:
            par = cur

            cur = cur.left
        elif cur.val < key:
            par = cur

            cur = cur.right

        elif par.val == key:
            return par




def isSubTree(s, t):


    if not t:
        return True
    if not s: return False

    if sameTree(s, t):
        return True

    return isSubTree(s.left, t) or isSubTree(s.right, t)



def sameTree(self, s, t):

    # then they are the same tree
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return (sameTree(s.left, t.left) and
                sameTree(s.right, t.right))
    return False