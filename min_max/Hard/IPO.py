'''

At most distinct k projects before the IPO

Maximize total capital

You are given n projects where the ith project has a pure profit profits[i] and
 a minimum capital of capital[i] is needed to start it.

 You have w capitals

 - Finish proj -> get profit -> profit added


 At most k distinct proj maximize capitals
'''
from typing import List

from Queue_heap.max_heap import MaxHeap, MinHeap

'''

The solution to this problem involves sorting projects by their capital requirements
 and using a greedy approach to pick projects that 
 can be started with the current available capital and yield the highest profit.

Firstly, we need to categorize projects based on whether they are within our current capital capabilities. 
We use two heaps (priority queues) to do this: 

h1 for projects we cannot afford yet, and 
h2 for profitable projects we can do right away. 

    h1 is min-heaped on capital required, so projects requiring less capital are at the top. 
    Heap h2 is max-heaped on profits
    so the most profitable projects we can afford are at the top.

The algorithm proceeds as follows:

    Pair each project's capital and profit and push them into h1.
    Heapify h1 to structure it according to the minimum capital required.
    For up to k projects, do the following:
    Move projects from h1 to h2 if they can be afforded with the current capital w.
    If h2 has projects, pop the project with the maximum profit, add that profit to w.
    If h2 is empty, it means there are no more projects that can be done with the current capital, and we break the loop.
    Decrease k by 1 because a project has been completed.
    By following this approach, we ensure that with each iteration, we are choosing the most profitable project that can be started with the available capital. Once k reaches zero or there are no projects left that can be afforded, the algorithm ends. The value of w at this point is the maximized capital we aimed to find.

'''


def findMaximizedCapital(k: int, startingCapital: int, profits: List[int], capital: List[int]) -> int:
    '''
    h1 : stuff we can't afforrd yet
    h1 is min-heaped on capital required, so projects requiring less capital are at the top.

    h2: is max-heaped on profits
    so the most profitable projects we can afford are at the top.
    '''
    min_heap_by_capital = [(c, p) for c, p in zip(capital, profits)]
    h1 = MinHeap()

    '''
    Using the xample above 
    profits = [1, 2, 3];  capital = [0, 1, 1]
    
    The above h1 would look like the following
        h1 = [[0, 1], [2, 1], [3, 1]]
        
    '''
    for e in min_heap_by_capital:
        h1.push(e)
    h2 = MaxHeap()
    print(h1.pop())

    while k:

        '''
         Extract from h1 the proj with smallest capital from h1 and push it into 
         h2 
         h1 = [[0, 1], [2, 1], [3, 1]]
        '''
        while h1 and h1[0][0] <= startingCapital:
            '''
            Here we are pushing the smallest profit to the maxHeap
            '''
            h2.push(h1.pop()[1])

        '''
        If no proj available in max
        
        '''
        if not h2:
            break

        # Pop the project with the highest profit from the max heap and add it to our current capital.
        startingCapital += h2.pop()
        k -= 1

    return startingCapital


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
findMaximizedCapital(2, 0, profits, capital)
