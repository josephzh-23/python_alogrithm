'''
CPU idle: no tasks

start : enqueue time
end: tasks

'''
import heapq
from typing import List

from Heap.max_heap import MinHeap

'''Now, one point to note here is that let's say current time is 0, the heap is empty, and the next available task 
will enqueue at 10.
 
 The CPU will sit idle until current time reaches 10. Instead of incrementing current time by 1, 
we will update current time directly to 10, which will reduce the number of iterations in our approach and improve 
the run-time.

1. If queue empty 

then it will be seen immediately 

'''


def getOrder( tasks: List[List[int]]) -> List[int]:


    '''
    Keep the original indexes first before we change the order,

    '''

    for i, t in enumerate(tasks):
        t.append(i)


    tasks.sort(key = lambda t: t[0])

    res, minHeap = [], []

    # time will be the smallest of the bunch here 
    i, time =0, tasks[0][0]


    # Add task index to each task for later reference
    for index, task in enumerate(tasks):
        task.append(index)

    # Sort tasks based on their enqueue time
    tasks.sort()


    '''
    Add the original index here as well, when the enqueuTime condition is met then we can keep 
    adding things here 
    
    '''
    # Initialize the answer list and a priority queue
    hp = MinHeap()

    # Initialize pointers and variables for task processing and time tracking
    num_tasks = len(tasks)
    task_index = 0

    # Process all tasks
    while not hp.isEmpty() or task_index < num_tasks:


        while i < len(tasks) and time >= tasks[i][0]:
            hp.append([tasks[i][1], tasks[i][2]])
            #move to the next current element here
            i+=1

        # move the current time if the queue is then empty here
        if not hp:
            time = tasks[i][0]
        else:
            procTime, index = hp.pop()

            time+= procTime
            res.append(index)
    return res












