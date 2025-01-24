from collections import defaultdict, deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Create a graph in adjacency list format
    graph = defaultdict(list)

    # Initialize indegree array to count prerequisites for each course
    indegrees = [0] * numCourses

    # Build the graph and fill indegrees based on prerequisites
    for course, prereq in prerequisites:
        graph[prereq].append(course)  # Add course to prereq's adjacency list
        indegrees[course] += 1  # Increment indegree of the course

    # Start with courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if indegrees[i] == 0])


    '''
    What does the queue look like here?
    '''

    print("queue is ", queue)
    # Counter for number of courses with no remaining prerequisites
    completed_count = 0

    # Process courses in topological order
    while queue:
        # Pop a course with no remaining prerequisites
        course = queue.popleft()
        completed_count += 1

        # Decrease the indegree of course's successors
        for successor in graph[course]:
            indegrees[successor] -= 1

            # If successor now has no prerequisites, add to queue
            if indegrees[successor] == 0:
                queue.append(successor)

    # If all courses have been completed, return True, otherwise False
    return completed_count == numCourses


# so here there is one course that has no prerequisite here
# which is 0
'''
The graph will look the following first 
g = {0:[1,2], 1:[3], 2:[3], 3:[]}

We can take the course 0 because it has no prerequisite 
'''
numCourses = 4; prerequisites = [[1,0],[2,0],[3,1],[3,2]]

canFinish(numCourses, prerequisites)