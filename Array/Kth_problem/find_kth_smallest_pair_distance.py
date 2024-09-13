

'''
The distance of a pair [a, b] defined as abs diff between a and b,
 teh kth distance amonng all the pairs
 [1, 3,1]       -

We want the kth smallest pair distance here

 determine whether there're at least k pairs whose distances <= distance

 1. Sort the array given 2 inputs here have 2 pters,
 2. Both pters go from left most

 3. If the current pair pointed at has a distance <= distance, all pairs between these pointers
 are valid (since the array is already sorted),
 if cur pair ditsnance > distance, move forward the slow pointer, by the time both reach the end, scan i
 is done see if total exceeds k here
 
  4.

  '''
from typing import List


def smallestDistancePair(nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    left, right = 0, nums[-1] - nums[0]
    while left < right:
        mid = left + (right - left) // 2
        if enough(mid):
            right = mid
        else:
            left = mid + 1
    return left


def enough(distance, nums) -> bool:  # two pointers
    n = len(nums)
    count, i, j = 0, 0, 0
    while i < n or j < n:
        '''
        If currenlty smaller than go faster here, 
        '''
        while j < n and nums[j] - nums[i] <= distance:  # move fast pointer
            j += 1
        count += j - i - 1  # count pairs
        i += 1  # move slow pointer
    return count >= k