'''

Problem is
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.



The idea is to convert an

1. Use a hashmap first
2. Each key a unique number here from nums, and its corresponding value of
how many times it appears

3. # of distinct integers = # of rows it spreads over


we only add a new row when it's necessary – that is,
when the number of occurrences of the current number exceeds the current number of rows in the ans array.
'''
from collections import Counter


def populateArray(nums):
    cnt= Counter(nums)
    ans = []
    for number, count in cnt.items():
        for i in range(count):

            # check if the current row i exists in ans, if not create a new row(an empty list)
            # if ans has 0 [], and if we have {6: 3}
            # then at least 3 brackets are needed here and not just this then
            if len(ans) <=i:
                ans.append([])

            ans[i].append(number)
    return matrix











