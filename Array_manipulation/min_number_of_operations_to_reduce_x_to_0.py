
'''
You are given an integer array nums and an integer x.
In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.



'''

class Solution:
    def min_operations(self, nums, x):
        n = len(nums)
        total_sum = sum(nums)

        # If the total sum is equal to 'x', no operations are needed
        if total_sum == x:
            return n

        # Calculate the difference between the total sum and 'x'
        total_sum -= x
        i, j = 0, 0
        curr_sum = 0
        ans = 0

        # Sliding window approach to find the minimum operations
        while j < n:
            curr_sum += nums[j]

            # If the current sum is greater than the target difference,
            # move the window's left end (i) to reduce the sum
            while i < j and curr_sum > total_sum:
                curr_sum -= nums[i]
                i += 1

            # If the current sum equals the target difference,
            # update the answer with the maximum window size
            if curr_sum == total_sum:
                ans = max(ans, j - i + 1)

            j += 1

        # If 'ans' is still 0, it means no subarray with the target sum was found
        return -1 if ans == 0 else n - ans


# Driver code
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 4, 2, 3]
    x = 5
    result = solution.min_operations(nums, x)

    if result == -1:
        print("No solution found.")
    else:
        print("Minimum operations required:", result)