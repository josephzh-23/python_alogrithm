

'''

Given an integer randomly of k numbers
Do this wihtout using extra memory or sapce here

Randomly output k numbers and return as an integer array here

The above is very important here
Write an algo thatn runs in O(n) here

[ 6, 8, 2, 1, 3, 10, 4]
k = 3

Reservoir sampling problem here
'''
import random

def randomPickIndices_first_variant_398(nums, k):
    result = nums[:k]
    '''
    
    Going from k to len(nums)
    k = 3 
    r = 1 
    
    this makes sure we are making this unique here 
    results[1] = nums[3]
    '''
    for i in range(k, len(nums)):
        n = i + 1

        r = random.randint(0, n - 1)
        if r < k:
            result[r] = nums[i]

    return result