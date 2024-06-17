# Using a good subarray here


'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.


Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum.

The values are [23, 2, 4, 6, 7] k = 6 here

And then [2, 4] is a continuosu process here subarray of size


# return true if this has the array that we are looking for as said


Graphically what this means is that
Hashmap
[23, 2, 4, 6, 7]    if k = 6 here then it becomes obvisou that we have
23 % 6 = 0      idx 0
25 % 6 = 1      idx 1
29 % 6 = 5      idx 2

    remainder   index
        5       0
        1       1
        5       2       And then here we already have 2, 4 as the answer
'''

def keepCheckingUntilSumEquals(nums, k):
    '''
   Build a remainder and an end index here
    '''

    remainder = {0: -1 } #map the remainder -> end index
    total= 0
    for i, n in enumerate(nums):
        total += n
        r= total % k

        # store that remainder here or, so the following code would be ok as said
        if r not in remainder:
            remainder[n] = i
        elif i - remainder[r] >=2:
            return True

    return False