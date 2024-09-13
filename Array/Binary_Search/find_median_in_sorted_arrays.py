'''
Help you find half the partition in the left array here


This is straight taking frmo the left
'''
from typing import List


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A

        '''
        
        Why subtract 2? j and i both start at 0  to account for both i and j 
        
        The value we will use to compare here, A[i + 1] 
        '''
        j = half - i - 2  # B


        '''
        Break into the left and right partition here 
        to the value here and then that's the one you want here 
        
        '''

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd $ of eleemtsn
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        # reducing the size of left partition from a here
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1