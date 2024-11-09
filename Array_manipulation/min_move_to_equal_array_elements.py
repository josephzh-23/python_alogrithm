'''

This is problem 453, there is no trick to this questino just math here

Make all eleemnts equal here

Given an integer array nums of size n,
return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

[1, 2, 3]

1.
Calculate the sum of all numbers in the array with sum(nums)
which iterates over nums once.

2.
Find the minimum number in the array with min(nums)
which also iterates over nums once.

3.
Multiply the minimum element by the number of elements in the array with
min(nums) * len(nums). This gives the sum of elements if all of them were the minimum value.

4.
Subtract the sum of all elements as if they were the minimum value from the actual sum of the array elements to get the total number of increments needed.

The result of the subtraction sum(nums) - min(nums) * len(nums) is the answer to the problem, which is returned by the solution function.
'''


class Solution:
    def minMoves(self, nums) -> int:
        # Calculate the sum of all numbers in the list
        total_sum = sum(nums)
        # Find the minimum value in the list
        min_value = min(nums)
        # Calculate the number of moves required to equalize the values
        # by subtracting the product of the minimum value and list length from the total sum
        moves = total_sum - min_value * len(nums)

        return moves
