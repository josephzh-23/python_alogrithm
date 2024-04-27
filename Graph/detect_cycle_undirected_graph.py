# so if the input is as following:
import collections
from typing import List

arr = [[1, 0], [0, 3], [3, 2]]
# there is a cycle here


def checkCycle(numCourse: int, preReq: List[List[int]]):
    graph = collections.defaultdict(list)
    for course, pre in preReq:
        graph[pre].append(course)

    print(graph)

    # now for checking cycle

    def dfsCycle(node,onPath, visited):
        onPath.add(node)
        visited.add(node)

        for neigh in graph[node]:
            print('neighbor is ', neigh)
            if neigh in onPath or dfsCycle(neigh, onPath, visited):
                return True

        onPath.pop(node)
        print(onPath)
        return False
    print(numCourse)

    visited = set()
    onPath = set()
    for n in range(numCourse):
        print(n)
        if n not in visited and dfsCycle(n, onPath, visited):
            return True
    return False
print(checkCycle(2, arr))

