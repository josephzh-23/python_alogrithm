from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    ranges = []
    i = 0

    while i < len(nums):
        start = nums[i]

        '''
        
        When this exits 
        nums[i] will then be the last one that is not continuous 
        [0, 1, 2, 4]
        
        nums[i[ will be 2 
        '''
        while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1

        print('nums[i] is', nums[i])
        if start != nums[i]:
            ranges.append(str(start) + "->" + str(nums[i]))

            # this is to take care of the last case
        else:
            ranges.append(str(nums[i]))

        i += 1

    return ranges


nums= [0, 1, 2, 4, 5, 7]
summaryRanges(nums)