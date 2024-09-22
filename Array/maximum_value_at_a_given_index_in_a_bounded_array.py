'''
This questoin is rated tough as seen here


n = 4, index = 2, maxSUm = 6 here


Conditions
sum of all the nums does not exceed maxSum up here
abs(nums[i] - nums[i + 1]) <= 1     where 0 <= i < n -1



What this is sayign is basically you have

n = 4, index = 2, maxSum = 7 here and then you want to make this work here

Solutions:

1) We know that nums[index] must be a positive integer and
 that the sum of all elements in the array must not exceed maxSum.
  This means that nums[index] has an upper bound given by maxSum.

2) Use bin search, lowest possible value for nums[index] 1 and the max
possible value which is maxSum here

3) For each possible value of nums[index] we test in our binary search, we calculate the sum of elements that would be required to form a valid array if nums[index] were that value. To do this, the sum function is used,
which calculates the sum of elements in either the left or the right here

The key:

In order to maximize the sum here so what we do is we let the number




A couple of cases here that's very important here

4) If calculated sum <= maxSum,
    can increase nums[index]



'''
import math


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:


        '''
This function calculates the sum of the first cnt terms of an arithmetic series that
starts at x and decreases by 1 each term until it reaches 1 or runs out of term


        '''
        def calculate_sum(start_value, count):

            if start_value >= count:
                # If the start value is larger than or equal to count,
                # calculate the sum of the first `count` numbers in the arithmetic series
                # descending from `start_value`

                return (start_value + start_value - count + 1) * count // 2
            else:
                # If start_value is less than count, then the series is not long
                # enough to decrease down to 1. It bottoms out at 1 after `start_value` steps
                # Then we have to count the remaining `count - start_value` times 1.
                return (start_value + 1) * start_value // 2 + count - start_value

        left, right = 1, maxSum  # Set the search range between 1 and maxSum

        while left < right:      # Use binary search to find maximum value
            mid = (left + right + 1) >> 1  # Calcualte the middle point

            # Check if the sum of both sides with `mid` as the peak value is <= maxSum
            if calculate_sum(mid - 1, index) + calculate_sum(mid, n - index - 1) + mid <= maxSum:
                left = mid   # If it's less than or equal to maxSum, this is a new possible solution
            else:
                right = mid - 1  # If it exceeds maxSum, we discard the mid value and go lower

        return left  # At the end of the loop, `left` is our maximum value

# Example of how to use the class
# solution = Solution()
# result = solution.maxValue(10, 5, 54)
# print(result)  # The results would print the maximum value that can be achieved


