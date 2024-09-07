'''
Min swap to group all ones together here



'''

# start with array first and then
def ans(nums, target):
    l = 0
    r = 0
    numOfOnes = 0

    while r < len(nums):

        while nums(l) ==1:
            numOfOnes = min(numOfOnes, r - l + 1)
            l += 1
        r += 1
    return numOfOnes if numOfOnes != float('inf') else 0