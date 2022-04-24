from _ast import List


def permute(nums: List[int]) -> List[List[int]]:

    result = []

    #base case
    if (len(nums) == 1):
        return [nums[:]]

    for i in range(len(nums)):
        # pop the 0th char, which if starting with [1, 2, 3]
        # start with 1
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        # add multiple values to a result array
        result.extend(perms)

        # n is what we removed at the beginning
        nums.append(n)
    return result