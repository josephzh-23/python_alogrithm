'''
Best way to do this is you have mulitple rooms here , u don't know what's availalble
at all times in this case

1. Use a way to check if a room is availalbel or not here

2. This would be the perfect way to check here

Keep all the meeting in a minheap where the 


Keep track of the ending time of when sth is free and opens up here

Whatever is left is the very end here
'''
from Queue_heap.max_heap import MinHeap


def solution(intervals):
    # and we sort by the ending value as said so
    # the ending will always be at the very end here

    # and that's it here
    intervals.sort(key=lambda x: x[1])

    # and then

    minHeap = MinHeap()

    # the first one here very important
    minHeap.push(intervals[0])

    for i in range(1,len(intervals)):

        # cure
        cur = intervals[i]
        earliest = minHeap.pop()

        # check for conflict here
        # if the current start >= earliest meeting ending here
        if cur[0] >= earliest[1]:
            earliest[1] = cur[0]

        # else there is a conflict between the meeting
        #cur.start < earliest.end

        # else we push the current to it and that's it here
        else:
            minHeap.push(cur)

        minHeap.push(earliest)
        print(minHeap.__len__())

intervals = [[0,30],[5,10],[15,20]]


solution(intervals)








