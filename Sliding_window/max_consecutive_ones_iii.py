'''
When we get to a point where k < 0 then need to move pointer again here
- Start removeing 0 that we took

Where thsi is a 2 pointer apporach here


'''


def longestOnes(nums, k) -> int:
    l = maxCons = 0

    for r, num in enumerate(nums):

        '''
        This is just for simplifying here 
        if k = 1, 1-1 = 0 
        if k = 0, 1-0  = 1
        
        '''
        k -= 1 - num

        if k < 0:
            '''
            A simpler approach down here 
            What this means is if nums[l] = 1 
            then nothing happens to k,
            
            if nums[l] = 0 , then we are giving 1 back to k
            '''
            k += 1 - nums[l]

            # then
            l += 1

        # this is the case where k > 0, still valid here 
        else:
            maxCons = max(maxCons, r - l + 1)

    return maxCons
