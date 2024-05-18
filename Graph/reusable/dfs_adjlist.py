'''
The video link as above as shown before
'''


graph = {
    'A': ['B', 'C', 'D'],
    'B':['E'],
    'C':['D', 'E'],
    'D':[],
    'E':[]
}
visited =set()
def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)

        for neigh in graph[root]:
            dfs(visited, graph, neigh)

dfs(visited, graph, 'A')




