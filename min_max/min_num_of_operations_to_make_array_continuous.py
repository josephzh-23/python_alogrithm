"""

1, 2, 3, 5, 6

Choose an x here in the code
Make an [x, x + n - 1] above
if x = 1 , x + n - 1 = 5

[1, 2, 3, 5]    we can see above missing a 4        O(n^2)
So have a left and right pointer with the left - 1
the regular window = R - l + 1      here would be window = R - l
"""

def minOperations(nums) -> int:
    length = len(nums)

    # need to the set here to avoid duplicate
    nums = sorted(set(nums))
    res = length
    r = 0
    for l in range(len(nums)):
        # nums[l], nums[l] + length - 1
        '''
        this is the window from above nums[l], nums[l] + length - 1
        [1, 5] 
        '''
        while r < len(nums) and nums[r] < nums[l] + length:
            r+=1
        window = r- l
        res = min(res, length - window)
    return res










