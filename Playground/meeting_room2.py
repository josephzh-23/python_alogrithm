'''

Meeting room 2 problem here
'''
from sorting.Heap import MinHeap

'''
Sort the given meetings by their start time.
Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
If not, then we allocate a new room and add it to the heap.
After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

'''

def meetingRoom2(intervals):

    # would contain all a list of the end times here
    freerooms = MinHeap(32)


    # if we sort the meetign here and then we can keep starting
    # this would be the max here and very important stuff to come and then next we have sth
    intervals.sort(key = lambda x: x[0])

    # add first meeting
    freerooms.insert(intervals[0][1])
    # now for the remaining here
    # for remaining here
    for meeting in intervals[1: ]:
        # 5 < 12
        if freerooms.peek() <= meeting[0]:
            freerooms.removeMin()
        # fi the new room is then assigned here we have this here

        # assign the end time to this meeting here
        freerooms.insert(meeting[1])
    return freerooms.size

intervals = [[0, 30], [5, 10], [15, 20]]
print(meetingRoom2(intervals))
