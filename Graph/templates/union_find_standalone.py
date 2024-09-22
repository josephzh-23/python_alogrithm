'''

This is the improved versino here

- The TC here becoems

find : log(n) and union : log(n) here

'''


# there is also an example of how to use this code here
# in below as you can see on the left or in the code 

class DisJointSets():
    def __init__(self,N):
        # Initially, all elements are single element subsets
        self.parents = [node for node in range(N)]
        self.ranks = [1 for _ in range(N)]

    def find(self, u):
        while u != self.parents[u]:
            # path compression technique
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        return u

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        # Union by rank optimization
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if self.ranks[root_u] > self.ranks[root_v]:
            self.parents[root_v] = root_u
        elif self.ranks[root_v] > self.ranks[root_u]:
            self.parents[root_u] = root_v
        else:
            self.parents[root_u] = root_v
            self.ranks[root_v] += 1
        return False