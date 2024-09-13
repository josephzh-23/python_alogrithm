'''
A lower and upper here


[0, 1, 3, 50, 75]
0 to 99

we can simply check consecutive elements to see if
 they differ by one or not. If they don't, then we have found a missing range.

 nums[i + 1]- nums[i] <= 1      consecutive
 nums[i+ 1] - nums[i] > 1       not consecutive

 However, there are two edge cases:
Edge case 1
If we don't start with lower as the first element of the array,
we will need to include [lower, num[0] - 1] as a missing range as well.

Edge case 2: here
Similarly, if we don't end with upper as the last element of the array,
we will need to include [nums[n - 1] + 1, upper] as a missing range as well where n is the length of nums.
'''
from typing import List

# and then here you have the code
# code here
# case 1:
#We check if the first element of the array is equal to lower or not. If lower < nums[0]
# if lower < num[0],  we have a missing range [lower, nums[0] - 1]. We add it to missingRanges.

'''
If the current element nums[i] and the next element nums[i + 1] differ by 1 or less, 
there are no missing numbers between tehse 2 numbers 

- if nums[i + 1] - nums[i] > 1 is added to the missing ranges here

'''


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        missing_ranges = []
        if n == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges

        # Check for any missing numbers between the lower bound and nums[0].
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        # Check for any missing numbers between successive elements of nums.
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])

        # Check for any missing numbers between the last element of nums and the upper bound.
        if upper > nums[n - 1]:
            missing_ranges.append([nums[n - 1] + 1, upper])

        return missing_ranges