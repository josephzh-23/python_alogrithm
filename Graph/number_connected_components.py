from typing import List


'''
We can use dfs on this as well 

A graph of n nodes, also given edges[i] = [ai, bi] 
indicating an edge between ai and bi in the graph

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

1. At the start par[1] = 1, all parent of element is itself

2. if par[0] = par[2], they are connected
otherwise not connected

Ex: [0, 1]
union-rank find method
1. 0 will be par of itself, make par[1] = 0

[1, 2] 
pare [ 0,  1, 2, 3, 4]
rank [2, 1, 1, 1, 1] 
'''
class Solution:
    def countConnectedComp(s, n, edges:List[List[int]])->int:

        # at the begining, each node is a parent of itself
        par = [i for i in range(n)]
        rank = [1] *n

        '''
        Given a node : find its parent
        '''
        def find(n1):
            # res the root paretn
            res = n1

            '''
            Keep looking for parent node if not found alraedy 
            When we have found the parent node 
            '''
            # if 3 != 4
            while res!= par[res]:

                #set the par[res] = to its grandparent, this is path comppression
                par[res] = par[par[res]]

                # update the current pointer to its parent
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # 0 to indiicate no union
            # if different parent, then not connected
            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[2] = p1
                rank[p1] +=rank[p2]

            # 1 means that we have gotten a successful union
            return 1

        res = n

        # each time we do a union, we reduce sth by 1
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res


s= Solution()
res = s.countConnectedComp(5, [[0, 1], [1, 2], [3, 4]])
print(res)







