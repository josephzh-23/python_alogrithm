

'''

Solution page: 254
THis is question 4.3 from the cracking coding interview book

Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth

(e.g., if you have a tree with depth D, you'll have D linked lists).
This is very simple


Strategy:
    pass in level + 1 to the next recursive call with DFS preorder here as well
'''

# can do this using DFS as given in the example
from Binary_tree.binaryTree import Node


def createLevelLinkedlistUtil(root, lists, level):

    #base case
    if not root:
        return

    list = []
    # the current level not contained in the list
    if len(lists) == level:
        '''
        I* Levels are always traversed in order. So, if this is the first time we've
    visited level i, we must have seen levels 0 through i - 1. We can
    therefore safely add the level at the end. 
        '''
        lists.append(list)

    else:
        list = lists[level]

    list.append(root)
    createLevelLinkedlistUtil(root.l, lists, level + 1)
    createLevelLinkedlistUtil(root.r, lists, level + 1)



def createLevelLinkedlist(root):
    lists = []
    createLevelLinkedlistUtil(root, lists, 0)
    return lists


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
val = createLevelLinkedlist(root)

for list in val:
    print(end="\n")
    for item in list:
        print(item.data, end = ",")