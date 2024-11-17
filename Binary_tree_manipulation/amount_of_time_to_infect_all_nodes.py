'''


This is quite interesting

Imageine if we have the following

       1
      / \
     2   3
        / \
       4   5

Then the above would be transformed into the following:

1. We can use dfs to convert the above here

2.
'''
from collections import defaultdict


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def amountOfTimeToInfectAllNodes(root, start):
    # Graph represented as an adjacency list
    graph = defaultdict(list)
    def dfs(node):
        if node:

            if node.left:
                graph[node.left.value].append(node.value)
                graph[node.value].append(node.left.value)

            if node.right:
                graph[node.right.value].append(node.value)
                graph[node.value].append(node.right.value)
            # First recur on left child

            '''
            The ones below are number 1 thing here 
            
            And then what's important is figuring out the next part 
            '''
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    queue = [start]
    seen = set()

    '''
    And when does this end though? that's an interesting question
    
    
    
    '''
    time = 0
    while queue:
        time +=1
        for _ in range(len(queue)):
            cur = queue.pop(0)
            seen.add(cur)
            for neighbour in graph[cur]:
                if neighbour not in seen:
                    queue.append(neighbour)

    # the above here is important

    print('time is', time)
    return time

'''
The above is the tree node here and then we have 

'''

r = TreeNode(1)
r.right = TreeNode(3)
r.left = TreeNode(5)

r.right.right = TreeNode(6)
r.right.left = TreeNode(10)

r.left.right = TreeNode(4)
r.left.right.right = TreeNode(2)
r.left.right.left = TreeNode(9)
start = 3

amountOfTimeToInfectAllNodes(r, 3)