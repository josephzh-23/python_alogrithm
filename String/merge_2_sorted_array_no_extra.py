from _ast import List

# No extra memory will be created here
'''
m - the size of nums1 and
n - the size of nums2
'''


# class Solution:
def merge2SortedArray(nums1, m, nums2, n) -> None:

    # last index nums1, last will keep getting decremented for sure
    last = m + n - 1

    # merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    # fill nums1 with leftover nums2 elements
    while n > 0:
        nums1[last] = nums2[n-1]
        n -=1
        last -=1

    # iterate over nums1 and then reprint everything here
    for x in nums1:
        print(x)


arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 3]
m = len(arr1)
n = len(arr2)
# s = Solution()
merge2SortedArray(arr1, m, arr2, n)
