'''
Best way to do this is you have mulitple rooms here , u don't know what's availalble
at all times in this case

1. Use a way to check if a room is availalbel or not here

2. This would be the perfect way to check here

Keep all the meeting in a minheap where the 


Keep track of the ending time of when sth is free and opens up here


'''
from Queue_heap.max_heap import MinHeap


def solution(intervals):
    # and that's #1 here
    intervals.sort(key=lambda x: x[1])

    # and then

    minHeap = MinHeap()

    # the first one here very important
    minHeap.push(intervals[0])

    for i in range(0, )












