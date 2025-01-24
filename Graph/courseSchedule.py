import collections
from typing import List



'''
We will create a map here 
    0 : [1, 2]
    1: [3, 4]
    
    if a cycle is found -> then can't finish the course 
    
    Ex:
    numCourses = 2, prerequisites = [[1,0],[0,1]]
    
    Basically we use a DFS approach to check for cycle
    Note that you should make two array to keep track 
    1.Visited
    We use a vector visited to record all the visited nodes and
     
     2. onPath
        vector onpath to record the visited nodes of the current DFS visit.
     Once the current visit is finished, we reset the onpath 
     value of the starting node to false.
     in the for loop 

'''
class Solution:
    def canFinish(s, numCourses:int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        for course, pre in prerequisites:
            adjList[pre].append(course)

        def dfsCycle(node, onPath, visited):


            #say it's 3, neighbors 1, 2, 4
            onPath[node] = True
            visited[node] = True
            for neighbor in adjList[node]:
                if onPath[neighbor] or dfsCycle(neighbor, onPath, visited):
                    return True

                # pop because next time we would be on a different path
            onPath[node] = False
            return False

        visited = [False] *numCourses
        onPath = [False] * numCourses
        for n in range(numCourses):
            # initialized newly for each path to take
            if not visited[n] and dfsCycle(n, onPath, visited):
                return False

        return True


# Python3 program to check whether we can finish all
# tasks or not from given dependencies.

test = [[0, 1],[2, 3],[1,2]]
s = Solution()
print(s.canFinish(3, test))

