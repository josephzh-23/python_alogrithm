from typing import List

# has to run in O(n) time
''' 
    To solve this problem 
    
    The explanation for this is 
    Look at code [100, 4, 200, 1, 3 , 2]
    
    can be broken down into 3 sequences
    [1 2 3 4]   [100]   [200] 
    How to know when sequence starts? When it ends?
    
    1. Take 1, it starts b/c 0 is not there
    2. Take 4, it ends b/c there is no 5. 

'''

def longestConsecutive( nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        print(n)
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1

            # Check if our set has the next value
            # Ex: if 1, it would be 2, and then 3
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))