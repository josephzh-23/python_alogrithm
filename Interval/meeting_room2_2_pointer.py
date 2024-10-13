'''

The 2 pointer approach nothign else used here
'''
from typing import List

'''

Extract and Sort Times: First, extract the start and end times from the intervals and sort them.

1) 
Two-Pointer Technique: Use two pointers, one for the start times and one for the end times, to iterate through the sorted lists.

2) 
Counting Rooms: Increment the room count whenever a meeting starts and decrement it when a meeting ends.

And the answer is basically and thisi is very important here 
Track Maximum Rooms: Track the maximum number of rooms used simultaneously,
 which gives the required number of rooms.
'''


def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    # Base case: If there are no intervals, no meeting rooms are needed.
    if not intervals:
        return 0
    # this is the same as
    # Extract start and end times from the intervals.
    start = [i[0] for i in intervals]
    end = [i[1] for i in intervals]

    # Sort start and end times.
    start.sort()
    end.sort()

    # Initialize two pointers for start and end times and counters.
    s = e = 0
    counter = 0
    max_count = 0

    # Iterate through all intervals.
    while s < len(intervals):

        # [1, 5, 3] < [4, 5, 6]
        # If a meeting starts before another one ends, increment the room count.
        if start[s] < end[e]:

            # Look at 1, 4 one room is needed here and then 1 room is needed here
            counter += 1
            s += 1

            '''
            
            If we have the following here  [1, 5, 6], [3,4, 6]
             at i = 1 5  > 4 
             
             we can use the first room for this room here and that's very important here 
            then increment the end pointer 
            '''
        else:
            # If a meeting ends, decrement the room count.
            counter -= 1
            e += 1

        # Keep track of the maximum number of rooms needed at the same time.
        max_count = max(max_count, counter)

    # Return the maximum number of rooms needed.
    return max_count
