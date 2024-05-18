'''
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2],
 [2,4], [3,1,2], [1,2,4], [3,1,2,4].

 And then you have
 Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

1.  If we know that an element is the smallest in a given range,
 we can determine the number of subarrays in this range that contain this element

 2. Example:
 [0, 3, 4, 5 ,2, 3, 4, 1, 4]

 We need to find the number of subarrays where 222 is the smallest integer, here ->
 [1, 6] index:

 2. q1 how to count # of subarrays that contaisn 2 as smallest fromt the given range?
there r 4 elem before ([3, 4, 5, 2]) and 3 elem after ([2, 3, 4]) so total is
3 * 4= 12

3. how to get range where each elem is smallest?

- . For this, we find the nearest element on the left, which is less than itself. Then, find the closest element on
the right, which is less than itself. If iii and jjj are the indices of these elements on the left and right,
then [i+1,j−1][i + 1, j - 1][i+1,j−1] indices create our range.

Use monotonic stack to -> value of i and j here
And just build the monotonic stack here

Edge case here 1. Duplciate elements 4.possbile in the case of [2, 2, 2],
While finding the boundary elements for a
range, we look for elements that are strictly less than the current element on the left. To decide the right
boundary, we look for the elements which are less than or equal to the current element

Example - [3, 1, 5, 2, 6, 2, 8, 2, 1]

Appears at idx : 3, 5, 7 here, and then
When calculating the range for the second 222 (at index 555), we calculate

the next smaller element to be the 2 at index 7. The previous smaller
 comes from strict comparison, though,
so the previous smaller element is 1 at index 1 here (as mentioned before strictly < cur elem on the left
b/c of the edge case) here



. '''
from typing import List


def sumSubarrayMins(arr: List[int]) -> int:
    MOD = 10 ** 9 + 7
    stack = []
    sum_of_minimums = 0;

    for i in range(len(arr) + 1):
        while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
            '''
            # the edge case we mentioned of 3 duplicates [3, 1, 5, 2, 6, 2, 8, 2, 1]
            # Notice the sign ">=", This ensures that no contribution
            # is counted twice. right_boundary takes equal or smaller
            # elements into account while left_boundary takes only the
            # strictly smaller elements into account
            '''
            mid = stack.pop()

            # whatever was the top
            left_boundary = -1 if not stack else stack[-1]
            right_boundary = i
            # The previous smaller item's index comes from the current top of stack. If the stack is empty,
            # we consider it −1.

            # # of subarrays that has the mid as minimum here
            count = (mid - left_boundary) * (right_boundary - mid)
            sum_of_minimums += (count * arr[mid])

        stack.append(i)

    return sum_of_minimums % MOD


