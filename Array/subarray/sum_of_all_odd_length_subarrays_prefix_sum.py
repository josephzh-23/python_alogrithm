'''
We will keep a for loop with a running map here to make things simple here

Can be applied to
1) Count number of nice subarrays prefix sum problem here

'''
from typing import List

'''

Using this we basically reduce it down from the original brute force approach here 
[1, 4, 2, 5, 3] here 
'''
def sumOfOddLengthSubarrays(nums):
    n = len(nums)
    res= 0
    prefixSum = [0] *n

    for i in range(1, n):
        prefixSum[i] = prefixSum[i -1 ] + nums[i]



    # and the above is it for this soultion here
    for i in range(0, n):
        for j in range(i, n):

            if j - i + 1 %2 == 0:
                continue

            if i - 1 < 0: res += prefixSum[j]
            else: res += prefixSum- prefixSum[i-1]
    return res




