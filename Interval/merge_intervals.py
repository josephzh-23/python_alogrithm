

'''
intervals[i] = [starti, endi] here

and then here we have the code

[1, 3], [2, 6]


Above is the solution here


'''
from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:

        endTime, startTime = interval
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.


        # [1, 2 ] , [4, 5]
        # and 2 < 5 we can add it here
        if not merged or merged[-1][1] < startTime:
            merged.append(interval)
        else:

            # [1 , 3], [2, 4] ->  and then this becomes [1, 4]

            # and here this is good ?
            # then becomes what ?
            # so the end gets updated
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])


        # and the above should work here
    return merged