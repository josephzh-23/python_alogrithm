'''
The video link as above as shown before
'''
import collections

from Graph.flood_fill import isValid
from Graph.reusable.dfs_matrix import directions

graph = {
    'A': ['B', 'C', 'D'],
    'B':['E'],
    'C':['D', 'E'],
    'D':[],
    'E':[]
}
visited =set()


'''
isConnected = [[1,1,0],
[1,1,0],
[0,0,1]]


if i and j the same alwasy connected here anyways
0 -1 good 
2 -1 good 
3 - 3 connected
isConnected[i][j] = 1




How to return a value from dfs here? 

'''
matrix = [[0, 1], [0, 2], [1, 2], [2, 0]]

def dfs(node, isConnected, visit):
    visit[node] = True
    for i in range(len(isConnected)):
        if isConnected[node][i] and not visit[i]:
            dfs(i, isConnected, visit)


def findCircleNum(isConnected):
    n = len(isConnected)

    numberOfComponents = 0
    visit = [False] * n
    for i in range(n):
        print(n)
        if not visited:
            numberOfComponents +=1
            dfs(i, isConnected, visit)
    print(numberOfComponents)
    return numberOfComponents


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
findCircleNum(isConnected)

