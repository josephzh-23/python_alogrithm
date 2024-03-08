"""
If we were to partition here

Appraoch 1
We can choose either to take or not take an element as said
this results in O (k * 2^n)

To reduce this, everyt time we find a sub set that satisifies the condition we can then remove
it so we get (k -1 ) as said

"""

def canPartitionKSubsets(nums, k)-> bool:

    # not divislbe by k here so no answer possible here
    if sum(nums) %k :
        return False
    target = sum(nums)/k

    # we use this to make sure that used numbers can not be used
    used = [False] * len(nums)

    def backtrack(i, k, subsetSum):
        if k == 0:
            return True

        if(subsetSum == target):
            return backtrack(0, k-1, 0)

        for j in range(i, len(nums)):
            if (used[j] or subsetSum + nums[j] > target):
                continue

            used[j] = True
            if (backtrack(j + 1, k, subsetSum + nums[j])):
                return True
            used[j] = False

        return False
    return backtrack(0, k, 0)