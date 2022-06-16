

# if we know target > mid
# do we go left or go right?
'''
 4  5   6   7   0   1   2
 L          mid            R
    if target =5, 5 < 7, and it's > 4, then search on left of mid
otherwise search on right of mid. This seems like the normal flow of things

'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # Focus on left sorted portion
            if nums[l] <= nums[mid]:

                # 4  5   6   7   0   1   2
                # search in right portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # search in left portion
                else:
                    r = mid - 1

            # right sorted portion
            else:
                # then search on the left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # then search on the right
                else:
                    l = mid + 1
        return -1