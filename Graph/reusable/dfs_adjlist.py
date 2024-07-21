'''
The video link as above as shown before
'''
import collections

graph = {
    'A': ['B', 'C', 'D'],
    'B':['E'],
    'C':['D', 'E'],
    'D':[],
    'E':[]
}
visited =set()


'''
The below need to be converted into what was said before 
matrix = [[0, 1], [0, 2], [1, 2], [2, 0]] into 


And that's it over here 
0: [1, 2]
1: [2, 0 ]
2: 0 
'''
matrix = [[0, 1], [0, 2], [1, 2], [2, 0]]
def dfs(points):
    graph = collections.defaultdict(set)
    s = set()
    for a, b in points:
        graph[a].add(b)
        graph[b].add(a)
    print(graph)
    dfsUtil(graph, 0, s)


def dfsUtil(graph, node, visited):
    visited.add(node)
    print('node is', node)

    for neigh in graph[node]:
        if neigh not in visited:
            dfsUtil(graph, neigh, visited)


dfs(matrix)




