'''

The result is sorted here

1. Finding the closest # to x in arr
2.  the 3rd closest number to x must be either to
the left of the first number or to the right of the second number.

3. Left to start of the array and right = len(arr) - k

    Perform a binary search between l and r


4. Check if x is closer to arr[mid] or arr[mid + k]



'''
from typing import List


def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    # Initialize the left and right pointers for binary search.
    # The right pointer is set to the highest starting index for the sliding window.
    left, right = 0, len(arr) - k

    # Perform binary search to find the left bound of the k closest elements.
    while left < right:
        # Calculate the middle index between left and right.
        mid = (left + right) // 2

        '''
        Check the distance from x to the middle element 
        If elem at mid is closer to x 
        or equal in distance compared to the element at mid + k
        
        Mve right pointer to mid because we know it's in the left side 
        
    else:
        we move it to the right here 
        '''
        if x - arr[mid] <= arr[mid + k] -x:
            right = mid
        else:
            left = mid + 1

    # Extract the subarray from the left index of size k, which will be the k closest elements.
    return arr[left:left + k]