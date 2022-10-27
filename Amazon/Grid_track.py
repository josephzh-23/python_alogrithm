from Graph.BFS import queue

grid = ['abc', 'abd', 'ccd']

# the best way to approach this would be to
'''

graph = {
    'A': ['B', 'C', 'D'],
    'B':['E'],
    'C':['D', 'E'],
    'D':[],
    'E':[]
}
'''
# you can transform this first into a dict with the 2 items
def transFormListIntoDict(graph):

    d = dict()
    n = len(graph)
    adj = {u: [] for u in range(n)}
    i = 0

    for row in graph:

        # a new one
        if row[i] not in d:
            d[row[i]] = []


        i+=1

    print(d)


transFormListIntoDict(grid)


