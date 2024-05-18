from typing import List


'''
n = 7, 

edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
 hasApple = [false,false,true,false,true,true,false]
 
 And only here we can collect the apples in this case 
Output: 8 


'''

def minTime(n: int, edges: List[List[int]], hasApple)-> int:

    adj = {i: [] for i in range(n) }

    for par, child in edges:
        adj[par].append(child)
        adj[child].append(par)

    def dfs(cur, par):
        time = 0

        for child in adj[cur]:
            if child == par:
                continue
            childTime = dfs(child, cur)
            if childTime or hasApple[child]:

                '''
                2 here b/c you need to spend 2 seconds to go over 1 edge 
                of the tree, so this is a round trip 
                
                '''
                time += 2 + childTime
        return time

    dfs(0, -1)