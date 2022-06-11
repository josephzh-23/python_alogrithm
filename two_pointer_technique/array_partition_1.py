
'''

Given an integer array nums of 2n integers, group these integers into n pairs
 (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi)

  for all i is maximized. Return the maximized sum.
'''
# This problem is called Array_hash Partition 1
def arrayPairSum( nums):

    nums.sort()
    i=0
    sum =0

    while i < len(nums) -1:
        sum += nums[i]
        i+=2
    return sum

nums = [1, 2, 3, 5]
print(arrayPairSum(nums))