class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def LevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        CurrentLevel(root, i)


def CurrentLevel(root , level):
    if root is None:
        return
    if level == 1:
        print(root.data,end=" ")
    elif level > 1 :
        CurrentLevel(root.l, level - 1)
        CurrentLevel(root.r, level - 1)


def height(node):
    if node is None:
        return 0
    else :
        lheight = height(node.l)
        rheight = height(node.r)
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
LevelOrder(root)