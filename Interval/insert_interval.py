from typing import List

'''
The problem states that you need to have 

Insert the new interavl so that no overlapping intervals here 

- return interval after the insertino here 

[[1, 3], [6, 9]]    and then newInterval = [2, 5] 

[[1, 5], [6, 9]] 
'''

'''
When presented with the task of inserting a new interval into a list of non-overlapping intervals, 

my initial thought is to iterate through the existing intervals while maintaining the sorted order. The key is to handle three cases: intervals that come before the new interval without overlap, intervals that overlap with the new interval, and intervals that come after the new interval without overlap.

Approach
1 ) 
Iterate through all intervals that end before the start of the new interval and add them to the result list.
        
2) 
For intervals that overlap with the new interval (intervals that start before or at the same time as the end of the new interval),
 merge them by updating the start to the minimum of the current starts and the end to the maximum of the current ends.
    when overlap 
        new interval = [min(curStart, start), max(end, curEnd)
 
 3) 
Once there are no more overlapping intervals, add the merged new interval to the result list.
Finally, add all remaining intervals that start after the end of the new interval to the result list.
Complexity

    when overlap:
        
Time complexity: The time complexity is O(n) because we have to iterate through all the intervals once.
Space complexity: The space complexity is O(n) for the result list that we return, which contains the merged intervals.
'''


# and this is it here
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        '''
        So like this question here we have the code here
        [[1,2],[3,5],[6,7],[8,10],[12,16]],  new interval [4, 8] and then it becvomes 
        
        
        [[1,2],
        '''
        # Add all intervals before the new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Now there is the overlap here then we can have

        # the 2 intervals in questions is  [6, 7] and [4, 8]

        # Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
        # So this becomes [3, 10 ]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)

        # Add all the remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return resultIntervals[0]