'''

Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

'''

# step 1: sort by the starting point here,keep track of the pointers here if overlap or not here

'''
3 possibilities here 
[2, 4]
        [5, 8]
1.  Non-overlapping : 
we only need to move the previous pointer (j) to the next pointer(i),
Count of interval not changed here 

[5, 8]
    [7, 9] 
2. cur endpoint > next index starting 
In this case, the greedy approach is, we can remove 
the next (later) interval and compare it with the next interval,

[1, 9]
[3, 4]
the current endpoint > than the next index endppoint here 
 Since we want the minimum number of intervals to be removed to make the rest of the intervals non-overlapping, we can rem
 ain the next (later) interval. Hence, the previous pointer(j) is updated to the current interval(i).
'''


def overlapIntervals(intervals):
    # by the starting point here
    intervals.sort(key = lambda x: x[0])
    countRemove = 0

    # j -> current end
    j =0
    for i in range(0, len(intervals)):
        nextStartIndex = intervals[i][0]
        nextEndIndex = intervals[i][1]

        curEnd = intervals[j][1]

        if curEnd > nextStartIndex:
            countRemove +=1

            # cur end bigger?
            if nextEndIndex < curEnd:
                j = i

            '''
            Non-overlapping case here 
            [2, 4]  [5, 8] 
            the becomes [5, 8] move up by 1 index here 
            '''
        else:
            j = i

    return countRemove






