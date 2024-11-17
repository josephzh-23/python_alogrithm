'''


The problem here is actually quite simple as said

Sorted in non-decreasing order

'''
from typing import List


'''

The way this works is pretty interesting as said 
'''

def merge(self, nums1: List[int], total_nums1: int, nums2: List[int], total_nums2: int) -> None:
    """
    Merges two sorted arrays, nums1 and nums2, into a single sorted array.
    The first array nums1 has a size sufficient to hold the contents of both arrays.
    The merge is done in-place.

    :param nums1: List[int], the first sorted array with extra space for nums2.
    :param total_nums1: int, the number of valid elements in nums1.
    :param nums2: List[int], the second sorted array to be merged into nums1.
    :param total_nums2: int, the number of elements in nums2.
    """
    # Initialize pointers for nums1 and nums2 starting from the end of their valid elements



    '''
    We need to go from the back here and try to approach this question 
    
    and then so what we do is basically 
    
    '''
    index1, index2 = total_nums1 - 1, total_nums2 - 1

    # Start filling nums1 from the end, to avoid overwriting elements of nums1 that are not yet merged
    finalIndex = total_nums1 + total_nums2 - 1


    '''
    and now porabbly even less stuff as compared to before right
    This way when going from the back we can always make sure we have the biggest element on the back here and that's what we
    want to see here 
    
    And this is good then cause we have an easier time then doing this problem 
    '''
    # Merge in reverse order
    while index2 >= 0:
        # If nums1 is not yet exhausted and the current element is larger than nums2's, place it in the current position
        if index1 >= 0 and nums1[index1] > nums2[index2]:
            nums1[finalIndex] = nums1[index1]
            index1 -= 1  # Move the nums1 index backwards
        else:
            # Else, place element from nums2
            nums1[finalIndex] = nums2[index2]
            index2 -= 1  # Move the nums2 index backwards
        finalIndex -= 1  # Move the merge index backwards