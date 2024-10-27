'''

1. Sort the intervals based on starting pt

2. Use a minheap to keep track of the end time of the last interval added in each group

3.
For each interval, check the root of the min-heap, which gives the earliest end time of all groups. If the
start of the current interval is greater than the earliest end time,

cur.start >= earliest.end
                            as you said we can just add it
this means that we can add the interval to this group without overlaps, and thus,
we replace the old end time with the end time of the current interval by
popping the root of the heap and pushing the new end time.

4. If cur.start < earliest.end
It means this overlaps with everyone, we need to start a new group here then


5. The size at the end represents what we have

The size of the heap at the end denotes the minimum number of groups needed,
as each item in the heap represents a group's latest end time and all intervals within that group that do not overlap.


'''
from Queue_heap.max_heap import MinHeap



'''
Then the problem then becomes 


'''


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
intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
solution(intervals)