'''

The problem here

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

 We need to find the number of subarrays where 2 is the smallest integer, here ->
 [1, 6] index:

 2. q1 how to count # of subarrays that contaisn 2 as smallest from the given range?
there r 4 elem before ([3, 4, 5, 2]) and 3 elem after ([2, 3, 4]) so total is
3 * 4= 12 (trust this part as this can not be faked over here) as said


step 3:
 how to get range where each elem is smallest?

- . For this, we find the nearest element on the left, which is less than itself. Then, find the closest element on
the right, which is less than itself. If i and j are the indices of these elements on the left and right,
then [i+1,j−1] indices create our range.


Step 4:
Use monotonic stack to -> value of i and j here
And just build the monotonic stack here




Step 5:
There is an edge case of  Duplciate elements 4.possbile in the case of [2, 2, 2],


Deciding on the left and right boundary here

While finding the boundary elements for a
range,

we look for elements that are strictly less than the current element on the left. To decide the right
boundary, we look for the elements which are less than or equal to the current element

Example - [3, 1, 5, 2, 6, 2, 8, 2, 1]

Appears at idx : 3, 5, 7 here, and then
When calculating the range for the second 2 (at index 5),
right bound = 7
left bound = 1  (which is 1 here)

For the 3rd 2 here:
right bound = 8         (next smallest)
left bound = -1         (previous smallest)        this is b/c the stack is empty by this point that's why we have this



. '''
from typing import List


def sumSubarrayMins(self, arr: List[int]) -> int:
    MOD = 10 ** 9 + 7
    stack = []
    sum_of_minimums = 0;

    for i in range(len(arr) + 1):

        # when i reaches the array length, it is an indication that
        # all the elements have been processed, and the remaining
        # elements in the stack should now be popped out.

        while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
            # Notice the sign ">=", This ensures that no contribution
            # is counted twice. right_boundary takes equal or smaller
            # elements into account while left_boundary takes only the
            # strictly smaller elements into account

            mid = stack.pop()
            left_boundary = -1 if not stack else stack[-1]
            right_boundary = i

            # count of subarrays where mid is the minimum element
            count = (mid - left_boundary) * (right_boundary - mid)
            sum_of_minimums += (count * arr[mid])

        stack.append(i)

    return sum_of_minimums % MOD


