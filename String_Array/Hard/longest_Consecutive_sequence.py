from typing import List

# has to run in O(n) time
''' 

0. Need a set, a for and while loop
1. 
    To solve this problem 
        -
    The explanation for this is 
    Look at code [100, 4, 200, 1, 3 , 2]
    
    can be broken down into 3 sequences
    [1 2 3 4]   [100]   [200] 
    How to know when sequence starts? When it ends?
    
    1. Take 1, it starts b/c 0 is not there     start = 1 in this case
        while (n + start) in numSet:
            start += 1

'''

def longestConsecutive( nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        print(n)

        # n could be 4, and so we check if 3 is there
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            start = 1

            # Check if our set has the next value
            # Ex: if 1, it would be 2, and then 3
            while (n + start) in numSet:
                start += 1
            longest = max(start, longest)
    return longest
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))