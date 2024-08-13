from String.String_Array.findMode import List






def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    # for iterarigng the index and value
    for i, a in enumerate(nums):

        # that means this is the same value as before [-3 -3,
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1

            # the case where it equals
            else:
                res.append([a, nums[l], nums[r]])
                l += 1

                # Again checking for duplicate here
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res