
# a list of integers here

# https://leetcode.com/problems/number-of-ways-to-split-array/description/
def waysToSplit(nums):
    splits = 0 # variable to store # of valid splits here
    s = nums[0] # sum to store all elements here

    n = len(nums)
    prefix = [0] * n     # prefix

    for i in range(1, n):
        prefix[i] = prefix[i-1] + nums[i]
        s+= nums[i]


    # creating the splits here
    for k in range(0, n):

        # current sum >= the rest of the sum
        if(prefix[k] >= prefix[n-1] - prefix[k]):
            splits+=1

    print(splits)



nums = [10, 4, -8, 7]
waysToSplit(nums)



