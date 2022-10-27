from typing import List


class Solution:
    def countConnectedComp(s, n, edges:List[List[int]])->int:

        # at the begining, each node is a parent of itself
        par = [i for i in range(n)]
        rank = [1] *n

        def find(n1):

            res = n1
            # not the parent of itself
            while res != par[n1]:
                # not connected
                par[res] = par[par[res]]
                res = par[res]
            return res
