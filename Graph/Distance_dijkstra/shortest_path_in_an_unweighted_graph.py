'''

What you will be given
edges[][] = [[0, 1],
[1, 2], [0, 3], [3, 4] , [4, 7], [3, 7], [6, 7], [4, 5], [4, 6], [5, 6]]
'''



'''
What you will need
1) 
You need a distance matrix dist[0, 1 ..., v-1] such that dist[i] stores the distance 
of vertex i from src vertex 

2) array par[0, 1... , v-1] 



'''

def solution():

    # v here is the # of edges here
    V = 5
    par = [-1] * V