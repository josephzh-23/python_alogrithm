'''
THis is important here as we need this a lot

'''
from typing import List


def minimumOperations(self, nums: List[int]) -> int:
    num_sums = 0  # number of merges

    # Task is to balance both sides of the array.
    left = 0
    right = len(nums) - 1

    # Balance left and right side, until both pointers meet.
    while left <= right:
        # If the two edges are balanced, there is no need to change them
        # as it only unbalances the whole array and leads to more merges
        if nums[left] == nums[right]:
            left += 1
            right -= 1
            # No new merges


        # If one side is small, we MUST merge it as we cant reduce the other end
        # Here we will ignore the values in the visited indices as we dont want to mess with the array
        #  and deal with correcting the indices, its unnecessary and wasteful.
        elif nums[left] < nums[right]:
            # merge the one on the left side her e
            nums[left + 1] = nums[left] + nums[left + 1]
            left += 1
            num_sums += 1  # Increase merge count


        # If right side is small update the inner value on the right and move the pointer inside.
        else:
            nums[right - 1] = nums[right - 1] + nums[right]
            right -= 1
            num_sums += 1
    # As you can see, we dont try to make the values equal, we only do what we can thats merge.
    # If they are equal, then great, we move on to make the inner subset x[KYZ]x a palindrome.
    # In the case we dont make the right and left equal we end up merging the whole array as one element
    #  thus making a palindrome, so an answer is guarenteed.